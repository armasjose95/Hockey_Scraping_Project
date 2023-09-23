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


soup.find_all('div', class_='col-md-12')  # returns just this information
# you can return multiple if there is multiple

soup.find_all('p')  # returns just this 'p' information
