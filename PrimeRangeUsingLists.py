# program to print priem numbers between in range given  by user(including the ranges)
lowerRange=int(input("Enter lower limit :"))
upperRange=int(input("Enter upper limit :"))

primeNumbers=[0]*(upperRange-lowerRange)
primeNumberIndex=0
flag=0

i=lowerRange
while(i!=upperRange):
    for j in range(2,i):
        if(i%j==0):
            flag=1

    if(flag==0):
        primeNumbers[primeNumberIndex]=i
    primeNumberIndex+=1
    flag=0
    i+=1

print("Prime numbers between {0} and {1} are :\n".format(lowerRange,upperRange))
print(primeNumbers)

                








