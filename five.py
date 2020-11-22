import numpy
import operator
import functools
original_matrix =  [[1,3,4,5,9],   [2,4,5,6,10],  [3,5,6,7,0],   [4,6,7,8,1],  [5,7,8,9,2],   [6,8,9,10,3],  [7,9,10,0,4], [8,10,0,1,5],  [9,0,1,2,6],  [10,1,2,3,7], [0,2,3,4,8]]
def matrix():
    rows = int(input("\nPlease key in the number of matrices: "))
    m = int(input("\nPlease key in the number to be added to the matrix: "))
    n = 5

    bigger_list = functools.reduce(operator.iconcat, original_matrix, [])

    matrix = [bigger_list[i * n:(i + 1) * n] for i in range((len(bigger_list) + n - 1) // n )]

    output_matrix = matrix[:rows]


    i =1
    while True:
        print("\nThis is the matrix number %d: " %(i))
        print(numpy.array(output_matrix))

        i += 1
        def fanya():
            for y in output_matrix:
                new_list = []
                y[:]=[i+ m for i in y]

            for a in output_matrix:
                small_new_list = []
                for b in a:
                    if b > 10:
                        small_new_list.append(b - 10)  
                    else:
                        small_new_list.append(b) 
                new_list.append(small_new_list)
            return new_list
            
        output_matrix = fanya()
        if i == rows + 1:
            break
matrix()


