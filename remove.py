# program to input elementa in list and remove certain elements on request of user
firstList = []

n = int(input("How many elements do u want to enter : "))
i = 0
while i != n:
    m = int(input("Enter element no{0} : ".format(i + 1)))
    firstList.append(m)
    i += 1

print(firstList)

check = input(
    "Do you want to remove any elements from the list? (y for yes , n for no)"
)
if check == "y":
    while check == "y":
        r = int(input("Which element do you want to remove ? :"))
        if r in firstList:
            firstList.remove(r)
        else:
            print("Element not found in list")

        check = input("Do you want to remove more elements from the list(y/n)")
        if check != "y":
            break

print("The final list is ", firstList)
