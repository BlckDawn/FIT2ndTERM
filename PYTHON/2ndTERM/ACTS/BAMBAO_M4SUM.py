Fruits = {"Apple": 15, "Orange": 16, "Mango": 25, "Banana": 7, "Strawberry": 35, "Ponkan": 6}

for fruit, price in Fruits.items():
    if fruit == "Ponkan":
        print(fruit, ":", price)
    else:
        print(fruit, ":", price, end=", ", flush=True)
    
print("Total Number of Items:", len(Fruits))

print("Items: ",end="",flush=True)
for fruit in Fruits:
    if fruit == "Ponkan":
        print(fruit, end="")
        print()
    else:
        print(fruit, end=", ", flush=True)

print("Sorted Items: ",end="",flush=True)
for fruit in sorted(Fruits.keys()):
    if fruit == "Strawberry":
        print(fruit, end="")
        print()
    else:
        print(fruit, end=", ", flush=True)
    
search = str(input("Searched Item: "))

if search in Fruits:
    print("Item:", search, "with the price of", Fruits[search])
else:
    print("Fail")

total = (Fruits["Banana"] * 3) + (Fruits["Mango"] * 4) + (Fruits["Strawberry"]*1)
print("Items Selection:")
print("Banana(3):", Fruits["Banana"] * 3)
print("Mango(4):", Fruits["Mango"] * 4)
print("Strawberry(1):", Fruits["Strawberry"] * 1)
print("Total Price:", total, "(8 items)")

print(*Fruits )