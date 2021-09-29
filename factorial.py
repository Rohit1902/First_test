#program to print factorial of integer provided by user

n=int(input("Enter the number : "))

fact =1
for i in range(1,n+1):
   fact=fact*i

print("Factorial of {0} is {1}".format(n,fact))
