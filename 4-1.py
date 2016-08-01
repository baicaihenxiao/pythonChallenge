import urllib, re

#2016-8-1 14:45:57
#another method to solve level 4, using urllib

'''

introduce urllib: https://pythonprogramming.net/urllib-tutorial-python-3/
try:
	x = urllib.urlopen('https://www.google.com/')
	saveFile = open('noheaders.txt','w')
	saveFile.write(str(x.read()))
	saveFile.close()
except Exception as e:
    print(str(e))
'''



urlstr = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s'
nothing = '63579'


while True:
	try:
		print urlstr%nothing
		data = urllib.urlopen(urlstr%nothing).read()
		print data
		nothing = re.search(r'([\d]+)', data).group(1)
		print nothing
	except Exception as e:
		print 'AAAAAAAAAAAA'
		print(str(e))
		break
		


