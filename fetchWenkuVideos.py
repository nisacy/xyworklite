#!/usr/bin/python
import sys
import urllib
import urllib2
from bs4 import BeautifulSoup

def fetchUrl():
	url = sys.argv[1]
	response = urllib2.urlopen(url)

	html_doc = response.read()

	soup = BeautifulSoup(html_doc,"html.parser",from_encoding="utf-8")
	div = soup.select('div[id="video-info"]')
	
	videourl = div[0]['video-address']
	videoname = videourl.split('/')[-1]
	urllib.urlretrieve(videourl, videoname)
	print ('download ' + videoname + ' success')

fetchUrl()