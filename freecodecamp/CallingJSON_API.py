import urllib.request, urllib.parse, urllib.error
import ssl
import json

#gia na me hackaroun
verify = ssl.create_default_context()
verify.check_hostname = False
verify.verify_mode = ssl.CERT_NONE


search = 'http://py4e-data.dr-chuck.net/json?'
param = dict()
api_key = 42

placeID = ''
while True:
    address = input('Enter location:')
    if(len(address) < 1):
        break
    param['address'] = address
    param['key'] = api_key
    url = search + urllib.parse.urlencode(param)
    print('Retrieving data from:',url)
    site = urllib.request.urlopen(url,context=verify)
    data = site.read().decode()
    print('Retrieved',len(data),'characters')
    try:
        info = json.loads(data)
    except:
        print('====== Failed to retrieve ======')
        break
    print(info)
    placeID = info['results'][0]['place_id']
    
print('\nPlace ID:',placeID,'\n')

quit()

    