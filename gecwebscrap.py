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
containers = page_soup.findAll("marquee")
print(containers)

"""
filname='clgscrap.csv'
f= open(filename,"w+")
headers= "Date,Notification\n"
f.write(headers)

f.close()
"""

