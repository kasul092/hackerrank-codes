# k = 2
# l = [i for i in range(1, 5+1)]
# # for i in range(1, k+1):
# #     l.sort(by = "quicksort")
# #     print(l)

# l = l[3:]+l[:3]
# print(l)

list_1 = [1, 2, 3, 4, 5]
n = 4 
print ("Original List : " + str(list_1)) 
list_1 = [list_1[(i + n) % len(list_1)] for i, x in enumerate(list_1)]
print ("Rotated list : " + str(list_1)) 