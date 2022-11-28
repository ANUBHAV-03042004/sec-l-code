x=int(input("enter the value of x="))
y=int(input("enter the value of y="))
if(x==0)and(y==0):
    print("it lies in origin")
elif(x>0)and(y>0):
 print("it lies in 1st quadrant")
elif(x<0)and(y>0):
 print("it lies in 2nd quadrant")
elif(x<0)and(y<0):
 print("it lies in 3rd quadrant")
elif(x>0)and(y<0):
 print("it lies in 4th quadrant")
elif x==0:
    print("y axis")
else:
    print("x axis")