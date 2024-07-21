from bs4 import BeautifulSoup
from urllib.request import urlopen
import ssl
import csv
csv_file = open("wiki_links.csv", "w")
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE
uh = urlopen("https://www.google.com/search?client=safari&rls=en&q=google+search+python&ie=UTF-8&oe=UTF-8",context=context)
data = uh.read().decode()
data = BeautifulSoup(data, "html.parser")
# print(data.title)
links = data.find_all("a")
for link in links:
    link = link.get("href").encode()
    link = str(link)
    csv_file.write(link + "\n")
    