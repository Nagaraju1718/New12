print("1.Addition 2.Substraction 3.Multiplication 4.Division 5.ModuloDivision")
choice=int(input("Enter choice"))
if(choice==1):
    print(a+b)
elif(choice==2):
    print(a-b)
elif(choice==3):
    print(a*b)
elif(choice==4):
    if(b==0):
        print("cant possible")
    else:
        print(a/b)
elif(choice==5):
    if(b==0):
        print("cant possible")
    else:
        print(a%b)
else:
    print("Select valid option")