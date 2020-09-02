from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup
myurl= 'https://ktu.edu.in/eu/core/announcements.htm'
ucli= ureq(myurl)
page_html = ucli.read()
ucli.close()

page_soup = soup(page_html,"html.parser")
containers = page_soup.findAll("div",{"class":"c-details"})
for container in containers:
    title_container = container.findAll("label",{"class":"news-date"})
    main_title= title_container[0].text
    time =  main_title[0:10] + " " + main_title[24:28]
    print(time)

    title = container.li.text.split("\n",2)
    print(title[0].strip())

    link_header = container.li.p.a.text
    link = container.li.p.a.get("href")
    print(link_header  + " || " + link)