def baliktad(temp):
    textfile = sys.argv[1] #import sys

    f = open(textfile, "r")
    print(f.read())
    f.seek(0)
    f1 = open("reverse.txt", "w+")

    temp = f.readlines()
    temp1 = temp[::-1]
    f1.seek(0)
    data = f1.writelines(temp1)
    f1.seek(0)
    print(f1.read())
    f1.close()

def balot():
    sys.argv[0]

    num = int(sys.argv[2])
    f = open(sys.argv[1], "r")

    value = f.read()
    wraptext = textwrap.TextWrapper(width=num, replace_whitespace = False)
    wordwrap = wraptext.wrap(text=value)

    for x in wordwrap:
        print(x)

    f.close()

def igitna():
    textfile = sys.argv[1]
    f = open (textfile, 'r')
    value = f.readlines()
    for x in value:
        print(x.center(110))

def sea():
    seashell = "\nShe sells seashells on the seashore;\n", "The shells that she sells are seashells I'm sure.\n", "So if she sells seashells on the seashore,\n",  "I'm sure that the shells are seashore shells.\n"
    f = open("she.txt", "w+")
    f.writelines(seashell)
    f.seek(0)
    temp = f.readlines()
    f.seek(0)
    print(f.read())
    f.seek(0)
    f.close()

def main():
    sea()

main()