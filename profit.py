ac = float(input("pls enter the actual pruduct prize"))
sa = float(input("pls enter the sales"))
if(sa>ac):
    amount=sa-ac
    print("total profit=",amount)
else:
    print("no profit!")