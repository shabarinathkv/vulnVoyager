import argparse
from analyzer.core import analyze_site
from analyzer.crawler import crawl_links
from analyzer.report import generate_html_report

def main():
    parser = argparse.ArgumentParser(description="VulnVoyager - Website Security Analyzer")
    parser.add_argument("url", help="Target website URL (e.g. https://example.com)")
    parser.add_argument("--depth", type=int, default=1, help="Crawl depth for internal links")
    args = parser.parse_args()

    print(f"[+] Crawling internal links from {args.url} (depth={args.depth})...")
    urls = crawl_links(args.url, max_depth=args.depth)

    print(f"[+] Analyzing {len(urls)} pages...")
    results = [analyze_site(url) for url in urls]

    print("[+] Generating report...")
    output_path = generate_html_report(results, urls)
    print(f"[✓] Report saved to {output_path}")

if __name__ == "__main__":
    main()
