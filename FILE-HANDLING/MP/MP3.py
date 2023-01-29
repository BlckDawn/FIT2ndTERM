
def pt1():
    filename = input("Input the filename to be opened: " )
    if ".txt" in filename:
        f = open(filename, "w+")
        for x in range(4):
            msg = "test file {x}\n".format(x = x+1)
            f.writelines(msg)
        f.seek(0)
    else:
        filename = filename + ".txt"
        f = open(filename, "w+")
        for x in range(4):
            msg = "test file {x}\n".format(x = x+1)
            f.writelines(msg )
        f.seek(0)
    print("The Lines in the file test.txt are: ", len(f.readlines()))
    f.close()

def pt2():
    filename = input("Input the filename to be opened: " )
    if ".txt" in filename:
        f = open(filename, "w+")
        for x in range(4):
            msg = "test file {x}".format(x = x+1)
            f.writelines(msg + "\n")
        f.seek(0)
    else:
        filename = filename + ".txt"
        f = open(filename, "w+")
        for x in range(4):
            msg = "test file {x}".format(x = x+1)
            f.writelines(msg + "\n")
        f.seek(0)
    print("The content of the file {} are: ".format(filename))
    print(f.read()) 
    f.close()

def pt3():
    charcount = 0
    wordcount = 0
    filename = input("Input the filename to be opened: " )
    if ".txt" in filename:
        f = open(filename, "w+")
        for x in range(4):
            msg = "test file {x}\n".format(x = x+1)
            f.writelines(msg)
        f.seek(0)
    else:
        filename = filename + ".txt"
        f = open(filename, "w+")
        for x in range(4):
            msg = "test file {x}\n".format(x = x+1)
            f.writelines(msg )
        f.seek(0)
    print("The content of the file {} are: ".format(filename))
    print(f.read()) 
    f.seek(0)
    wordcount = f.read()
    print("The number of words in the file {} are:".format(filename), len(wordcount.split()))
    f.seek(0)
    for x in f.read():
        for y in x.replace(" ", "").strip():
            charcount += 1
    print("The number of characters in the file {} are:".format(filename), charcount)
    f.close()

def pt4():
    filename = input("Input the 1st file name: " )
    filename1 = input("Input the 2nd file name: " )
    filename2= input("Input the new file name where to merge the above two files: ")
    if ".txt" in filename:
        f = open(filename, "w+")
        f1 = open(filename1, "w+")
        f2 = open(filename2, "w+")
    else:
        filename = filename + ".txt"
        filename1 = filename1 + ".txt"
        filename2 = filename2 + ".txt"
        f = open(filename, "w+")
        f1 = open(filename1, "w+")
        f2 = open(filename2, "w+")
        
    f.writelines("This is the file {}.".format(filename))
    f1.writelines("This is the file {}.".format(filename1))
    f.seek(0)
    f1.seek(0)
    temp = f.read() + "\n" + f1.read()
    f2 = open("test2.txt", "w+")
    f2.write(temp)
    f2.seek(0)
    if f2.tell() == 0:
        print("\nThe two files merged into {}".format(filename2), "\nfilesuccessfully..!!")
        print("The content of the file {} is: ".format(filename2))
        print(f2.read())
    else:
        print("Caught Lackin")

    f.close()
    f1.close()
    f2.close()
    
def main():
    #pt1()
    #pt2()
    pt3()
    #pt4()

main()