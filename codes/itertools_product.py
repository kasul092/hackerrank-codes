from itertools import product

A = map(int,input().split())
B = map(int,input().split())

for item in product(A,B):
    print(item,end=' ')

# input = A = 1,2
# B = 3,4
# output = (1, 3) (1, 4) (2, 3) (2, 4) 