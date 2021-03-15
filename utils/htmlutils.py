from splinter import Browser
import requests

def get_html(url):
    r = requests.get(url)
    if r.status_code == 200:
        return r.text
    return None

def get_html_with_js(url):
    html = None
    try:
        browser = Browser("firefox", headless=True)
        browser.visit(url)
        html = browser.html
        browser.quit()
    except Exception as e:
        print(e)
    return html