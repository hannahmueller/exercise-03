con1 = "y"
while con1=="y":

    print("Enter number 1: ")
    num1 = int(input())
    print("Enter number 2: ")
    num2 = int(input())

    print("Enter operation: ") #add or multiply
    op1 = str(input())

    if op1 == "add" or op1 == "addition" : # add/addition
        print("Sum: " + str(num1+num2))
    elif op1 == "multi" or op1 == "multiplication":  # multi/multiplication
        print("Product: " + str(num1*num2))


    print("Continue? [y/n]: ") #start over
    con1 = str(input())  #y/n
    if con1 == "y":
        print()