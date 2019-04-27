#importing necessasary libraries
from datetime import date
import requests
from bs4 import BeautifulSoup
#creating a properly named file to write data to
today = date.today()
name = today.strftime("%Y%m%d") + ".txt"
file = open(str(name),"w+")
#base url 
url = 'https://www.bls.gov/eag/home.htm'
response = requests.get(url)
soup = BeautifulSoup(response.content,'html.parser')
#gather all the links from the sidebar, then modify the base url into an array of usable state urls
listPre = soup.find_all('div', class_='secondary-nav')[-1]
links = []
for link in listPre.find_all('a'):
    links.append("https://www.bls.gov" + link.get('href'))
#for every individual link we created in the array, loop through and scrape the data
for link in links:
    soupData = BeautifulSoup(requests.get(link).content,'html.parser')
    try:
        dataTable = soupData.find('tbody')
        #Scrape the state name
        stateName = soupData.find("div", { "id" : "programs-main-content" }).find('h2').text
        #Scrape the Labor Force Rate and strip the unneeded text
        rOne = dataTable.find_all('tr')[1]
        laborForce = rOne.find_all('span')[-2].text.strip("(p)")
        #Scrape the Unemployment rate and strip the unneeded text
        rTwo = dataTable.find_all('tr')[4]
        unemRate = rTwo.find_all('span')[-2].text.strip("(p)")
        #Ouput both values to the console as neatly formatted strings.
        print("Current Unemployment rate for " + stateName + " is " + unemRate)
        print("Current Civilian Labor Force rate for " + stateName + " is " + laborForce)
        file.write(stateName + "," + str(unemRate) + "," + today.strftime("%Y%m%d")
        file.write(stateName + "," + str(laborForce) + "," +today.strftime("%Y%m%d")
    except:
        print("Value not valid")
        pass
f.close()
