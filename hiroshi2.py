a=(int((input("enter the amount=")))-100)
twok=(a//2000)
print("no.of 2000 notes are=",twok)
a=(a-(2000*twok))
fiveh=(a//500)
print("no.of 500 notes are=",fiveh)
a=(a-(500*fiveh))
twoh=(a//200)
print("no.of 200 notes are=",twoh)
a=(a-(200*twoh))
oneh=(a//100)
print("no.of 100 notes are=",oneh+1)
a=(a-(100*oneh))