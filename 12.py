#2016-8-21 14:07:00
#level 11: http://www.pythonchallenge.com/pc/return/5808.html

#username:huge password:file

encode = 'utf-8'


from PIL import Image, ImageDraw
import urllib
import re

def get_challenge(s):
	return urllib.urlopen('http://www.pythonchallenge.com/pc/' + s)


#Image.open(get_challenge('return/evil1.jpg')).show()
# print '1\n1'
# gfx = get_challenge('return/evil2.gfx').read();

'''print gfx[:25]
print re.sub(r'[^ -~]','?',gfx)
gfx[0:60:5]'''

'''
types = ['jpg','png','gif','png','jpg']
for i in range(5): open('evil2%d.%s' % (i, types[i]),'wb').write(gfx[i::5])
'''

h = open('evil2.gfx', "rb")
data = h.read()
h.close()

new_data = [[], [], [], [], []]
n = 0

for byte in range(len(data) - 1):
    new_data[n].append(data[byte])
    n = 0 if n == 4 else n + 1

for n, elt in enumerate(new_data):
    h = open(str(n + 1)+'.jpg', "wb")
    h.write("".join(elt))
    h.close()


#1. the title of the page is 'odd even'
#2. print the pixel, you can find the pattern;
#3. remove the odd pixels and show the new photo;
#4. there's a dim string 'evil' on the up-right of the photo

#the next level website: http://www.pythonchallenge.com/pc/return/evil.html
