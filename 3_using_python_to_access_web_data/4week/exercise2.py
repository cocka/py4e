# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
counttimes = input('Enter count: ')
position = input('Enter position: ')
count_int = int(counttimes)

for xurumelas in range(count_int): 
    print('Retrieving:', url)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all of the anchor tags
    tags = soup('a')
    pos = 0
    for tag in tags:
        pos = pos +1
        if pos > int(position):
            break
        url = tag.get('href', None)

print('Retrieving:', url)
