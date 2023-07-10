from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
 
def get_online_sum(Url):
    url = Url
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup.find_all('a')
    
    count = 0
    for tag in tags:
        if (count == 17):
            third_url = tag.get('href',None)
            third_Name = tag.contents[0]
        count += 1
    return third_url,third_Name

initial_url = input('Give initial url :')
for i in range(7):
    initial_url,name = get_online_sum(initial_url)
print("Last name :",name)
    
quit()