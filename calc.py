while True:

    print("Enter number 1: ")
    num1 = int(input())
    print("Enter number 2: ")
    num2 = int(input())
    print("Enter Math Operation:")
    math1 = input()
    if  math1 == "addition" or math1 =="add":
        print("Sum: " + str(num1+num2))
    if math1 == "multiply" or math1 == "multi":
        print("Product: " + str(num1*num2))
    print("Wanna continue (type 'yes' or 'y') or exit (type 'exit' or 'e')?")
    userinput = input()
    if userinput == "yes" or userinput =="y":
        print("here we go again")
        

    if userinput == "exit" or userinput == "e":
        print("see you later")
        exit()
    
