import requests
from bs4 import BeautifulSoup
from docks import add_to_db

url_folder = []


def googleparse(question):
    url_folder = []
    url = "https://www.google.com/search"

    params = {"q": question}  # add "hl":"en" to get english results
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0"
    }
    soup = BeautifulSoup(
        requests.get(url, params=params, headers=headers).content, "html.parser"
    )

    for a in soup.select("a:has(h3)"):
            # print(a['href'])
        url_folder.append(a["href"])

    for elem in url_folder:
        soup = BeautifulSoup(
            requests.get(elem, params=params, headers=headers).content, "html.parser"
        )
        text = soup.text.replace('\n', " ")
        try:
            add_to_db(question, elem, text[:100])
        except:
            pass
        return text[:1000]