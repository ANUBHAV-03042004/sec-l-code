
principal=float(input("enter the principal amount="))
rate=float(input("enter the rate of interest="))
time=float(input("enter the time in years="))
SI=(principal*rate*time)/100
print(f"simple interest on principal amount of {principal} is=",SI)
FINAL_AMOUNT =(principal + SI)
print(f"final amount of principal amount of {principal} is=",FINAL_AMOUNT)
per_month=(FINAL_AMOUNT/(time*12))
installments=(time*12)
print("you have to pay the final amount of %d rs. by paying  %d rs. per month till %d months"% (FINAL_AMOUNT,per_month,installments))

