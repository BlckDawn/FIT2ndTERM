n = "*"
row = 5

for x in range(5):
    print(n*5)
print()

for x in range(1, row+1):
    for y in range(1, row+1):
        if x == 1 or x == row or y == 1 or y == row:
            print(n, end = "")
        else:
            print(" ", end = "")
    print()

print()

for x in range(5):
    print(" " * x, n * 5)

print()

for x in range(row):
    for y in range(x):
        print(" ", end="")
    for a in range(row):
        if a == 0 or x == 0 or a == (row - 1) or x == (row - 1):
            print(n, end = "")
        else:
            print(" " , end = "")
    print()

print()

for x in range(6):
    print(n * x)

print()
for x in range(1, row + 1):
    for y in range(1, row + 1):
        if y == 1 or x == row or y == x:
           print(n , end = "" )
        else:
           print(" ", end = "")
    print()