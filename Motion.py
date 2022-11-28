a=eval(input("enter the first number:"))
b=eval(input("enter the second number:"))
y=(input("enter'pi'for pi value ||'e' for e value:"))
o=(input("enter '+'for addition ||'-'for subtraction||'*'for multiplication||'/'for division:"))

pi=3.14
e=2.71

if ((y =='pi') and (o =='+')):
           g= ((a*pi)+(b*pi))
           print (f"pi_The sum of {a} and {b} is {g}")


elif((y =='e') and (o =='+')):
        h=((a*e)+(b*e))
        print (f"e_The sum of {a} and {b} is {h}")
    
elif ((y =='pi') and (o =='/')):
         g= ((a*pi)/(b*pi))
         print (f"pi_The division of {a} and {b} is {g}") 
elif ((y =='e') and (o =='/')):
           h=((a*e)/(b*e))
           print (f"e_The division of {a} and {b} is {h}")
        
elif ((y =='pi') and (o =='*')):
           g= ((a*pi)*(b*pi))
           print (f"pi_The multiplication of {a} and {b} is {g}") 

elif ((y =='e') and (o =='*')):
          h=((a*e)*(b*e))
          print (f"e_The multiplication of {a} and {b} is {h}")
        
elif ((y =='pi') and (o =='-')):
          g= ((a*pi)-(b*pi))
          print (f"pi_The subtraction of {a} and {b} is {g}")

elif ((y =='e') and (o =='-')):
           h=((a*e)-(b*e))
           print (f"e_The subtraction of {a} and {b} is {h}")

else:
            print("invalid command")