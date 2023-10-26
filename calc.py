con1 = "y"
while con1=="y":

    print("Enter number 1: ")
    num1 = int(input())
    print("Enter number 2: ")
    num2 = int(input())

    print("Enter operation: ") #add or multiply
    op1 = str(input())

    # add/addition
    if op1 == "add" : 
        print("Sum: " + str(num1+num2))
    if op1 == "addition" : 
        print("Sum: " + str(num1+num2))

    # multi/multiplication
    if op1 == "multiply" : 
        print("Product: " + str(num1*num2))
    if op1 == "multiplication" : 
        print("Product: " + str(num1*num2))


    print("Continue? [y/n]: ") #start over?
    con1 = str(input())  #y/n
    if con1 == "y":
        print()