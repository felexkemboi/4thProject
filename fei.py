import numpy
from numpy import inf
add_number = int(input("Enter the number to add to the numbers: "))
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
        #if i > 50: #not necessary
            #new_list[n] = i-50
        #elif i >= 40:
            #new_list[n] = i - 40
        #elif i   >= 30:
            #new_list[n] = i - 30
        #elif  i >= 20:
            #new_list[n] = i - 20
        if i  >=10:
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
print(matrix)
