a=int(input("enter the year="))
if a%400==0  or a%100!=0 and a%4==0:
    print("leap year")
else:
    print("not a leap year")