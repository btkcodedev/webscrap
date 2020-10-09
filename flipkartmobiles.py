import requests     #Helps to send HTTP request(connections)
from urllib.request import urlopen as ureq #Helps to get connected with Specified URL's
from bs4 import BeautifulSoup as soup #Helps to extract webpages using HTML Parser function
import smtplib #Helps to send out mails using SMTP
import io  #Helps tp encode the characters into specified format
import csv  #Helps to read csv file
#opens up the web connection with specified URL

myurl= 'https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&otracker=categorytree&page=1'
ucli= ureq(myurl)
page_html = ucli.read() #reads the webpage and transfers to a variable
ucli.close()

page_soup = soup(page_html,"html.parser")
containers = page_soup.findAll("div",{"class":"bhgxx2 col-12-12"})
title=[]
amount=[]
l=[]
for container in containers:
  datas=container.findAll("a",{"class":"_31qSD5"})
  link=container.findAll("div",{"class":"_1UoZlX"})
  for nextlinks in link:
    orglink=nextlinks.a.get('href')
    real="https://www.flipkart.com"+orglink
    print(real)
    l=l+[real]
  for data in datas:
    nextcontainers = data.findAll("div",{"class":"_1uv9Cb"})
    for cont in nextcontainers:
      print(cont.div.text)
      realprice=cont.div.text
      amount=amount+[realprice]
    maindata=data.findAll("div",{"class":"_1-2Iqu row"})
    for headdata in maindata:
      head=headdata.findAll("div",{"class":"col col-7-12"})
      print(head[0].div.text)
      mt=head[0].div.text
      title=title+[mt]
      rating=headdata.findAll("div",{"class":"niH0FQ"})
      print(rating[0].span.text)
      specs=headdata.findAll("li",{"class":"tVe95H"})
      for spec in specs:
        print(spec.text)
      print("\n")
print(l)
print(title)
print(amount)
