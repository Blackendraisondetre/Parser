from googlesearch import search
from bs4 import BeautifulSoup
from collections import Counter
from string import punctuation
from urllib.parse import urlparse
import requests

def scrap(link, n_word, garbage):
	#Holen Sie sich die URL
	r = requests.get(link)
	soup = BeautifulSoup(r.content, features="html5lib")
	#Holen Sie sich die Wörter innerhalb von Absätzen
	text_p, text_div = (''.join(s.findAll(text=True))for s in soup.findAll('p')),(''.join(s.findAll(text=True))for s in soup.findAll('div'))
	c_p, c_div = Counter((x.rstrip(punctuation).lower() for y in text_p for x in y.split())), Counter((x.rstrip(punctuation).lower() for y in text_div for x in y.split()))
	total = c_div + c_p

	domain = urlparse(link).netloc

	if n_word in total:
		print(f"{domain} : {n_word} : {str(total.get(n_word))}")
		if domain in garbage.keys():
			garbage[domain] += total.get(n_word)
		else:
			garbage[domain] = total.get(n_word)
	else:
		print('¯\_(ツ)_/¯')

def searching(query, amount, pause):

	garbage = {}

	for j in search(query, tld="co.in", num=amount, stop=amount, pause=pause):
		scrap(j,query.lower(),garbage)
	print(garbage)

searching("Anime",5,1)
