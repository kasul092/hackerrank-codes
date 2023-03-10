# Given an array of integers, where all elements but one occur 
# twice, find the unique element.
# Example
# a = [1,2,3,4,3,2,1]
# The unique element is 4.

def lonelyinteger(a):
    for i in a:
        s =a.count(i)
        if s >1:
            pass
        else:
            return i
a = [1,2,3,4,3,2,1]
result = lonelyinteger(a)
print(f"the unique integer is {result}")






def lonely(a):
    l = [i for i in a if a.count(i) == 1]
    return l
print(lonely([1,2,3,4,5,4,3,2,1]))
