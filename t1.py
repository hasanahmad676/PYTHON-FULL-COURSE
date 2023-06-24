# import the necessary libraries
from bs4 import BeautifulSoup
import requests
url = "https://www.pararius.com/apartments/amsterdam"

#step-1 : get the html
page = requests.get(url)
htmlcontent=page.content
#print(htmlcontent).....commmented  the print function.

#step-2: parse the html
soup = BeautifulSoup(htmlcontent,'html.parser')
#print(soup).....commented the soup print function
lists = soup.find_all('section', class_='listing-search-item')
#print(lists)

for list in lists:
    title = list.find('a',class_='listing-search-item__link--title').text
    price = list.find('div',class_='listing-search-item__price').text
    area = list.find('li',class_='illustrated-features__item--surface-area').text
    rooms = list.find('li',class_='illustrated-features__item--number-of-rooms').text
    interiror = list.find('li',class_='illustrated-features__item--interior').text
    info = [title,price,area,rooms,interior]
    print(info)
