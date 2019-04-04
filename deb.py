import numpy
from itertools import islice

m = int(input("\nPlease key in the number to be added to the matrix: "))

noma = int(input("\nPlease key in the number to be maximum: "))

bnote = [[1,2,3],[3,4,5],[1,6,7],[2,4,6],[2,5,7],[3,4,7],[3,5,6]]

def chunk(it, size):
    it = iter(it)
    return iter(lambda: tuple(islice(it, size)), ())

def matrix():
    #n = int(input("\nPlease key in the number of columns: "))
    bnote = [[1,2,3],[3,4,5],[1,6,7],[2,4,6],[2,5,7],[3,4,7],[3,5,6]]
    #noma = int(input("\nPlease key in the number to be maximum: "))
    i = 1
    while True:
        print("\nThis is the matrix number %d: " %(i))
        #print(bnote)
        print(numpy.array(bnote))
        i += 1
        bnote = numpy.array(bnote) + m
        bnote = bnote.tolist()
        #print(bnote)
        for item in bnote:
            for i,number in enumerate(item):
                if number >m:
                    item[i] = number - m
        #print(bnote)
        """
        for item in bnote:
            for i,number in enumerate(item):
                if number>noma:
                    item[i] = number - m
                    """
        if i == 10:
            break
        #return bnote
matrix()
