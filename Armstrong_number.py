# PROGRAM TO DETERMINE WHETHER A NUMBER IS A ARMSTRONG NUMBER OR NOT
n=int(input("Enter a number : "))
a=b=n
count=sum=0
while(n!=0):
    count+=1
    n=n//10  
    print(n)

print(count)

while(b!=0):
    sum+=(b%10)**count
    b=b//10

print(sum)

if(sum==a):
    print("{0} is a Armstrong number".format(a))
else:
    print("{0} is not a  Armstrong number".format(a))

       
# def Order(x):
#     n=0
#     while(x!=0):
#         n+=1
#         x=x//10

#     return n





