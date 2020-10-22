import requests     #Helps to send HTTP request(connections)
from urllib.request import urlopen as ureq #Helps to get connected with Specified URL's
from bs4 import BeautifulSoup as soup #Helps to extract webpages using HTML Parser function
import smtplib #Helps to send out mails using SMTP
import io  #Helps tp encode the characters into specified format
import csv  #Helps to read csv file
#opens up the web connection with specified URL

urlss=[] 
for i in range(1,5):  #use n+1 pages for clearing index out of range error
  laps='https://www.flipkart.com/laptops/pr?sid=6bo,b5g&otracker=categorytree&page='+str(i)
  mobs='https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&otracker=categorytree&page='+str(i)
  cams='https://www.flipkart.com/cameras/pr?sid=jek,p31&otracker=categorytree&page='+str(i)
  hpo='https://www.flipkart.com/headphones/pr?sid=fcn&otracker=categorytree&page='+str(i)
  acs='https://www.flipkart.com/air-conditioners/pr?sid=c54&otracker=categorytree&page='+str(i)
  urlss=urlss+[acs]  # Change the variable with a dropdown box when merging with its front end
print(urlss)

title=[]
amount=[]
l=[]
spec=[]
rat=[]

for i in range(1,2):  #only use n-1 pages which are proxy safe in the list
  myurl= urlss[i]
  ucli= ureq(myurl)
  page_html = ucli.read() #reads the webpage and transfers to a variable
  ucli.close()
  page_soup = soup(page_html,"html.parser")
  containers = page_soup.findAll("div",{"class":"bhgxx2 col-12-12"})
  for container in containers:
    datas=container.findAll("a",{"class":"_31qSD5"})
    link=container.findAll("div",{"class":"_1UoZlX"})
    for nextlinks in link:
      orglink=nextlinks.a.get('href')
      real="https://www.flipkart.com"+orglink
      l=l+[real]
    for data in datas:
      nextcontainers = data.findAll("div",{"class":"_1uv9Cb"})
      for cont in nextcontainers:
        realprice=cont.div.text
        print(realprice)
        amount=amount+[realprice]
      maindata=data.findAll("div",{"class":"_1-2Iqu row"})
      for headdata in maindata:
        head=headdata.findAll("div",{"class":"col col-7-12"})
        mt=head[0].div.text
        print(mt)
        title=title+[mt]
        rating=headdata.findAll("div",{"class":"niH0FQ"})
        try:
          print(rating[0].span.text)
          oo=rating[0].span.text
          rat=rat+[oo]
        except:
          print("No Rating")
          rat=rat+["No rating"]
        specs=headdata.findAll("li",{"class":"tVe95H"})
        for spec in specs:
          print(spec.text)
        print("\n")
        
if title==[]:  #for different type of page
  for i in range(1,2):  #only use n-1 pages which are proxy safe in the list
    myurl= urlss[i]
    ucli= ureq(myurl)
    page_html = ucli.read() #reads the webpage and transfers to a variable
    ucli.close()
    page_soup = soup(page_html,"html.parser")
    containers = page_soup.findAll("div",{"class":"bhgxx2 col-12-12"})
    for container in containers:
        
      datas=container.findAll("div",{"class":"_3liAhj"})

      for data in datas:
        link=container.findAll("a",{"class":"Zhf2z-"})
        for nextlinks in link:
          orglink=nextlinks.get('href')
          real="https://www.flipkart.com"+orglink
          l=l+[real]
        maindata=data.findAll("a",{"class":"_2cLu-l"})
        mt=maindata[0].text
        print(mt)

        subdata=data.findAll("div",{"class":"_1rcHFq"})
        sb=subdata[0].text
        print(sb)

        title=title+[mt]
        rating=data.findAll("div",{"class":"niH0FQ _36Fcw_"})
        try:
          print(rating[0].span.text)
        except:
          print("No Rating")
          
        nextcontainers = data.findAll("div",{"class":"_1vC4OE"})
        realprice=nextcontainers[0].text
        amount=amount+[realprice]
        print(realprice)
        print("\n")
print(l)
print(title)
print(rat)
print(amount)
print(len(amount))
     
