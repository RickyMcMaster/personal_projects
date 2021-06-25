import requests
from bs4 import BeautifulSoup
import csv

url = "http://quotes.toscrape.com/"
home = requests.get(url)

html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
# print(home.text)
soup = BeautifulSoup(home.text, "html.parser")

# print(soup.title)
# print(soup.title.string)
# print(soup.find_all('quote'))
mydivs = soup.find_all("div", {"class": "quote"})
# for x in mydivs:
#     print(x.text)
print(mydivs[0])

# print(soup.get_text())