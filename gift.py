import numpy as np
n = int(input("Enter the number of rows in a matrix: "))
a = [[0] * n for i in range(n)]
for i in range(n):
   for j in range(n):
        a[i][j] = int(input())

print(np.matrix(a))
