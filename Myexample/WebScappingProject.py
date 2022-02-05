import requests
import bs4
base_url = 'https://books.toscrape.com/catalogue/page-{}.html'
res = requests.get(base_url.format(1))
soup= bs4.BeautifulSoup(res.text,'lxml')
#print(soup)
products = soup.select(".product_pod")
#print(products[0])

# MAin Code for grabbing every book having two star rating in the website
all_books = []
for n in range(1,51):
    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)

    soup = bs4.BeautifulSoup(res.text,"lxml")
    books = soup.select(".product_pod")

    for book in books:
        if len(book.select('.star-rating.Two')) != 0:
            book_title = book.select('a')[1]['title']
            all_books.append(book_title)

print(all_books)