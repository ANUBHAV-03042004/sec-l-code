# 153=1^3+5^3+3^3=153

a=(int(input("enter any number:")))
c=0
sum=0
num=a
b=num
while(a!=0):
     h=a%10
     c=c+1
     a=a//10

while(num!=0):
    h=num%10
    sum+=(h**c)
    num=num//10

if sum==b:
    print("armstrong")
else:
      print("not an armstrong")