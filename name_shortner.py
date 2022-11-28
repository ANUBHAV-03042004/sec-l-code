#write a python program to take name from user and write it in short form input:Anubhav Kumar Srivastava

n = input("enter your name: ")
l=n.split()
p=""
for i in range(0,len(l)-1):
    p=p+l[i][0]+"."
p=p+" "+l[-1]
p=p.title()
print(p)

