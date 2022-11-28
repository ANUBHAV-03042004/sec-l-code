#dimensions of brick
h1=int(input("enter height of brick="))
l1=int(input("enter length of brick="))
w1=int(input("enter width of brick="))
d1=h1*l1*w1
print("dimension of 1 brick is=",d1)
#dimensions of wall
h2=int(input("enter height of wall="))
l2=int(input("enter length of wall="))
w2=int(input("enter width of wall="))
d2=h2*l2*w2
print("dimension of wall is=",d2)

print("total no. of bricks in wall=",int(d2/d1))