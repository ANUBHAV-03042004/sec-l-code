a=int(input('enter the length='))
for i in range(1,a+1):
    for j in range(1,i):
        print(" ",end='')
    for j in range(a,i-1,-1):
        print("*",end='')
    print()    