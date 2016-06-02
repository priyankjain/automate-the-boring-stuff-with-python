#! python3
# xkcdDownloader.py - A Python scraper to download all comic images
# from http://xkcd.com/
# Author: Priyank Jain
#####################################################################
import re, requests, bs4, traceback, os
comicNumber = None
prevComicUrl = None
comicUrl = 'http://xkcd.com'
comicNumberRegex = re.compile(r'http://xkcd.com/([0-9]*)')
comicImageNameRegex = re.compile(r'http://imgs.xkcd.com/comics/([\w.]*)')
if not os.path.exists('data'):
	os.mkdir('data')
os.chdir('data')
while comicNumber != 0:
	try:
		currentComicPage = requests.get(comicUrl)
		currentComicPage.raise_for_status()
		comicSoup = bs4.BeautifulSoup(currentComicPage.text)
		navLinks = comicSoup.select('#middleContainer ul.comicNav li a')
		if len(navLinks)>1:
			prevComicUrl = 'http://xkcd.com{0}'.format(navLinks[1].get('href'))
			comicUrl = prevComicUrl
		else:
			print("Could not retrieve previous comic on page {0}".format(comicUrl))
		middleContainer = comicSoup.select('#middleContainer')
		if middleContainer is not None:
			middleContainerText = middleContainer[0].getText()
			numberMatch = comicNumberRegex.search(middleContainerText)
			comicNumber = None
			comicImageName = None
			if numberMatch is not None:
				comicNumber = numberMatch.group(1)
			imageNameMatch = comicImageNameRegex.search(middleContainerText)
			if imageNameMatch is not None:
				comicImageName = imageNameMatch.group(1)
			if comicNumber is None or comicImageName is None:
				print("Could not save comic image for URL: {0}".format(comicUrl))
			else:
				imageRes = requests.get(r'http://imgs.xkcd.com/comics/{0}'.format(comicImageName))
				imageFile = open('{0}_{1}'.format(comicNumber, comicImageName),'wb')
				imageRes.raise_for_status()
				for chunk in imageRes.iter_content(1000):
					imageFile.write(chunk)
				imageFile.close()
		if comicUrl != prevComicUrl:
			break
	except:
		print("Exception occurred", traceback.format_exc())
