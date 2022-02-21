# Find  the index of "umit" in "I am sumit Pujari"
# You should not use any string operators or methods or packages
# You have to implement it


def find_index(string, sub_string):
    index = 0
    end = 0
    if index < len(string):
        for i in range(len(string)):
            if string[index+end] != sub_string[end]:
                index += 1
                end = 0
                continue
            end += 1
            if end == len(sub_string):
                return ("substring present in string on index is ",index)
    return -1
string = "I am sumit Pujari"
sub_string = "umit"
print(find_index(string, sub_string))