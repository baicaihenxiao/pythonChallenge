#2016-8-8 22:13:58
#level 8: http://www.pythonchallenge.com/pc/def/integrity.html



import bz2

print bz2.decompress('BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')
print bz2.decompress('BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08')

# the html source code shows 'un' and 'pw' followed by two strings, which represent encoding of username and password.
# I really don't know the encoding scheme, so google to find answer.
# So just use bz2 module to decompress...  and you find username and password
# click the bee in the picture and redirect to another page to enter the credential.
# username:huge
# password:file

#the next level website: http://www.pythonchallenge.com/pc/return/good.html
