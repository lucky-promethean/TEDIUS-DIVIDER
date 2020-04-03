##INTELLECTUAL PROPERTY OF LUCKY GORAYA AND PROMETHEAN ENTERPRISES
##ANYONE WHO REMOVES THIS HEADER OR TRIES TO SELL THIS CODE WILL BE DEALT WITH
## GITHUB.COM/LUCKY-PROMETHEAN
##THIS PROGRAM ALLOWS YOU TO DIVIDE ONE NUMBER BY MULTIPLE DIFFERENT NUMBERS REPEATEDLY QUICKLY

V = float(input("Enter number that will stay constant "))
if V==0: V=10;
i=1
result=0
torb=str(input("is the constant number to appear at the [t]op or [b]ottom"))
checker=bool;
if torb=='t': checker=bool(1)

finalincrement=int(input("how many repitions "));
while i<finalincrement+1:
    num = float(input("Enter number "));
    if checker==(1): result=V/num
    else: result=num/V
    print ("division number", i);
    print(result)
i=i+1

