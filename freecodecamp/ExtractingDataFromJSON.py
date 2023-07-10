import json
import ssl
import urllib.request, urllib.parse, urllib.error

#gia na me hackaroun
verify = ssl.create_default_context()
verify.check_hostname = False
verify.verify_mode = ssl.CERT_NONE

summ = 0
while True:
    address = input('Enter url - ')
    if (len(address)) < 1:
        break
    print('Hacking the url - ',address)
    site = urllib.request.urlopen(address, context=verify)
    data = site.read().decode()
    print('Retrieving',len(data),'characters')
    info = json.loads(data)
    print('User count:',len(info))
    print(info)
    counts = [comment['count'] for comment in info['comments']]
    print(counts)
    for count in counts:
        summ += count
        
print('\nSum ======', summ)
            
            
    