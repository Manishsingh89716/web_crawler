﻿# 🕷️ E-commerce Product URL Crawler

This project is a web crawler built for discovering product page URLs from multiple e-commerce websites like:

- [Virgio](https://www.virgio.com/)
- [TataCliq](https://www.tatacliq.com/)
- [Nykaa Fashion](https://www.nykaafashion.com/)
- [Westside](https://www.westside.com/)

## 🚀 Objective

Automatically crawl and extract all product URLs from e-commerce category pages, even if content is dynamically loaded.

---

## 🛠️ Tech Stack

- Python 🐍
- [Playwright](https://playwright.dev/python/) (for browser automation)
- Regex (for identifying product page patterns)
- JSON (for structured output)

---

## 📁 Project Structure

E-commerce_web_crawler/ 
├── main.py # Driver script to run the crawler 
├── crawler.py # Contains crawling logic using Playwright 
├── product_urls.json # Output file (auto-generated) 
├── README.md


## ▶️ How to Run

### 1. Install dependencies

pip install -r requirements.txt
playwright install
2. Run the script
python main.py
Product URLs will be saved to product_urls.json.

📦 Output Format
json
{
  "nykaafashion.com": [
    "https://www.nykaafashion.com/product/123",
    "https://www.nykaafashion.com/product/456"
  ],
  "tatacliq.com": []
}

Loom Demo:- https://www.loom.com/share/3d0e6fe1f11b4122838e2316e866115e?sid=bee858f2-0126-4572-b968-fe615dd01a80

✅ Features
Handles dynamic content with scrolling

Filters direct product page URLs using URL patterns

Works across multiple domains

Easy to scale and extend

🔒 Note
Some websites might block automation tools or load content via complex JavaScript frameworks — so Playwright with headless browser is used for better rendering.

👨‍💻 Author
Manish Singh
