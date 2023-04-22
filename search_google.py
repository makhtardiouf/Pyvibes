import requests

def google_search(query):
    """Searches Google for the given query """

    url = f'https://www.google.com/search?q={query}'
    response = requests.get(url)
    print(response.text)
    if response.status_code == 200:
        return response.json()

    else:
        raise Exception('Error searching Google: {}'.format(response.status_code))

if __name__ == '__main__':
    try:
        query = input('What would you like to search for? ').strip()
        print(f"Query: {query}")

        results = google_search(query)

        for result in results['items']:
            print('Title: {}'.format(result['title']))
            print('URL: {}'.format(result['link']))

    except Exception as e:
        print(f"Search failed: {e}")

