import urllib.request
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
count=0
sumup=0

soup = BeautifulSoup(html,'html.parser')

# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    sumup+=int(tag.contents[0])
    count=count+1
print("Count:",count)
print("Sum:",sumup)
   