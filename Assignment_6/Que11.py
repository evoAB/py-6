m=int(input("Enter month number : "))
if m in (1,3,5,7,8,10,12):
    print("31 days")
elif m in (4,6,9,11):
    print("30days")
elif m==2:
    print("28 or 29 days")
else:
    print("Invalid month")