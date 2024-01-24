
from bs4 import BeautifulSoup
import requests
import pandas as pd

# sending an HTTP requests with Request and all I need to do is
# set an URL and pass it through requests.get(),
# store the returned HTML inside a page variable
# and print response.status_code.

url = 'http://www.scrapethissite.com/pages/forms/'
page = requests.get(url)
print(page.status_code)
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
# imported pandas
# headers are now printed
df = pd.DataFrame(columns=hockey_column_titles)
df


# start pulling in data for each column
# they come in with their headers, so will need to get rid of them
column_data = table.find_all('tr')


# need to loop through because this is a list
# as it gets looped through I'm finding all and looking for the td tags(individual data(row data))
# then I'm taking each piece of data & getting out the text & stripping it to clean it
# now in a list for each individual row
for row in column_data[0:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]


# then take the length and use it when I put in this new info
# checking length of our data frame each time it's looping through
# and then I'm going to put the info in the next position by appending it to our empty data frame
length = len(df)
df.loc[length] = individual_row_data
df


df.to_csv(r'/Users/josearmas/Desktop/Hockey_Scraping_Project\Teams.csv', index=False)
