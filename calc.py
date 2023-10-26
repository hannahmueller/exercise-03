x = True
while x:
    print("Enter number 1: ")
    num1 = int(input())
    print("Enter number 2: ")
    num2 = int(input())
    print("Enter function: addition  or multiplication")
    func = str(input())
    if func == "add" :
        print("Sum: " + str(num1+num2))
    if func == "mult" :
        print("Product: " + str(num1*num2))
    print("Do you want to continue?")
    y = str(input())
    if y == "" :
        break