str=input("enter any string=")
len=len(str)
c=0
g=0
l=0
sp=0
s=0
u=0
i=0
v=0

for i in range(0,len):
    st=str[i]
    i=i+1
    if st.isdigit():
       c=c+1
    if st.isalpha():
     g=g+1
    if st.islower():
        l=l+1
    if st.isupper():
        u=u+1
    if st=='a' or st=='A'or st=='E' or st=='I' or st=='O' or  st=='U' or  st=='e' or st=="i" or st=="u" or st=="o":
        v=v+1
    elif st==" ":
         s=s+1
    else:
        sp=sp+1
print("special character:",sp)
print("no.of digits in the given string are:",c)
print("no.of alphabets in the given string are:",g)
print("no.of spaces in the given string are:",s)
print("no.of lower characters in the given string are:",l)
print("no.of upper characters in the given string are:",u)
print("no.of vowels in the given string are:",v)
