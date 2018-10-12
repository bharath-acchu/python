
print('\n\t\t\t SIMPLE CALCULATOR\n')
while 1:
    print('which operation you want to ?\n')
    print('1.addition\n2.subtraction\n3.multiplication\n4.division\n')
    ch=int(input('ENTER YOUR CHOICE\n'))
    a=float(input("Enter first number\n"))
    b=float(input("Enter second number\n"))
    
    if ch is 1:                        #is also used as equality operator
        print("ans=",a+b)
    elif(ch==2):
        print("ans=",a-b)
    elif(ch==3):
        print("ans=",a*b)
    elif(ch==4):
        print("ans=",a/b)
    else:print("improper choice\n")
