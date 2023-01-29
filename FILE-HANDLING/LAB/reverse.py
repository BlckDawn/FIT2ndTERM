import sys

textfile = sys.argv[1]

f = open(textfile, "r")
print(f.read())
f.seek(0)

f1 = open("she.txt", "r+")

temp = f.readlines()
temp1 = temp[::-1]
f1.seek(0)
data = f1.writelines(temp1)
f1.seek(0)
print(f1.read())
f.close()
f1.close()