import json
import requests
from bs4 import BeautifulSoup
books_json_list=[]
next_page = True
page =1
while next_page:
    api_url = f"https://books.toscrape.com/catalogue/page-{page}.html"
    response = requests.get(url=api_url)
    soup = BeautifulSoup(response.text,'lxml')
    articles = soup.find_all("article",class_="product_pod")
    if not articles:
        break
    else:
        for article in articles:
            title = article.h3.a["title"]
            price = article.find("p",class_="price_color").text.strip("Â£")
            books_json_list.append({"Book Name" : title , "Price " : price})
    page +=1

with open("books.json","w") as datafile:
    json.dump(books_json_list,datafile,indent=4)