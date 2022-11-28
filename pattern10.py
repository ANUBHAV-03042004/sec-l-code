a=int(input('enter the length='))
for i in range(1,a):
    for j in range(a,i,-1):
        print(" ",end='')
    for j in range(1,i+1):
           if(j==1 or j==i):
              print("* ",end='')
           else:
              print("  ",end='')





    print()    
for i in range(1,a+1):
    for j in range(1,i):
        print(" ",end='')
    for j in range(a,i-1,-1):
        if(j==a or j==i):
         print("* ",end='')
        else:
            print("  ",end='')
    print()    