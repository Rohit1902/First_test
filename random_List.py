# program to generate random list and remove numbers divisible by 2

import random    #import random_List

randomList=[]
evenList=[]
i=0
while (i!=10):
    n=random.randint(1,100)
    randomList.append(n)
    i+=1
print("Random list is : ",randomList)    

# j=0
# for j in range(0,10):
#     print(randomList)
#     if((randomList[j]%2)==0):
#        del randomList[j]
#     j+=1

for element in randomList:
    # print(element)
    if((element%2)==0):
        evenList.append(element)

print(evenList)       
for element in evenList:
    randomList.remove(element)

print("Final List is : ",randomList)

         






