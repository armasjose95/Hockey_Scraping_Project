from bs4 import BeautifulSoup
import requests

url = 'http://www.scrapethissite.com/pages/forms/'

page = requests.get(url)

# <Response [200]>

soup = BeautifulSoup(page.text, 'html')
# page is sending the request & html is retrieving raw html I am using
# html will parse the info in an html format

print(soup.prettify())

# soup.find('div') # this finds the first 'div' class


# soup.find_all('div') # finds all 'div' on the page
# a ',' comma separates each 'div' class


# soup.find_all('div', class_='col-md-12')  # returns just this information
# you can return multiple if there is multiple

# soup.find_all('p')  # returns any 'p' information


# soup.find_all('p', class_= 'lead') # find 'p' div w/ specific lead class

# .text
# trying to pull some info or a paragraph of text for ex.
# soup.find_all('p', class_= 'lead').text # error
# error because i'm using find all and find all doesn't have a text attribute
# can switch to just find
# use find_all most of the time unless you want to extract text


soup.find('p', class_='lead').text.strip()
# pulls text between quotes no longer in a list or with 'p' tags for ex. or class attribute
