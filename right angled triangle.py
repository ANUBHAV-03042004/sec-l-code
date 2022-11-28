a=(float(input("enter 1st side of triangle=")))
b=(float(input("enter 2nd side of triangle=")))
c=(float(input("enter 3rd side of triangle=")))
h=0

scalene=(a != b != c!=a)
print("it is a scalene triangle=",scalene)
isoceles=((a==b)or(b==c)or(c==a))
print("it is a isoceles triangle=",isoceles)

if(a>b)and(a>c):
    h=a
    if(h*h)==((b*b)+(c*c)):
     print("it is a right angled triangle")
    else:
     print("it is not a right angled triangle")

elif(b>a)and(b>c):
    h=b
    b=a
    if(h*h)==((b*b)+(c*c)):
      print("it is a right angled triangle")
    else:
     print("it is not a right angled triangle")
elif(c>a)and(c>b):
    h=c
    c=a
    if(h*h)==((b*b)+(c*c)):
     print("it is a right angled triangle")
    else:
     print("it is not a right angled triangle")
else:
    print("invalid")
