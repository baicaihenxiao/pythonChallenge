#2016-7-20 13:20:12
#http://www.pythonchallenge.com/pc/def/map.html


from __future__ import print_function
text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
for c in text:
	if c.isalpha():
		print(chr((ord(c) - ord('a') + 2)%26 + ord('a')), end='')
	else:
		print(c, end='')
		
url =  "http://www.pythonchallenge.com/pc/def/map.html"



for c in url:
	if c.isalpha():
		print(chr((ord(c) - ord('a') + 2)%26 + ord('a')), end='')
	else:
		print(c, end='')
		
#the result is to replace map with ocr in the URL.
#the next level website: http://www.pythonchallenge.com/pc/def/orc.html
