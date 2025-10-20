from bs4 import BeautifulSoup
import requests as rq

page = rq.get("https://quotes.toscrape.com/")

soup = BeautifulSoup(page.content, 'html.parser')

quotes = soup.find_all('span', class_ = 'text')
authors = soup.find_all('small',  class_ = 'author')
for i in range(len(quotes)):
    print(quotes[i].text," : ",authors[i].text )
    print()


def find_by_authors(author):
    content = soup.find_all('div',class_= 'quote')

    for i in content:
        quote = i.find('span', class_='text')
        author = i.find('small', class_= 'author')

        if(author == author.text):
            print(quote.text, " ", author.text, "\n")

find_by_authors('Albert Einstein')