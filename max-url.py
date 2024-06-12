import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def parse_urls(url):
    internal_links = set()
    external_links = set()

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        for link in soup.find_all('a', href = True):
            href = link['href']
            if href.startswith('#'):
                continue
            if urlparse(href).netloc == '':
                internal_links.add(href)
            else:
                external_links.add(href)
        
        total_urls = len(internal_links) + len(external_links)

        with open('urls.txt', 'w') as file:
            for link in internal_links.union(external_links):
                file.write(link + '\n')

        print(f'total internal links: {len(internal_links)}')
        print(f'tetal external links: {len(external_links)}')
        print(f'total urls: {total_urls}')
    
    except requests.exceptions.RequestException as e:
        print(f' an error occured {e}')

url = input('here paste your url: ')
parse_urls(url)