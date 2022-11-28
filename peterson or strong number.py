#peterson number= 145=1!+4!+5!=145
num=int(input("enter a number="))
sum=0
copy=num
while(num!=0):
    fact=1
    i=1
    d=num%10 
    while(i<=d):
      fact=fact*i
      i=i+1   
    sum=sum+fact
    num=num//10
if sum==copy:
  print(sum,"is a peterson number")
else:
    print(sum,"is not a peterson number")
