
import numpy
from numpy import inf
from random import randint

def matrix():
    number = float(input("Please key in the number to be added to the matrix: "))
    rows = int(input("\nPlease key in the number of the rows: "))
    columns = int(input("\nplease key in the number of the columns: "))

    #columns = len(smaller_list) not recquired

    smaller_list = []
    while columns > 0:
        random_number = randint(0, 10)
        smaller_list.append(random_number)
        if len(smaller_list) == columns -1:
            break
        else:
            continue
    #smaller_list.append(inf)

    print("\nDefining the variables ...")

    bigger_list = []
    #smaller_list=[int(x) for x in input('Enter first row: ').split()]
    #smaller_list=smaller_list[0:columns-1]
    #print(smaller_list)
    #smaller_list.append(inf)
    bigger_list.append(smaller_list)
    print("\nAdding %d to the previous list ..." %(number))
    print("\nMaking sure the values are not larger than 10 ...")

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
matrix()
