from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'http://www.scrapethissite.com/pages/forms/'

page = requests.get(url)


# <Response [200]>

soup = BeautifulSoup(page.text, features="html.parser")
# page is sending the request & html is retrieving raw html I am using
# html will parse the info in an html format
print(soup)

soup.find('table')


soup.find('table', class_='table')


table = soup.find('table')
print(table)


# soup.find('th').text.strip()
# = 'Team Name'


column_titles = table('th')
print(column_titles)

# looping through each column header/title[th tag] so I can loop trough to get each header/title
hockey_column_titles = [title.text.strip() for title in column_titles]
print(hockey_column_titles)
# ['Team Name', 'Year', 'Wins', 'Losses', 'OT Losses', 'Win %', 'Goals For (GF)', 'Goals Against (GA)', '+ / -']


# enter titles into pandas data frame

df = pd.DataFrame(columns=hockey_column_titles)
df
