# def count_substring(string, sub_string):
#     for i in range(0, len(string)): 
#         a = sub_string.count(string[i])
#     return a

# if __name__ == '__main__':
#     string = "ABCDCDC".strip()
#     sub_string = "CDC".strip()
    
#     count = count_substring(string, sub_string)
#     print(count)



# using re
import re

def count_substring(string, sub_string): 
    match = re.findall('(?='+sub_string+')',string)
    return len(match) 

if __name__ == '__main__':
    string = "ABCDCDC".strip()
    sub_string = "CDC".strip()
    
    count = count_substring(string, sub_string)
    print(count)