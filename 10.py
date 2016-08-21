#2016-8-19 15:45:12
#level 10: http://www.pythonchallenge.com/pc/return/bull.html

#username:huge password:file

encode = 'utf-8'


from PIL import Image, ImageDraw

def a(n):#output the top n elements of the sequence a("look and say sequence")
	p = "1"
	seq = [1]
	while (n > 1):
		q = ''
		idx = 0 # Index
		l = len(p) # Length
		while idx < l:
			start = idx
			idx = idx + 1
			while idx < l and p[idx] == p[start]:
				idx = idx + 1
			q = q + str(idx-start) + p[start]
		n, p = n - 1, q
		seq.append(int(p))
	return seq
	
print a(10)#output the top 10 elements of the sequence
print len(str(a(31)[30]))#the parameter 'n' in the function represent the length of the sequence

#1. the image showed in the webpage and array named 'coords' in the source code doesn't give any help to solution
#2. the answer is to use "sequence.txt" and the tip "a[30]="
#3. access the link http://www.pythonchallenge.com/pc/return/sequence.txt : a = [1, 11, 21, 1211, 111221, 
#4. this sequence is "look and say sequence", 
#	refer to link : https://oeis.org/search?q=1%2C+11%2C+21%2C+1211%2C+111221&language=english&go=Search
#					https://oeis.org/A005341/list
#5. a[30] represents the 31st element in the sequence, the length is 5808

#the next level website: http://www.pythonchallenge.com/pc/return/5808.html
