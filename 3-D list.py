# 3X3X3 list
# [[['#', '#', '#'], ['#', '#', '#'], ['#', '#', '#']],
#  [['#', '#', '#'], ['#', '#', '#'], ['#', '#', '#']],
#  [['#', '#', '#'], ['#', '#', '#'], ['#', '#', '#']]]

 # concept of 2-D array doesnt work here
# [[['#','#'],['#','#'],['#','#'],         
#   [['#','#'],['#','#'],['#','#'],
#   ['#','#'],['#','#'],['#','#'],
#   ['#','#'],['#','#'],['#','#'],
#   ['#','#'],['#','#'],['#','#']
# # 5 X 3 X 2 list
# [[['#', '#', '#', '#', '#'],['#', '#', '#', '#', '#'],['#', '#', '#', '#', '#']],
#  [['#', '#', '#', '#', '#'],['#', '#', '#', '#', '#'],['#', '#', '#', '#', '#']]]
import pprint

col1=3
col2=3
row1=3
# first 3 columns, second 3 columns, third 3 rows
def three_D(a,b,c):
    list1=[[['1' for col in range(a)] for col in range(b)] for row in range(c)]
    list2=[[['2' for col in range(a)] for col in range(b)] for row in range(c)]
    print("First list is")
    pprint.pprint(list1)
    print("Second list is")
    pprint.pprint(list2)
    print("Merged list is : ")
    list=list1+list2
    return list

    

pprint.pprint(three_D(col1,col2,row1))    


