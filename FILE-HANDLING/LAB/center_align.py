import sys

textfile = sys.argv[1]

f = open (textfile, 'r')

value = f.readlines()

for x in value:
    print(x.center(110))