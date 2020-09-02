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
myurl= 'https://ktu.edu.in'
ucli= ureq(myurl)
page_html = ucli.read()
ucli.close()

page_soup = soup(page_html,"html.parser")
containers = page_soup.findAll("div",{"class":"latest-news"})

for container in containers:
    title_container = container.findAll("li",{"style":""})
    title_time = title_container[0].label.text[0:10] + " " + title_container[0].label.text[24:28]
    title_content = title_container[0].a.text
    print(title_time + " | " + " Announcement :" + title_content)
"""
filname='clgscrap.csv'
f= open(filename,"w+")
headers= "Date,Notification\n"
f.write(headers)

f.close()
"""

