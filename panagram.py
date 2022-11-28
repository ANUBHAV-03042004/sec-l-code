#the quick brown fox jumps over the lazy dog
n=input().lower()
for i in range(97,123):
    c=chr(i)
    if c not in n:
        print("not panagram")
        break
else:
    print("panagram")

   
