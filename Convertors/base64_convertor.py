import sys
import base64

inp = sys.argv[1]
opt = sys.argv[2]

if opt=='e':
	print "Base64 Value: ",base64.b64encode(inp)
elif opt=='d':
	print "ASCII Value: ",str(inp.decode("base64"))