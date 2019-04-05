import numpy
originalsample = [[1,2,3],[3,4,5],[1,6,7],[2,4,6],[2,5,7],[3,4,7],[3,5,6]]
sample = [[1,2,3],[3,4,5],[1,6,7],[2,4,6],[2,5,7],[3,4,7],[3,5,6]]
add = float(input("Please key in the number to be added to the matrix: "))
limit = int(input("\nplease key in the number of the limit to be looped in the matrix: "))

k = 1
while True:
    print("\nThis is the matrix number %d: " %(k))
    print(numpy.array(sample))
    k = k+1
    for item in sample:
        for i,number in enumerate(item):
            number +=add
            if number >limit:
                item[i] = number - limit
            else:
                item[i] = number
    if k == 9:
        break
