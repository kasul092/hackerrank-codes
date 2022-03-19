# a_string = "abcdefghijklmnopqrstuvwxyz"
# s = ""
# n = 4
# for index in range(0, len(a_string), n):
#     s = a_string[index : index + n]
#     print(s)


import textwrap

def wrap(a_string, n):
    a = textwrap.fill(a_string, n)
    print(a)
    return a
wrap("abcdefghijklmnopqrstuvwxyz", 4)


