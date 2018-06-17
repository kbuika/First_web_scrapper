from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

# the url of the website we want to scrape.
my_url = 'https://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48'

# opening up connection, grabbing the page.
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parsing.
page_soup = soup(page_html, "html.parser")

 # grabs each product
containers = page_soup.findAll("div",{"class":"item-container"})

# creates a file and saves the items we have scrapped as csv
filename = "products.csv"
f = open(filename, "w")

headers = "Brand, product_name, shipping\n"

f.write(headers) 

# loop the web page for the items we need and their attributes.
for container in containers:
	brand = container.div.div.a.img["title"]  

	title_container = container.findAll("a",{"class":"item-title"})
	product_name = title_container[0].text

	shipping_container = container.findAll("li", {"class":"price-ship"})
	shipping = shipping_container[0].text.strip()

	print("brand: " + brand)
	print("product_name: " + product_name)
	print("shipping: " + shipping) 

	# concatenate the attributes of the items.
	# replace funtion is used to remove the commas in order to prevent creating many vague lists.
	f.write(brand + "," + product_name.replace(",", " ") + "," + shipping + "\n")

f.close()
# code on the console in order to view instant results.
# run the program.