import requests
from bs4 import BeautifulSoup

page = requests.get("http://alertablu.cob.sc.gov.br/d/")
soup = BeautifulSoup(page.content, "html.parser")

ths = soup.select("#table-meteorologico thead th")
tds = soup.select("#table-meteorologico tbody td")

titles = [th.getText().replace("\n", "").strip() for th in ths]
data = [td.getText().replace("\n", "").strip() for td in tds]

print(titles)
print(data)
