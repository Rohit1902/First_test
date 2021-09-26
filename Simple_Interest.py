# program to return simple interest on principal provided by the user
p = int(input("Enter your principal amount : "))
r = int(input("Enter  rate per annum : "))
t = int(input("Enter time period : "))

sInterest=(p*r*t)/100
p=p+sInterest
print("The simple Interest is :{0}\nThe new amount is : {1} ".format(sInterest,p))
