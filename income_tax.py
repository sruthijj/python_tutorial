"""
    The tax is calculated as follows :
    if the income is <=250000 then no tax
    if the income is >250000 and <=500000 then tax is 5%
    if he income is >500000 and <=750000 then tax is 10%
    if the income is >750000 and <=1000000 then tax is 15%
    print tax amount
"""
income =int(input("Enter your income :"))
if income <= 250000:
    print("No Tax")
elif income > 250000 and income <= 500000:
    tax =  income * 0.05
    print("your annual income is",income ,"And the Tax Amount is :",tax)
elif income > 500000 and income <= 750000:
    tax = income * 0.10
    print("your annual income is",income ,"And the Tax Amount is :",tax)
elif income > 750000 and income <= 1000000:
    tax = income*0.15
    print("your annual income is",income ,"And the Tax Amount is :",tax)

