import urllib.request, urllib.parse, urllib.error
import ssl
import xml.etree.ElementTree as et

api_key = False
if api_key is False:
    api_key = 42
    servicuerl = 'http://py4e-data.dr-chuck.net/xml?'
else:
    servicuerl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

#gia na me hackaroun
verify = ssl.create_default_context()
verify.check_hostname = False
verify.verify_mode = ssl.CERT_NONE

summ = 0
while True:
    address = input('Enter Url - ')
    if len(address) < 1:
        break
    print('Retriving',address)
    site = urllib.request.urlopen(address, context=verify)
    data = site.read()
    print('Retrieve',len(data),'characters')
    trans = et.fromstring(data)
    print(trans)
    counts = trans.findall('.//count')
    for num in counts:
        summ += int(num.text)
print(summ)
    
quit()