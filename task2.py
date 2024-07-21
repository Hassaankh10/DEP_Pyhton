from bs4 import BeautifulSoup
from urllib.request import urlopen
import ssl
import csv
csv_file = open("links.csv", "w")
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE
url = input("Enter the url: ")
uh = urlopen(url ,context=context)
data = uh.read().decode()
data = BeautifulSoup(data, "html.parser")
# print(data.title)
csv_file.write("Links\n")
links = data.find_all("a")
for link in links:
    link = link.get("href").encode()
    # linkpos = link.find(b"/url?q=")
    link = str(link)
    link = link.replace("b'", "")
    if link.startswith("https://"):
        csv_file.write(link + "\n")
        continue
    