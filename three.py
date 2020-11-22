import numpy
import operator
import functools
original_matrix =  [[1,2,3],[5,6,7],[2,3,4],[3,4,5],[4,5,6],[6,7,1],[7,1,2]]
def matrix():
    rows = int(input("\nPlease key in the number of matrices: "))
    m = int(input("\nPlease key in the number to be added to the matrix: "))
    n = 3

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
                    if b > 7:
                        small_new_list.append(b - 7)  
                    else:
                        small_new_list.append(b) 
                new_list.append(small_new_list)
            return new_list
            
        output_matrix = fanya()
        if i == rows + 1:
            break
matrix()
