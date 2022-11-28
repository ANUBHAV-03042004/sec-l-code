#sum of all prime numbers

a=int(input("enter any integer="))

s=0
for i in range(2,a+1):
    for j in range(2,i):
        if(i%j==0):
            break
    else:
            s=s+i
print ("sum of all prime numbers",s)
