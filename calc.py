
while True:
    print("Enter number 1: ")
    num1 = int(input())
    print("Enter number 2: ")
    num2 = int(input())

    print(" Please enter a '*' for multiply or a '+' for addition (add/addition and multi/multiplication is also possible): ")

    operation = str(input())


    if operation != '*' and operation != '+' and operation != 'add' and operation != 'addition' and operation != 'multi' and operation != 'multiplication' :
        print("[-] Operation not allowed. Please provide  '*' or  '+' or the names of the Operation")




    if operation == '*' or operation == 'multi' or operation == 'multiplication':
        print("Product: " + str(num1*num2))


    if operation == '+' or operation == 'add' or operation == 'addition':
        print("Sum: " + str(num1+num2))
    
    print("do you want to continue? y/n")
    inputValue= str(input())
    if inputValue == 'n' or inputValue == 'N':
        exit(0)
    
