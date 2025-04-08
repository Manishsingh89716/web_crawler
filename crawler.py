from playwright.sync_api import sync_playwright
import re
import time

PRODUCT_PATTERNS = [r"/product[s]?/", r"/p/", r"/item/", r"/prod/", r"/shop/", r"/products/"]

def is_product_url(url):
    return any(re.search(pattern, url) for pattern in PRODUCT_PATTERNS)

def crawl_site(domain_url):
    product_urls = set()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(viewport={"width": 1280, "height": 800})
        page = context.new_page()

        print("🌐 Loading page...")
        page.goto(domain_url, timeout=70000)

        # Scroll slowly to bottom
        print("🔄 Scrolling for dynamic content...")
        for i in range(15):
            page.evaluate("window.scrollBy(0, document.body.scrollHeight)")
            time.sleep(1.5)

        print("🔎 Extracting links...")
        anchors = page.query_selector_all("a")
        for anchor in anchors:
            href = anchor.get_attribute("href")
            if href:
                # Handle relative URLs
                if href.startswith("/"):
                    base = domain_url.split("/")[0] + "//" + domain_url.split("/")[2]
                    href = base + href
                if is_product_url(href):
                    product_urls.add(href.split("?")[0])

        browser.close()
    return list(product_urls)
