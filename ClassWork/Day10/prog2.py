from bs4 import BeautifulSoup
import requests as req

page = req.get('https://quotes.toscrape.com/')

soup = BeautifulSoup(page.content, 'html.parser')

# print(type(soup))

# print(soup.prettify)


############################## To get quotes by authors #########################
page_heading = soup.find('a')

quotes = soup.find_all('span', class_ = 'text')
authors = soup.find_all('small', class_ = 'author')
for i in range(len(quotes)):
    print(f'{quotes[i].text} : by {authors[i].text}\n')


###################################################################################

# print(type(quotes))
# print(quotes)

# print(page_heading)

# print(type(page_heading))

def quotes_by_authors(author):
    quotes_page = soup.find_all('div', class_ = 'quote')
    
    for quotes in quotes_page:
        quote = quotes.find('span', class_ = 'text')
        authors = quotes.find('small', class_ = 'author')
        
        # if(authors == author):
        print(f'{quote.text} : {authors.text}\n')



quotes_by_authors('Albert Einstein')