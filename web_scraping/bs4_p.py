from urllib import request
from bs4 import BeautifulSoup as bs

with open(r'.\web_scraping\test.html','r') as f:
    html_doc = f.read()
''' 
def get_soup(url):
    response = request.urlopen(url)
    return BeautifulSoup(response.read(), 'html.parser')   
'''  

# soup = get_soup('http://127.0.0.1:5500/web_scraping/test.html')
soup = bs(open(r'.\web_scraping\test.html','r'), 'html.parser')
pretty_html = soup.prettify()
with open(r'.\web_scraping\test_pretty.html','w') as f:
    f.write(pretty_html)


soup = bs(open(r'.\web_scraping\test_pretty.html','r'), 'html.parser')

print(soup.title)
print(soup.title.name)
print(soup.title.string)

