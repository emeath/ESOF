#! /usr/bin/python3
# Project "I'm Feeling Lucky" Google Search
# lucky.py - Abrir varias tabs do Google

import requests, sys, webbrowser, bs4, time

print('Googling...') 	# display text while downloading the Google page
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text)

# Open a browser tab for each result.
linkElems = soup.select('.r a')

numOpen = min(5, len(linkElems))

for i in range(numOpen):
	time.sleep(1)
	webbrowser.open_new_tab('http://google.com' + linkElems[i].get('href'))
