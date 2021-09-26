# program to return simple interest on principal provided by the user
p = int(input("Enter your principal amount : "))
r = int(input("Enter  rate per annum : "))
t = int(input("Enter time period : "))

sInterest=(p*r*t)/100
p=p+sInterest
print("The simple Interest is :{0}\nThe new amount is : {1} ".format(sInterest,p))
 #today i am learning git. I made some changes to the previous file.
 #I also did a factorial program using loops
 # I learnt what OSI is