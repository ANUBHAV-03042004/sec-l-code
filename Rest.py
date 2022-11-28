a=eval(input("enter the first number:"))
b=eval(input("enter the second number:"))
o=(input("enter '+'for addition ||'-'for subtraction||'*'for multiplication||'/'for division:"))



if o == ("+") :
    
      c = a + b
      print (f"The sum of {a} and {b} is {c}")
    

elif (o=='-'):
       c = a - b
       print (f"The subtraction of {a} and {b} is {c}")


elif (o=='*'):
       c = a * b
       print (f"The multiplication of {a} and {b} is {c}")

elif (o=='/'):
       c = a / b
       print (f"The division of {a} and {b} is {c}")


else:
    print("invalid")



