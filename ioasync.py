# https://docs.python.org/3.5/whatsnew/3.5.html
# Coroutines with async and await syntax

import asyncio

async def http_get(url):
    reader, writer = await asyncio.open_connection(url, 80)

    writer.write(b'\r\n'.join([
        b'GET / HTTP/1.1',
        b'Host: %b' % url.encode('latin-1'),
        b'Connection: close',
        b'', b''
    ]))

    async for line in reader:
        print('>>', line)

    writer.close()

loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(http_get('www.google.com'))
finally:
    loop.close()
