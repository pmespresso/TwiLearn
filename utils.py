from lxml import etree
import requests
import sys
import re
 
def mWebLookup(s):
	page = requests.get('http://www.merriam-webster.com/dictionary/' + s)
	text = page.text.encode('ascii', 'ignore').decode('ascii')
	a = text.find('ssens')
	b = text.find('>', a)
	c = text.find('</span>', b+3)
	#print text[b+1:c]
	text = re.sub('(<.*?>)|(&lt)|(&gt)', '', text[b+1:c])
	text = re.sub('\s+', ' ', text);
	text = text[text.find(":")+1:]
	if(text.find('{ var') != -1):
		return 'Err: ' +s + ' could not be found. Check your spelling and try again'
	else:
		return text

def wikiLookup(s):
	page = requests.get('https://en.wikipedia.org/wiki/'+s)
	text = page.text.encode('ascii', 'ignore').decode('ascii')
	a = text.find('<p>')
	b = text.find('>', a)
	c = text.find('</p>', b+3)
	#print text[b+1:c]
	text = re.sub('(<.*?>)|(&lt)|(&gt)', '', text[b+1:c])
	text = re.sub('\s+', ' ', text);
	text = text[text.find(":")+1:]
	if(text.find('{ var') != -1 or len(text) < 3):
		return 'Err: ' +s + ' could not be found. Check your spelling and try again'
	else:
		return text