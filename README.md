# 📚 Books to Scrape - Web Scraper

This project is a simple **Python web scraping script** that extracts book titles and their prices from [Books to Scrape](https://books.toscrape.com/).  
The scraped data is stored in a JSON file (`books.json`) for further use.

---

## 🚀 Features
- Scrapes all available pages from [Books to Scrape](https://books.toscrape.com/).
- Extracts:
  - Book Title  
  - Book Price (£)
- Saves the scraped data into a **JSON file** with clean formatting.

---

## 🛠️ Requirements
Make sure you have the following installed:

- Python 3.x
- [Requests](https://pypi.org/project/requests/)
- [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/)
- [lxml](https://pypi.org/project/lxml/)

Install dependencies with:
```bash
pip install requests beautifulsoup4 lxml
```
📂 Project Structure
```bash
.
├── books.json      # Output file with scraped data
├── scraper.py      # Python script (your main code)
└── README.md       # Documentation

```
## ▶️ Usage
Run the script with:

```bash
python scraper.py
After execution, a file named books.json will be created with book names and prices.

```

## Example output (in books.json):
```
json
[
    {
        "Book Name": "A Light in the Attic",
        "Price ": "51.77"
    },
    {
        "Book Name": "Tipping the Velvet",
        "Price ": "53.74"
    }
]

```
## 🌐 Source
This project scrapes data from the demo website:
👉 Books to Scrape
(A website specifically created for practicing web scraping.)

## ⚠️ Disclaimer
This scraper is intended for educational purposes only.
Always check a website’s robots.txt and terms of service before scraping.

yaml
Copy code
