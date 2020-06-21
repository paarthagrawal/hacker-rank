import requests
from bs4 import BeautifulSoup
conn=requests.get("https://www.google.co.in/")
#print(conn.headers)
soup=BeautifulSoup(conn.text,'lxml')
links=soup.findAll("a")
#print(links)
for link in links:
    if 'h1' in link.text:
        print(link)
