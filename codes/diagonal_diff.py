
#
# Complete the 'diagonalDifference' function below.
#find the difference between left and right diagonal of array.
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    l = len(arr[0])
    left = sum([arr[i][i] for i in range(l)])
    right = sum([arr[l-1-i][i] for i in range(l-1,-1,-1)])
    diff = right-left
    # print(f"left diagonal is {left}")
    # print(f"right diagonal is {right}")
    return diff

arr = [[11 ,2, 4],
        [4, 5, 6],
        [10, 8, -12]]

result = diagonalDifference(arr)
print(f"the diagonal difference is {result}")

