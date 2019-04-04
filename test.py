import numpy
originalsample = [[1,2,3],[3,4,5],[1,6,7],[2,4,6],[2,5,7],[3,4,7],[3,5,6]]
sample = [[1,2,3],[3,4,5],[1,6,7],[2,4,6],[2,5,7],[3,4,7],[3,5,6]]
m = 9

k = 1
while True:
    print("\nThis is the matrix number %d: " %(k))
    print(numpy.array(sample))
    k = k+1
    for item in sample:
        for i,number in enumerate(item):
            number +=3
            if number >m:
                item[i] = number - m
            else:
                item[i] = number
    """if sample == originalsample:
        break"""
    if i == 10:
        break
#print(sample)
