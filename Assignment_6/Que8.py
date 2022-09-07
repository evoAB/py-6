print("ax^2+bx+c")
a=int(input("Enter a"))
b=int(input("Enter b"))
c=int(input("Enter c"))

d=b**2-4*a*c
if(d==0):
    print("Roots are real and equal")
else:
    if(d>0):
        print("Roots are real and distinct")
    else:
        print("Roots are imaginary")