from crawler import crawl_site
import json

DOMAINS = {
    "https://www.virgio.com/collections/women": "www.virgio.com",
    "https://www.tatacliq.com/bags/c-msh1010104": "www.tatacliq.com",
    "https://www.nykaafashion.com/women/clothing/c/6557": "www.nykaafashion.com",
    "https://www.westside.com/collections/women-dresses": "www.westside.com"
}

def main():
    all_products = {}

    for url, domain in DOMAINS.items():
        print(f"\n🔍 Crawling {url} ...")
        try:
            product_urls = crawl_site(url)
            print(f"✅ Found {len(product_urls)} product URLs.")
            all_products[domain] = product_urls
        except Exception as e:
            print(f"❌ Failed to load {url}: {e}")
            all_products[domain] = []

    with open("product_urls.json", "w") as f:
        json.dump(all_products, f, indent=4)

    print("\n🎉 All done! Output saved to product_urls.json")

if __name__ == "__main__":
    main()
