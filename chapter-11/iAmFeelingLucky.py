#! python3
# iAmFeelingLucky.py - A Python script to automatically search
# keywords in google and open the top 5 results in new tabs
# Author: Priyank Jain
#####################################################################
import webbrowser, bs4, sys, requests
if len(sys.argv) < 2:
	print("Usage: python3 iAmFeelingLucky.py <keyword-list>")
	sys.exit(-1)
else:
	searchTerm = ' '.join(sys.argv[1:])
	googleSearch = requests.get('https://www.google.com/search?q={0}'.format(searchTerm))
	googleSearch.raise_for_status()
	resultsSoup = bs4.BeautifulSoup(googleSearch.text)
	linksElem = resultsSoup.select('.r a')
	numOfTabs = min(5, len(linksElem))
	for i in range(numOfTabs):
		webbrowser.open('https://www.google.com{0}'.format(linksElem[i].get('href')))
