a=(int(input("enter any integer=")))
rev=0
while(a!=0):
 j=a%10
 rev=rev*10+j
 a=a//10
print(rev)