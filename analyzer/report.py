from datetime import datetime
import os

def generate_html_report(data, all_links):
    html = f"<html><body><h1>VulnVoyager Report</h1><p>Generated: {datetime.now()}</p>"
    for site in data:
        html += f"<h2>{site['url']}</h2><h3>Headers</h3><ul>"
        for k, v in site['headers'].items():
            html += f"<li>{k}: {v}</li>"
        html += "</ul><h3>SSL Info</h3><pre>" + str(site['ssl']) + "</pre>"
        html += "<h3>Technologies</h3><ul>" + "".join(f"<li>{t}</li>" for t in site['technologies']) + "</ul>"
        html += "<h3>Forms</h3><ul>"
        for form in site['forms']:
            html += f"<li>Action: {form['action']}, Method: {form['method']}</li>"
        html += "</ul>"
    html += "</body></html>"

    filename = f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
    path = os.path.join(os.getcwd(), filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    return filename
