import requests     #Helps to send HTTP request(connections)
from urllib.request import urlopen as ureq #Helps to get connected with Specified URL's
from bs4 import BeautifulSoup as soup #Helps to extract webpages using HTML Parser function
import smtplib #Helps to send out mails using SMTP
import io  #Helps tp encode the characters into specified format
import csv  #Helps to read csv file
#opens up the web connection with specified URL


myurl= 'http://www.cee-kerala.org/'
ucli= ureq(myurl)
page_html = ucli.read() #reads the webpage and transfers to a variable
ucli.close()  #We should close the connection as the webpage can contain timeout



#Get the html part using the html.parser function  of beautifulsoup library
page_soup = soup(page_html,"html.parser")
containers = page_soup.findAll("div",{"class":"alternating_list_color blink_me"})
w=0
s=0
q=0
for container in containers:
#  print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")                   #check the loop to know which loop is needed for extraction
#  print(container)
  q=q+1
  if(q==2):
     one=container.findAll("ul")                   #Getting secondary top link and news
     head=container.findAll("p")                   #Getting top link and news
     for x in head:
       if(w==0):
         main=x.findAll("a")
       w=w+1
     print(head[0].text + " : " + "http://www.cee-kerala.org" +main[0].get('href'))
     for seperator in one:
#        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")         #check the loop to know which loop is needed for extraction
#        print(seperator)
        s=s+1
        if(s==4):
          two=seperator.findAll("li")
          three=seperator.findAll("a")
          news=two[0].span.text
          link=three[0].get('href')
          print(news + " : " + link)




#for container in containers:
#  link=container.get('href')
#  first=container.text
#  print(first)
#  print(link)
