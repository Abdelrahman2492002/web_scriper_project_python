import requests
from bs4 import BeautifulSoup

response = requests.get("https://books.toscrape.com/")
soup = BeautifulSoup(response.content, "html.parser")

books = soup.findAll("article")
def get_book_info(book):
    title_element = book.h3.a
    rating_element = book.p
    price_element = book.find('p', class_='price_color')

    if title_element and rating_element and price_element:
        title = title_element.get("title", "No title available")
        rating = rating_element["class"][1] if len(rating_element["class"]) > 1 else "No rating available"
        price = price_element.get_text(strip=True)

        return title, rating, price
    else:
        return None

for book in books:
    book_info = get_book_info(book)
    
    if book_info:
        title, rating, price = book_info
        print(f"The title is: {title} and The rating is {rating} stars and the price: {price}")
    else:
        print("Some information is missing for this book.")
