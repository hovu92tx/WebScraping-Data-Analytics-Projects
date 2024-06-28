# Import the required modules.
from bs4 import BeautifulSoup
import pandas as pd
import requests
from selenium import webdriver
import re

# Access the HTML content from the webpage.
url = 'http://www.imdb.com/chart/top'
driver = webdriver.Chrome()
driver.get(url)
html= driver.page_source
# Create soup object
soup = BeautifulSoup(html, "html.parser")

# Get information from the soup object
movies = soup.find_all("li", class_="ipc-metadata-list-summary-item sc-10233bc-0 iherUv cli-parent")
lst= []

for movie in movies:

    # Extract the title
    title_tag = movie.find("h3",class_='ipc-title__text')
    title = title_tag.text.strip() if title_tag else 'NA'

    # Extract the year
    year_tag = movie.find('span', class_='sc-b189961a-8 kLaxqf cli-title-metadata-item')
    year = year_tag.text if year_tag else 'NA'

    # Extract the rating
    rating_tag = movie.find('span', class_='ipc-rating-star--imdb')
    rating = rating_tag.text.strip()[:3] if rating_tag else 'NA'

    # Extract the votes
    votes_tag = movie.find('span', class_='ipc-rating-star--voteCount')
    votes = votes_tag.text.strip() if votes_tag else 'N/A'
    vote_number = re.findall(r'\d+\.\d+|\d+', votes)

    # store the extracted information
    data ={"Title": title,"Year": year,"Rating": rating,"Votes": vote_number[0]}
    lst.append(data)

# Load data into a Data Frame
df = pd.DataFrame(lst)

# Save data frame into a csv file
df.to_csv('1. Movies Review Scraping And Analysis\imdb_top_250_movies.csv',index=False)
# Close webdriver 
driver.quit()