#This python script scraps data from wikipedia
#and prints the extracted text on the screen 

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


### Find siblings:
# s = soup.p.next_sibling.next_sibling

### Find children/content:
# content= firstPara.contents
# text = ""
# for line in content:
# 	print(line.find_all("a")[0].get('href'))
# 	if len(line)>1 or (len(line.get('class'))==1 and line.get('class')!='reference'):
# 		text = text+line.string
