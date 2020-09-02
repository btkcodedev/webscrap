from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup
#selecting the url and copying to a variable
myurl='https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38'
#opening the connection
ucli = ureq(myurl)
page_html = ucli.read()
ucli.close() #closing the connection

#Take the webpage file as html and store it to page_soup
page_soup = soup(page_html,"html.parser")
containers = page_soup.findAll("div",{"class":"item-container"})

filename= "product.csv"
f = open(filename,"w+")
headers ="brand, product_name, ship\n "
f.write(headers)


#looping for full data
for container in containers:
    brand = container.div.div.a.img["title"]

    title_container = container.findAll("a",{"class":"item-title"})
    product_name = title_container[0].text

    shipping_container = container.findAll("li",{"class":"price-ship"})
    ship = shipping_container[0].text.strip()

    print(brand + ": Brand")
    print(product_name + ": Product")
    print(ship + ": Shipping charge")
    print("\n")

    f.write(brand + ": Brand"+"," + product_name.replace(",","|") + "," +": Product" + ship + ": Shipping charge")
    f.write("\n")
f.close()