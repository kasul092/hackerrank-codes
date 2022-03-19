from collections import Counter
X = input()
S = Counter(map(int,input().split()))
N = int(input())
earnings = 0
for customer in range(N):
    size, x_i = map(int,input().split())
    if size in S and S[size] > 0:
        S[size] -= 1
        earnings += x_i
            
print(earnings) 

# input
10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50

# output = 200