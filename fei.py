import numpy
from numpy import inf
add_number = int(input("Enter the number to add to the numbers: "))
rows = int(input("Enter the number of columns: "))

smaller_list =[1,2,3,4,5,inf]
columns = len(smaller_list)
print("                      ")
print("Defining the variables ...")
bigger_list = []
bigger_list.append(smaller_list)
print("                      ")
print("Adding {} to the previous list ...".format(add_number))

print("                      ")
print("Make sure the values are not larger than 10 ...")
while True:
    new_list = [x+add_number for x in bigger_list[-1] ]
    for n, i in enumerate(new_list):
        if i > 50:
            new_list[n] = i-50
        elif i >= 40:
            new_list[n] = i - 40
        elif i   >= 30:
            new_list[n] = i - 30
        elif  i >= 20:
            new_list[n] = i - 20
        elif i  > 10: #removing the = sign so that only numbers above 10 are liable to substract
            new_list[n] = i-10
        else:
            new_list[n] = new_list[n]
    bigger_list.append(new_list)
    if len(bigger_list) > rows:
        break
#print(bigger_list)
matrix = numpy.array(bigger_list)
print("                      ")
print("The following is your {} * {} matrix".format(columns,rows) )
print(matrix)
