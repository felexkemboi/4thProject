import numpy
bnote = [[1,2,3],[3,4,5],[1,6,7],[2,4,6],[2,5,7],[3,4,7],[3,5,6]]
def matrix():
    noma = int(input("\nPlease key in the number to be maximum: "))

    n = int(input("\nPlease key in the number of columns: "))
    m = int(input("\nPlease key in the number to be added to the matrix: "))

    #noma = noma + 1

    my_list = list(range(1,noma))

    bigger_list = my_list*100

    matrix = [bigger_list[i * n:(i + 1) * n] for i in range((len(bigger_list) + n - 1) // n )]

    mwisho = matrix[:noma]


    i =1
    #print(mwisho)
    while True:
        print("\nThis is the matrix number %d: " %(i))

        print(numpy.array(mwisho))

        i += 1
        #new_list = [[z+m for z in y] for y in mwisho]
        def fanya():
            for y in mwisho:
                for x in y:
                    x = x+m
                    if x>noma:
                        x = x-noma
            return mwisho
        mwisho = fanya()

        """
        for k in new_list:
            for l in k:
                if l > noma:
                    l = l-noma
                else:
                    l = l
        """
        #print(numpy.array(new_list))
        if i == 10:
            break
        """
        for n, i in enumerate(new_list):
            if i >= 10:
                new_list[n] = i-noma
            else:
                new_list[n] = new_list[n]
        #if len(bigger_list) >= rows:
        mwisho = new_list
        if i == 10:
            break"""
matrix()





"""
bnote = [[z+m for z in y] for y in bnote]

def fanya():
    #noma = noma -1
    for item in bnote:
        for number in item:
            number = number+m
            if number>noma:
                number = number-noma
    return bnote
bnote = fanya()"""



"""
for j in bnote:
    for number in j:
        number += mnumpy.array(bnote)
        if number>noma:
            number = number - noma
            #new_small_list = list(new_small_list.append(number))
            new_small_list.append(number)
        else:
            new_small_list.append(number)"""
"""
new_small_list = []
new_bigger_list = []
for j in bnote:
    for number in j:
        number += mnumpy.array(bnote)
        if number>noma:
            number = number - noma
            #new_small_list = list(new_small_list.append(number))
            new_small_list.append(number)
        else:
            new_small_list.append(number)
"""
#new_small_list = list(new_small_list)
#new_bigger_list.append(new_bigger_list)
"""
#new_bigger_list = list(new_small_list)
#new_bigger_list.append(new_small_list)
#bnote = list(chunk(new_bigger_list, 3))"""
