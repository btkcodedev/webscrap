import requests                               #Helps to send HTTP request(connections)
from urllib.request import urlopen as ureq    #Helps to get connected with Specified URL's
from bs4 import BeautifulSoup as soup         #Helps to extract webpages using HTML Parser function
import smtplib,ssl                            #Helps to send out mails using SMTP
import io                                     #Helps tp encode the characters into specified format
import csv                                    #Helps to read csv file
from email.mime.text import MIMEText          #Email Decoration & Partitioning
from email.mime.multipart import MIMEMultipart

myurl= 'http://gecskp.ac.in' #provide the required URL
ucli= ureq(myurl)            #Connect to webpage using URLLIB
page_html = ucli.read()      #reads the webpage and transfers to a variable
ucli.close()                 #We should close the connection as the webpage can contain timeout


#Get the html part using the html.parser function  of beautifulsoup library
page_soup = soup(page_html,"html.parser")
#Specify the tag where brief of needed data can be extracted
containers = page_soup.findAll("a",{"style":"font-weight: 600; font-style: normal;"},{"href"})
#opens a file to save the results
filename='clgscrap.csv'

try:
  with open(filename,"r+",encoding="utf-16") as r:
    checker=[]
    reader = csv.reader(r, delimiter="\n")
    for i, line in enumerate(reader):
        checker=checker+[line]                    #Check for the same message or different
  #print(str(checker[2]))
except Exception as e:
  err=e

with open(filename,"w+",encoding="utf-16") as f:  # as the file contains malayalam, specifying an external encoding is needed
    headers= "NEWS,LINK\n"
    f.write(headers)                              #specifying headers
    lis=[]
    mailbody=[]
    maillink=[]
    q=0 
    i=0
    for container in containers:
        link = containers[q].get('href')         #Get the exact location inside the brief location
        news = containers[q].text                #Get the text inside the tags using .text function
        orglink = ("http://gecskp.ac.in/"+link)  #Get the link
        if(q==1):                                #For the checking of new update
            checkernew=news+" "+orglink          
        final="News: " + news+ "\n"
        linker="Link: " + orglink + "\n"
        mailbody=mailbody+[final]
        maillink=maillink+[orglink]
        lis=lis+[final+linker] 
        f.write(news.replace(",","|")+" "+orglink.replace(",","|") + "\n")  #Writing in the file.while Writing,the comma represents the next column
        q=q+1
        i=i+1
f.close()                                          #finally close the file to open it with interface
print("Latest\n",lis[1])
print("Previous\n",lis[2])
print("All\n",' '.join(lis))

if(str(checker[2])!=str("['"+checkernew+"']")):    #Check new update with old update
    #username : testscrapmailer@gmail.com pass: testscraper
    smtp_server = "smtp.gmail.com"                  #using python smtp gmail client
    port = 587                                      #For starttls
    sender="testscrapmailer@gmail.com"              #sender
    appkey=input("Enter Password")                  #password
    receiver="tagona3999@alicdh.com"               #receiver
    context = ssl.create_default_context()

    message = MIMEMultipart("alternative")
    message["Subject"] = "GEC SCRAPER"
    message["From"] = sender
    message["To"] = receiver

    # Create the plain-text and HTML version of message
    text = """\
    GEC SCRAPER: 
    Dear Student,
    The website has been updated by a new notification as follows
    """ +str(mailbody[1])+str(maillink[1])+""".
    Previous Mail: """ +str(mailbody[2])+str(maillink[1])+"""
    """

    html = """\
    <html>
      <body>
        <h4 style="text-align:center;">GEC SCRAPER</h4>
        <p>
          <h5><i>Dear Student,</i></h5>
          <br>The website has been updated by a new notification as follows,<br>
          """ +str(mailbody[1])+ """ <a href="""+str(maillink[1])+""">Details</a>
          <br> 
          <br>Previous Mail:<br>
          """ +str(mailbody[2])+ """ <a href="""+str(maillink[1])+""">Details</a>
        </p>
        <br>
        <h4>Thank You.</h4>
        <br>
        <h6>For Unsubscribing, Click <a href="#">here</a></h6>
      </body>
    </html>
    """

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    try:
      with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as conn:
          conn.login(sender, appkey)
          conn.sendmail(
              sender, receiver, message.as_string()
          )
    except Exception as e:
      print(e)
      conn.quit()
else:
  print("No New Updates")
