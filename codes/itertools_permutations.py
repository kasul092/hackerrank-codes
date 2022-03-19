# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

A,B = map(str, input().split())
 
for i in permutations(sorted(A), int(B)):
    print("".join(i))
dtstud