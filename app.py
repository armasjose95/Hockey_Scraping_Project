from bs4 import BeautifulSoup
import requests

url = 'http://www.scrapethissite.com/pages/forms/'

page = requests.get(url)

# <Response [200]>

soup = BeautifulSoup(page.text, 'html')
# page is sending the request & html is retrieving raw html I am using
# html will parse the info in an html format

print(soup.prettify())
