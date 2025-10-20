from bs4 import BeautifulSoup
import requests as req


page = req.get('https://quotes.toscrape.com/', verify=False)

soup = BeautifulSoup(page.content, 'html.parser')

# print(soup)


page_heading = soup.find('a') #returns the first 'a' element from the page first matching tag
print(page_heading)
print(page_heading.get_text())
print(page_heading.text)

quotes = soup.find_all('div', class_='quote')
for quote in quotes:
    quote_text = quote.find('span', class_ = 'text')
    author = quote.find('small', class_ = 'author')
    print(quote_text.text)
    print(author.text)


def show_quotes_byauthor(author):
    quotes = soup.find_all('div', class_='quote')
    for quote in quotes:
        quote_text = quote.find('span', class_ = 'text')
        author = quote.find('small', class_ = 'author')
        # if(author.text == author):

        print(quote_text.text)
        print(author.text)