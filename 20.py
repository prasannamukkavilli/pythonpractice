#write aprogram to accept the cost price of a bike and disply the road tax to be paid according to the fallowing criteria
#cost price  -  tax
#>100000          15%
#>50000           10%
#<50000            5%


price=float(input("enter the bike cost price"))
if price>100000:
    tax=0.15*price
    print("tax to be paid is",tax)
if price>50000 and price<=100000:
    tax=0.1*price
    print("tax to be paid is",tax)
if price<=50000:
    tax=0.05*price
    print("tax to be paid is",tax)
