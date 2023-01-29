#import math

def add(x, y):
    return int(x + y)

def sub(x, y):
    return int(x - y)

def prod(x, y):
    return int(x * y)

def quo(x, y):
    return int(x / 5)

def ACT1():
    x = int(input("First Number: "))
    y = int(input ("Second Number: "))

    print("Modulo Mode")
    print("The sum of %d and %d is %d." % (x, y, add(x, y)))
    print("The difference of %d and %d is %d." % (x, y, sub(x, y)))
    print("The product of %d and %d is %d." % (x, y, prod(x, y)))
    print("The quotient of %d and %d is %d." % (x, y, quo(x, y)))

    print("\nPrint(f'')")
    print(f"The sum of {x} and {y} is {add(x,y)}." )
    print(f"The difference of {x} and {y} is {sub(x,y)}." )
    print(f"The product of {x} and {y} is {prod(x,y)}." )
    print(f"The quotient of {x} and {y} is {quo(x,y)}." )

    print("\nFormat Method")
    print("The sum of {x} and {y} is {add}.".format(x = x, y = y, add = add(x,y)))
    print("The difference of {x} and {y} is {add}.".format(x = x, y = y, add = sub(x,y)))
    print("The product of {x} and {y} is {add}.".format(x = x, y = y, add = prod(x,y)))
    print("The quotient of {x} and {y} is {add}.".format(x = x, y = y, add = quo(x,y)))


def heron(s, a, b, c):
    if s == 0:
        s = (a + b + c) / 2 #if no semi perimiter
        x = s * ((s - a) * (s - b) * (s - c))
    else:
        x = s * ((s - a) * (s - b) * (s - c))
    return x ** (1/2)

def ACT2():
    print("\nHeron's Formula")
    s = float(input("Semi-perimeter: "))
    a = float(input("length of side a: "))
    b = float(input("length of side b: "))
    c = float(input("length of side c: "))

    
    area = heron(s, a, b, c)

    print(f"The area of the triangle is {area :.2f}")

def slope(x1, x2, y1, y2):
    m = (y2 - y1)
    m1 = (x2 - x1)
   
    if m1 < 0:
        m1 = abs(m1)
        m2 = m2 = f"The slope is - {m} / {m1}"
    else:
        m2 = f"The slope is {m} / {m1}"
    return m2
    
def ACT3():
    print("\nCompute the slope of the line using two points")
    x1, y1 = [float(a) for a in input("1st Point(x1, y1): ").split()]
    x2, y2 = [float(b) for b in input("2nd Point(x2, y2): ").split()]
    
    s = slope(x1, x2, y1, y2)
    print(f"\nThe slope is {s}") #
    print(u"The formula for slope is \x1B[4m x\N{SUBSCRIPT ONE} - y\N{SUBSCRIPT ONE}\x1B[0m")
    print("\t\t\t  x\N{SUBSCRIPT TWO} - y\N{SUBSCRIPT TWO}")



def main():
    #ACT1()
    #ACT2()
    ACT3()

main()
