'''
@author: Xin Wen
'''
import urllib.request 
import urllib
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET


address = input('Enter location: ')

sumup=0
url =  address
print ('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print ('Retrieved',len(data),'characters')
tree = ET.fromstring(data)
results=tree.findall('.//count')
print(len(results))
for result in results:
    sumup+=int(result.text)
print(sumup)

'''
    results = tree.findall('result')
    lat = results[0].find('geometry').find('location').find('lat').text
    lng = results[0].find('geometry').find('location').find('lng').text
    location = results[0].find('formatted_address').text

    print ('lat',lat,'lng',lng)
    print (location)
'''