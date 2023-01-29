import sys
import textwrap

sys.argv[0]

num = int(sys.argv[2])
f = open(sys.argv[1], "r")

value = f.read()
wraptext = textwrap.TextWrapper(width=num, replace_whitespace = False)
wordwrap = wraptext.wrap(text=value)

for x in wordwrap:
    print(x)

f.close()