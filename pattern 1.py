#5
# 54
# 543
# 5432
# 54321
a=int(input("enter the number how long  you wanted your pattern to be printed="))
rev=0
digits="0123456789"
for i in range(1,a+1):
    j=a-1
    rev=rev*10+j
    a=j 
    rev=(rev)

    print(rev)