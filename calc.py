
while True:
    print("Enter number 1: ")
    num1 = int(input())
    print("Enter number 2: ")
    num2 = int(input())
    print("Enter math operation")
    operation = input()
    if operation.casefold() == "add" or operation.casefold() == "addition":
        print("Sum: " + str(num1+num2))
    if operation.casefold() == "multi" or operation.casefold() == "multiplication":
        print("Product: " + str(num1*num2))
        
    print ("w fuer weiter und e für exit")
    end = input()
    if end == "e":
        exit()