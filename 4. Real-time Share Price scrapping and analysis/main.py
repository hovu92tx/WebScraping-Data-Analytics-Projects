import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import requests


def get_data(link):
    # Access the page
    # driver = webdriver.Chrome()
    # driver.get(link)
    # html = driver.page_source

    response = requests.get(link)
    html = response.content
    # Create soup object
    soup = BeautifulSoup(html, 'html.parser')
    # Extract data 
    stock = soup.find('div', attrs={'class':'md:relative md:bg-white'})
    if stock:
        company_name = stock.find('h1', attrs = {'class':'mb-2.5 text-left text-xl font-bold leading-7 text-[#232526] md:mb-2 md:text-3xl md:leading-8 rtl:soft-ltr'}).string
        price = stock.find('div', attrs = {'class':'text-5xl/9 font-bold text-[#232526] md:text-[42px] md:leading-[60px]'}).string
        date = stock.find('time', attrs = {'class':'whitespace-nowrap text-xs/4 font-normal text-[#5B616E]'}).string
    info = [company_name, price, date]
    # driver.quit()
    return info 


if __name__ == '__main__':
    urls = [
    'https://www.investing.com/equities/nike',
    'https://www.investing.com/equities/coca-cola-co',
    'https://www.investing.com/equities/microsoft-corp',
    'https://www.investing.com/equities/3m-co',
    'https://www.investing.com/equities/american-express',
    'https://www.investing.com/equities/amgen-inc',
    'https://www.investing.com/equities/apple-computer-inc',
    'https://www.investing.com/equities/boeing-co',
    'https://www.investing.com/equities/cisco-sys-inc',
    'https://www.investing.com/equities/goldman-sachs-group',
    'https://www.investing.com/equities/ibm',
    'https://www.investing.com/equities/intel-corp',
    'https://www.investing.com/equities/jp-morgan-chase',
    'https://www.investing.com/equities/mcdonalds',
    'https://www.investing.com/equities/salesforce-com',
    'https://www.investing.com/equities/verizon-communications',
    'https://www.investing.com/equities/visa-inc',
    'https://www.investing.com/equities/wal-mart-stores',
    'https://www.investing.com/equities/disney',
    ]
    stock_list = []
    for link in urls:
        stock_list.append(get_data(link))
    for stock in stock_list:
        name = stock[0].strip()
        price= stock[1].strip()
        date = stock[2].strip()
        print('Name: ',name,'\n','Price: $',price, '\n','Date: ',date,'\n','_'*40,'\n' )
    # df = pd.DataFrame(stock_list, index= False)
    # df.to_csv('4. Real-time Share Price scrapping and analysis\stock_list.csv')

