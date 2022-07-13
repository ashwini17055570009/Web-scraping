#give data of all postings of 15 pages of carpages website
import requests
from bs4 import BeautifulSoup
import pandas as pd

url='https://www.carpages.ca/used-cars/search/?category_id=1'

page=requests.get(url)
page

soup=BeautifulSoup(page.text,'lxml')
soup
df=pd.DataFrame({'Link':[''],'name':[''],'color':[''], 'price':['']})
a=0
while a<=15:
    postings=soup.find_all('div',class_='media soft push-none rule')
    for post in postings:
        try:
            link=post.find('a',class_='media__img media__img--thumb').get('href')
            link
            full_link='https://www.carpages.ca'+link
            full_link
            name=post.find('h4',class_='hN').text
            color=post.find_all('div',class_='grey l-column l-column--small-6 l-column--medium-4')[1].text.strip()
            price=post.find('strong',class_='delta').text.strip()
           
            df=df.append({'Link':full_link,'name':name,'color':color, 'price':price},ignore_index=True)
        except:
            pass
    
    
    next_page=soup.find('a',{'title':'Next Page'}).get('href')
    next_page
    next_fullPage='https://www.carpages.ca'+next_page
    next_fullPage
    url=next_fullPage
    page=requests.get(url)
    
    soup=BeautifulSoup(page.text,'lxml')
    a=a+1

df.to_csv('/home/ashwini/1-15carpage.csv')    
