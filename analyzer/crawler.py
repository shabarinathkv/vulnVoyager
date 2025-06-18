from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import requests

def crawl_links(start_url, max_depth=2):
    visited = set()
    results = []

    def crawl(url, depth):
        if depth > max_depth or url in visited:
            return
        try:
            response = requests.get(url, timeout=10)
            visited.add(url)
            results.append(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            for link in soup.find_all('a', href=True):
                full_url = urljoin(url, link['href'])
                if urlparse(full_url).netloc == urlparse(start_url).netloc:
                    crawl(full_url, depth + 1)
        except: pass

    crawl(start_url, 0)
    return results
