import sys

n = len(sys.argv)
base = int(sys.argv[n-1])
word = ""
arglist = []
newlist = []

for i in range(1,n-1):
	arglist.append(sys.argv[i])
print arglist

if base == 2:
	for x in arglist:
		curr = ""
		for i in range(0,len(x),8):
			curr = x[i] + x[i+1] + x[i+2] + x[i+3] + x[i+4] + x[i+5] + x[i+6] + x[i+7]
			newlist.append(curr)
elif base == 16:
	for x in arglist:
		curr = ""
		for i in range(0,len(x),2):
			curr = x[i] + x[i+1]
			newlist.append(curr)
elif base == 8:
	for x in arglist:
		curr = ""
		for i in range(0,len(x),3):
			curr = x[i] + x[i+1] + x[i+2]
			newlist.append(curr)
elif base == 10:
	for x in arglist:
		curr = ""
		for i in range(0,len(x),2):
			curr = x[i] + x[i+1]
			newlist.append(curr)
arglist = newlist

for x in arglist:
	word += chr(int(x,base))
print word