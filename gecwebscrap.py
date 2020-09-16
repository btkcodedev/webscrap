from lxml import html
import requests
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup

"""
from selenium import webdriver

def render_page(url):
    driver = webdriver.Chrome()
    driver.get(url)
    r = driver.page_source
    return r


    r = render_page(myurl)
"""

myurl= 'http://gecskp.ac.in'
ucli= ureq(myurl)
page_html = ucli.read()
ucli.close()

page_soup = soup(page_html,"html.parser")
containers = page_soup.findAll("a",{"style":"font-weight: 600; font-style: normal;"},{"href"})

q=0
for container in containers:
    link = containers[q].get('href')
    news = containers[q].text
    orglink = ("http://gecskp.ac.in/"+link)
    print("News: " + news+ " || Link: " + orglink + "\n")
    q=q+1
"""
filname='clgscrap.csv'
f= open(filename,"w+")
headers= "Date,Notification\n"
f.write(headers)

f.close()
"""

"""
page=requests.get("http://gecskp.ac.in")
page_content=html.fromstring(page.content)
items=page_content.xpath('//li/text()')
print(items)
"""