##INTELLECTUAL PROPERTY OF LUCKY GORAYA AND PROMETHEAN ENTERPRISES
##ANYONE WHO REMOVES THIS HEADER OR TRIES TO SELL THIS CODE WILL BE DEALT WITH
## GITHUB.COM/LUCKY-PROMETHEAN
##THIS PROGRAM ALLOWS YOU TO DIVIDE ONE NUMBER BY MULTIPLE DIFFERENT NUMBERS REPEATEDLY QUICKLY

V = float(input("Enter number that will stay constant , 0 for default [10] "));
if V==0: V=10;
i=1
result=0
finalincrement=int(input("how many repitions "));
while i<finalincrement+1:
        num = float(input("Enter number "));
        print ("division number", i)
        print(V/num)
        i=i+1


