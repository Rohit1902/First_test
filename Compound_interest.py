# PROGRAM TO CALCULATE COMPOUND INTEREST OVER PRINCIPAL VALUE PROVIDED BY USER
p = float(input("Enter your principal amount : "))
r = float(input("Enter  rate per annum : "))
t = float(input("Enter duration of each time period : "))
n = float(input("Enter no of time periods : "))

cInterest=p*(1+r/n)**(n*t) - p     #formula for CI
amt=p*(1+r/n)**(n*t)

print("The compound interest is {0:.2f} and the new amount is {1:.2f}".format(cInterest,amt))
