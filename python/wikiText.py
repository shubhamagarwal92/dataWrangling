@author = 'Shubham'
from bs4 import BeautifulSoup
import urllib2

def wikiWrangler(wikiPage):
	wiki = wikiPage
	header = {'User-Agent': 'Mozilla/5.0'} #Needed to prevent 403 error on Wikipedia
	req = urllib2.Request(wiki,headers=header)
	page = urllib2.urlopen(req)
	soup = BeautifulSoup(page)
	return soup

wiki = "http://en.wikipedia.org/wiki/Demographics_of_India"
soup = wikiWrangler(wiki)
paras = soup.find_all("p")
firstPara = paras[0].get_text()
print(firstPara)
