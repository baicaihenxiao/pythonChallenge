#2016-8-2 00:49:58
#level 6: http://www.pythonchallenge.com/pc/def/channel.html

import urllib, zipfile, re


#handle = urllib.urlopen("http://www.pythonchallenge.com/pc/def/channel.zip")
#print(handle.read())

z = zipfile.ZipFile('F:\\SougouDownload\\channel.zip', 'r')
number = '90052'
filename = '%s.txt'
comment =''
print filename%number
while True:
#for i in range(6):
	try:
		content = z.open(filename%number).read()
		print content
		number = re.search(r'\d+', content).group(0)
		comment += z.getinfo(filename%number).comment
	except Exception as e:
		print 'AAAAAAAAAA'
		print str(e)
		break

print comment		

#1. replace channel.html with channel.zip to download the zip file.
#2. open the zip file, you can find a readme file to tell you start from 90052.
#3. iterate through the file list and stop at 46145.txt, where tell you to collect the comments.
#4. use z.getinfo(filename).comment to collect all files' comment attributes.
#5. output the comments in console, the picture shows 'dockey', each letter of 'dockey' comprise of each letter in 'oxygen'.
#6. access the dockey.html, which hints to look at the letters and it's in the air.
#7. so the result is oxygen.html

'''
http://code.activestate.com/recipes/52265-read-data-from-zip-files/
for filename in z.namelist():
	print filename
	bytes = z.read(filename)
	print len(bytes)
'''
	
#the next level website: http://www.pythonchallenge.com/pc/def/oxygen.html
