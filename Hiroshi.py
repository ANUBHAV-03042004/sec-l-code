a=(int(input("enter amount="))-100)

if(a>=2000):
      b=(int(a/2000))
      print("no.of 2000 notes=",b)
if((a%2000)>=500):
     c=(int((a%2000)/500))
     print("no.of 500 notes=",c)
if(((a%2000)%500)>=200):
     d=(int(((a%2000)%500)/200))
     print("no.of 200 notes=",d)
    
if((((a%2000)%500)%200)>=100)or(a>=1) :
     e=int((((a%2000)%500)%200)/100)
     print("no.of 100 notes=",e+1)