x = True
while x:
    print("Enter number 1: ")
    num1 = int(input())
    print("Enter number 2: ")
    num2 = int(input())
    print('commands: multi,add ')
    func = str(input())
    if(func == 'multi'):
        res = num1 * num2
        print('result', res)
    elif(func == 'add'):
        res = num1 + num2
        print('result', res)
    else:
        print('non valid')

    print('command for continue c')
    resume = str(input())
    if not (resume == 'c'):
        x = False

