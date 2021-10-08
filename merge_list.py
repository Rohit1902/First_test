# program to take two lists and then merge them
first=[]
second=[]
third=[]

n1=int(input("How many elements do u want in first list : "))
n2=int(input("How many elements do u want in second list : "))

i=j=0
print("Enter elements for first list")
while(i!=n1):
    m=int(input("enter element "))
    first.append(m)
    i+=1

print("Enter elements for second list")
while(j!=n2):
    m=int(input("enter element "))
    second.append(m)
    j+=1

print("The first list is : ",first)
print("The second list is : ",second)

k=l=0
while(k!=n1):
    # print("HI")
    third.append(first[k])
    k+=1

while(l!=n2):
    third.append(second[l])
    l+=1

print("the merged list is : ",third)


