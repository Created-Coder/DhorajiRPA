
################ BEAUTIFULSOUP4 ###############################

from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen('https://eurasiaonline.ie/food-cupboard/')
html = html.read()

bs = BeautifulSoup(html, 'html.parser')

# Find All span tags
span = bs.find_all('span')

for i in price:
    print(i.get_text())

# Find All span with class or id

price = bs.find_all('span', {'class' : 'price'})
for i in price:
    print(i.text)

# Find Elements with Attributes like class or id

price = bs.find_all(class_ = "price")
for i in price:
    print(i.text)

# Find Different tags elements

all = bs.find_all(['h1', 'h2', 'h3', 'h4'])
for i in all:
    print(i.text)

# Find Multiple classes elements

classes_elements = bs.find_all({'class':{'', ''}})
for i in classes_elements:
    print(i.text)


# .find
# .find_all
# find element by class and id
# find elements with multiple tag name
# find elements with attributes
# find elements with multiple classes name
#
# .text
# .get_text()
