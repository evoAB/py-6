a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))
if(a>b>c):
    print(a,"number is greater")
else:
    if(b>a>c):
        print(b,"number is greater")
    else:
        if(c>a>b):
            print(c,"number is greater")
        else:
            print("numbers are same : ",a)
