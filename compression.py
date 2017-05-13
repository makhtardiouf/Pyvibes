__author__ = 'Makhtar'  # Modules zlib, gzip, bz2, lzma, zipfile and tarfile.
import zlib

s = b'witch which has which witches wrist watch'
print(s, len(s))

t = zlib.compress(s)
print("compressed to: ", t, len(t))

zlib.decompress(t)

print("CRC value: ", zlib.crc32(s))

