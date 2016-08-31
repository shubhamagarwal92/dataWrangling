#This python script scraps table from wikipedia
#and writes the table using pandas 

from bs4 import BeautifulSoup
import urllib2
import pandas as pd
def wikiWrangler(wikiPage):
	wiki = wikiPage
	header = {'User-Agent': 'Mozilla/5.0'} #Needed to prevent 403 error on Wikipedia
	req = urllib2.Request(wiki,headers=header)
	page = urllib2.urlopen(req)
	soup = BeautifulSoup(page)
	return soup

wiki = "http://en.wikipedia.org/wiki/Demographics_of_India"
soup = wikiWrangler(wiki)
table = soup.find("table", { "class" : "wikitable collapsible sortable" })
rows = table.find_all('tr')
print(len(rows))

districts2001 = []
districts2004 = []
state = []
rank = []
districtsGeoChange = []
for row in rows:
	cells = row.findAll("td")
	if len(cells) == 5:
		rank.append(cells[0].find(text=True))
		#rank.append(cells[0].string.strip()
		state.append(cells[1].find(text=True))
		districts2001.append(cells[2].find(text=True))
		districts2004.append(cells[3].find(text=True))
		districtsGeoChange.append(cells[4].find(text=True))

		# To fill '-' as 0 or NA: 
		# if cells[4].string.isdigit() == True:
		# 	districtsGeoChange.append(cells[4].find(text=True))
		# else:
		# 	districtsGeoChange.append(0)

columns={'Rank':rank,'State':state,'Districts2001':districts2001,'Districts2004':districts2004,'districtsGeoChange':districtsGeoChange}
# Create a dataframe from the columns variable
df = pd.DataFrame(columns)
fileName = 'indianDemographics.csv'
df.to_csv(fileName)