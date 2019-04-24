import requests
from bs4 import BeautifulSoup

url = 'https://www.bls.gov/eag/home.htm'
response = requests.get(url)
soup = BeautifulSoup(response.content,'html.parser')
listPre = soup.find_all('div', class_='secondary-nav')[-1]
#listPost = listPre.find_all('a')
links = []
for link in listPre.find_all('a'):
    links.append("https://www.bls.gov" + link.get('href'))
link = 'https://www.bls.gov/eag/eag.va.htm'
soupData = BeautifulSoup(requests.get(link),'html.parser')
dataTable = soupData.find('tbody')
rOne = dataTable.find_all('tr')[1]
laborForce = rOne.find_all('span')[-2]
print(laborForce.text)