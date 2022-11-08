from bs4 import BeautifulSoup
import requests

headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0"
    }
dict = ""
query = input('What are you searching for?: ')
url = "https://www.google.com/search"
params = {"q": input()}
page = requests.get()
soup = BeautifulSoup(page.text, headers=headers)
h3 = soup.find_all("h3", class_="r")
for elem in h3:
    elem = elem.contents[0]
    elem = elem["href"]
    link = ("https://www.google.com" + elem)
page = requests.get(link)
soup = BeautifulSoup(page.text)
text = soup.find(id="mw-content-text")
p = text.find("p")
while p != None:
    dict += p.get_text() + "\n"
    p = p.find_next("p")
dict = dict.split()
