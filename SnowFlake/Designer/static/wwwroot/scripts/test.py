import sys

f = open('test.html', 'w')

f.write(sys.argv[1])
f.close()
