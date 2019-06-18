import sys

inp = sys.argv[1]
base = int(sys.argv[2])

print "Integer Value: ",str(int(inp, base))
print "Hexadecimal Value: ",str(hex(int(inp, base)))
print "Octal Value: ",str(oct(int(inp, base)))
print "Binary Value: ",str(bin(int(inp, base)))
print "ASCII Value: ",str(chr(int(inp, base)))