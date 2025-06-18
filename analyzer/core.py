import requests, ssl, socket, tldextract
from bs4 import BeautifulSoup

def fetch_headers(url):
    try:
        response = requests.get(url, timeout=10)
        return response.headers, response.text
    except Exception as e:
        return {"Error": str(e)}, ""

def fetch_ssl_info(domain):
    try:
        ctx = ssl.create_default_context()
        conn = ctx.wrap_socket(socket.socket(), server_hostname=domain)
        conn.settimeout(5)
        conn.connect((domain, 443))
        return conn.getpeercert()
    except Exception as e:
        return {"Error": str(e)}

def detect_technologies(html):
    tech = []
    if 'wp-content' in html: tech.append("WordPress")
    if 'jquery' in html.lower(): tech.append("jQuery")
    if 'cloudflare' in html.lower(): tech.append("Cloudflare")
    return tech

def scan_forms(html):
    soup = BeautifulSoup(html, 'html.parser')
    forms = []
    for form in soup.find_all('form'):
        forms.append({
            'action': form.get('action'),
            'method': form.get('method', 'GET'),
            'inputs': [
                {'name': inp.get('name'), 'type': inp.get('type')}
                for inp in form.find_all('input')
            ]
        })
    return forms

def analyze_site(url):
    domain = tldextract.extract(url).fqdn
    headers, html = fetch_headers(url)
    ssl_info = fetch_ssl_info(domain)
    technologies = detect_technologies(html)
    forms = scan_forms(html)

    return {
        "url": url,
        "headers": headers,
        "ssl": ssl_info,
        "technologies": technologies,
        "forms": forms,
    }
