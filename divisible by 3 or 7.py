a =(int(input("enter the value =")))
if(a%3==0):
    print("divisible by 3",a//3)
if(a%7==0):
    print("divisible by 7",a//7)
if(a%3==0)and(a%7==0):
    print("divisible by both",a//3,a//7)
else:
   print("divisible by none")