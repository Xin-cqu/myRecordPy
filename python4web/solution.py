'''
@author: Xin Wen
'''
import urllib.request
from bs4 import BeautifulSoup

i=0
names=[]
url = input('Enter - ')
print('Enter count:')
count=int(input())
print('Enter position:')
positon=int(input())
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for i in range(0,count):
    htmlString=tags[positon-1].get('href',None)
    #print(htmlString)
    html=urllib.request.urlopen(htmlString).read()
    names.append(tags[positon-1].contents[0])
    soup = BeautifulSoup(html,'html.parser')
    tags=soup('a')
print(names)