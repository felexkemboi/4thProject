import numpy
from numpy import inf
"""add_number = int(input("Enter the number to add to the numbers: "))
rows = int(input("\nEnter the number of rows: "))

smaller_list =[1,2,3,4,5,inf]
columns = len(smaller_list)
#print("                      ")
print("\nDefining the variables ...")#add new line
bigger_list = []
bigger_list.append(smaller_list)
#print("                      ")
print("\nAdding {} to the previous list ...".format(add_number))

#print("                      ")
print("\nMake sure the values are not larger than 10 ...")
while True:
    new_list = [x+add_number for x in bigger_list[-1] ]
    for n, i in enumerate(new_list):
        if i  >10: #removing the = sign so that only numbers above 10 are liable to substract
            new_list[n] = i-10
        else:
            new_list[n] = new_list[n]
    bigger_list.append(new_list)
    if len(bigger_list) >= rows:#the loop breaks after rows - 1 iterations
        break
#print(bigger_list)
matrix = numpy.array(bigger_list)
#print("                      ")
print("\nThe following is your {} * {} matrix".format(rows,columns) )#interchange row and column
print(matrix)"""

print("""Hello, please call the matrix function and key in
1. the number to be added to the numbers.
2. the number of rows. i.e. in that order. in the brackets.""")

def matrix(number, rows):
    smaller_list = [1, 2, 3, 4, 5, inf]
    columns = len(smaller_list)
    print("\nDefining the variables ...")
    bigger_list = []
    bigger_list.append(smaller_list)
    print("\nAdding %d to the previous list ..." %(number))
    print("\nMake sure the values are not larger than 10 ...")
    while True:
        new_list = [x+number for x in bigger_list[-1]]
        for n, i in enumerate(new_list):
            if i >= 10:
                new_list[n] = i-10
            else:
                new_list[n] = new_list[n]
        bigger_list.append(new_list)
        if len(bigger_list) >= rows:
            break
    matrix = numpy.array(bigger_list)
    print("\nThe following is your %d * %d matrix!" %(rows, columns))
    print(matrix)

matrix(2, 2)


