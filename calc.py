while True : 
    print("Enter number 1: ")
    num1 = int(input())
    print("Enter number 2: ")
    num2 = int(input())
    print("Choose mathematical operation 'add' or 'multiply' : ")
    choice = str(input())
    if choice == "add" : 
        print("Sum: " + str(num1+num2))
    if choice == "multiply" : 
        print("Product: " + str(num1*num2))

    print("Programm beenden? Type 'y' or 'n': ")
    exitCmd = str(input())
    if exitCmd == "y" :
        exit()

