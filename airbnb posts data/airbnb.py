import requests
from bs4 import BeautifulSoup
import pandas as pd

url='https://www.airbnb.co.in/s/Honolulu--HI--United-States/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&query=Honolulu%2C%20HI&place_id=ChIJTUbDjDsYAHwRbJen81_1KEs&date_picker_type=calendar&checkin=2022-07-31&checkout=2022-08-01&source=structured_search_input_header&search_type=autocomplete_click'

page=requests.get(url)
page

soup=BeautifulSoup(page.text,'lxml')
soup
df=pd.DataFrame({'Link':[''],'Title':[''],'Details':[''], 'price':[''],'Rating':['']})
while True:
    postings=soup.find_all('div',class_='c4mnd7m dir dir-ltr')    
    for post in postings:
        try:
            link = post.find('a',class_='ln2bl2p dir dir-ltr').get('href')
            link_full='https://www.airbnb.co.in/'+link
            title= post.find('span',class_='t19nnqvo dir dir-ltr').text
            price=post.find('span',class_='_tyxjp1').text
            rating=post.find('span',class_='ru0q88m dir dir-ltr').text
            details=post.find('div',class_='f15liw5s s1cjsi4j dir dir-ltr').text
            df=df.append({'Link':link_full,'Title':title,'Details':details, 'price':price,'Rating':rating},ignore_index=True)
        except:
            pass
    
    
    next_page = soup.find('a', {'aria-label':'Next'}).get('href')
    next_page
    
    next_page_full='https://www.airbnb.co.in/'+next_page
    next_page_full
    
    url=next_page_full
    page=requests.get(url)
    
    soup=BeautifulSoup(page.text,'lxml')


df.to_csv('/home/ashwini/airbnb.csv')
