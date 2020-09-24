import requests     #Helps to send HTTP request(connections)
from urllib.request import urlopen as ureq      #Helps to get connected with Specified URL's
from bs4 import BeautifulSoup as soup     #Helps to extract webpages using HTML Parser function
import smtplib     #Helps to send out mails using SMTP
import io      #Helps tp encode the characters into specified format
import csv      #Helps to read csv file
#opens up the web connection with specified URL



myurl= 'http://gecskp.ac.in'   #provide the required URL
ucli= ureq(myurl)
page_html = ucli.read()      #reads the webpage and transfers to a variable
ucli.close()        #We should close the connection as the webpage can contain timeout



#Get the html part using the html.parser function  of beautifulsoup library
page_soup = soup(page_html,"html.parser")
#Specify the tag where brief of needed data can be extracted
containers = page_soup.findAll("a",{"style":"font-weight: 600; font-style: normal;"},{"href"})


#opens a file to save the results
filename='clgscrap.csv'
with open(filename,"w+",encoding="utf-16") as f:     # as the file contains malayalam, specifying an external encoding is needed
    headers= "NEWS,LINK\n"
    f.write(headers)      #specifying headers

    q=0
    for container in containers:
        link = containers[q].get('href')      #Get the exact location inside the brief location
        news = containers[q].text         #Get the text inside the tags using .text function
        orglink = ("http://gecskp.ac.in/"+link)  #Get the link
        if(q==1):
            storage=(news.replace(",","|")+" "+orglink.replace(",","|") + "\n")
        print("News: " + news+ " || Link: " + orglink + "\n") 
        f.write(news.replace(",","|")+" "+orglink.replace(",","|") + "\n")  #Writing in the file       #while Writing,the comma represents the next column
        q=q+1

f.close()  #finally close the file to open it with interface


"""
with open(filename,"r+",encoding="utf-16") as f:
    reader = csv.reader(f)
    row1=next(reader)
    row2=next(reader)
    row3=next(reader)
f.close()

print(row3)
print(storage)
if(row3==storage):
    print("yes")
else:
    print("No")
"""    
    
    
   
"""
page=requests.get("http://gecskp.ac.in")
page_content=html.fromstring(page.content)
items=page_content.xpath('//li/text()')
print(items)

import csv
from lxml import html
from selenium import webdriver

def render_page(url):
    driver = webdriver.Chrome()
    driver.get(url)
    r = driver.page_source
    return r
    r = render_page(myurl)
"""
