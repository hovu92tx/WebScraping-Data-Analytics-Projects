from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
import re
def ScrapeData(link):
    # Get web's html code
    driver = webdriver.Chrome()
    driver.get(link)
    time.sleep(10)
    html = driver.page_source
    # Create soup object
    soup = BeautifulSoup(html, 'html.parser')
    product = soup.find('div', attrs={'id':"dp-container"})
    if product:
        title = product.find('span', class_='a-size-large product-title-word-break').string
        price = product.find('span', class_='a-offscreen').string
        rating_count = re.findall(r'\b\d{1,3}(?:,\d{3})*\b',product.find('span', id='acrCustomerReviewText').string)
        rating = product.find('span', class_='a-icon-alt').string
    product_detail ={'title': title, 'Price': price, 'Rating': rating[:4],'Votes': rating_count[0]}
    return product_detail

if __name__ == '__main__':
    
    #Read csv file to get product's links
    # links = open('link.csv', 'r')
    # for link in links.readlines():
    #     print(ScrapeData(link))

    data = ScrapeData("https://www.amazon.com/Lulu-Home-Concentrated-Solution-Machine/dp/B087QHXW6Z/ref=lp_21571225011_1_1?pf_rd_p=53d84f87-8073-4df1-9740-1bf3fa798149&pf_rd_r=FSGVH39SYK0FZ1JA2XJ1&sbo=RZvfv%2F%2FHxDF%2BO5021pAnSA%3D%3D")
    print('Product\'s name:', data['title'].strip(),'\n', 'Price:', data['Price'],'\n','Rating:',data['Rating'],'\n', 'Number of votes:', data['Votes'])