#2016-8-1 15:26:14
#level 5: http://www.pythonchallenge.com/pc/def/peak.html
from __future__ import print_function
import urllib, re, pickle


handle = urllib.urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
file = pickle.load(handle)
for iter in file:
	for tup in iter:
		print(tup[0] * tup[1], end='')
	print('')

'''
another method:	
for iter in file:
	print ''.join(elmt[0] * elmt[1] for elmt in iter)
'''
		
#the next level website: http://www.pythonchallenge.com/pc/def/channel.html
