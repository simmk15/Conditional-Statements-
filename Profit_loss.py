sp=int(input("Enter the selling price="))
cp=int(input("Enter the cost price="))
if sp>cp:
    print("It is a profit of Rs.",sp-cp)
else:
    print("It is a loss of Rs.",cp-sp)