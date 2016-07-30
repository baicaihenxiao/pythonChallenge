#2016-7-30 15:17:44
#level 4: http://www.pythonchallenge.com/pc/def/linkedlist.php

import re
from lxml import html
import requests

'''
the tutorial found in : http://docs.python-guide.org/en/latest/scenarios/scrape/

page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
tree = html.fromstring(page.content)


#This will create a list of buyers:
buyers = tree.xpath('//div[@title="buyer-name"]/text()')
#This will create a list of prices
prices = tree.xpath('//span[@class="item-price"]/text()')


print 'Buyers: ', buyers
print 'Prices: ', prices
'''

tmpURL = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345'
for i in range(0, 500): #the scope of for loop is defined by indent
	print tmpURL
	page1 = requests.get(tmpURL) #get webpage
	strPage1 = page1.content #get content
	print strPage1
	res = re.search(r'[\d]+', strPage1) #regex expression to find number
	print res.group(0) #number which has been found
	linkNum = re.compile("\d+")
	tmpURL = re.sub(linkNum, res.group(0), tmpURL) #replace string: update new number in URL
	#print tmpURL


'''
Note that with this method I met several interruptions in the for loop.
For example, one misleading page which give you warning, so you have to replace the tmpURL manually for about two times.
The last two number is 52899,66831
Then in http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=66831 you can find the content:peak.html
so replace "linkedlist.php?nothing=12345" with "peak.html".

the next level is: http://www.pythonchallenge.com/pc/def/peak.html
'''
