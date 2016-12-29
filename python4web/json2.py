'''
@author: Xin Wen
'''
import urllib.request 
import urllib
import json

address = input('Enter location: ')

sumup=0
url =  address
print ('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode('utf-8')
print ('Retrieved',len(data),'characters')
#print(data)
info = json.loads(data)
#print(type(info))
print("Count:",len(info['comments']))

for item in info['comments']:
    sumup+=(item['count'])
    #print(item)
print('Sum:',sumup)

'''
    results = tree.findall('result')
    lat = results[0].find('geometry').find('location').find('lat').text
    lng = results[0].find('geometry').find('location').find('lng').text
    location = results[0].find('formatted_address').text

    print ('lat',lat,'lng',lng)
    print (location)
'''
