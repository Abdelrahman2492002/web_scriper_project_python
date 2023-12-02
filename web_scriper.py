import requests
from bs4 import BeautifulSoup

response = requests.get("https://books.toscrape.com/")
soup = BeautifulSoup(response.content, "html.parser")

books = soup.findAll("article")

for book in books:
    title = book.h3.a["title"]
    rating = book.p["class"][1]
    price = book.find('p', class_ ='price_color').get_text(strip=True)
    print(f"The title is : {title} and The rating is {rating} stars and the price : {price}")