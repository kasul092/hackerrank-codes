
def print_full_name(first, last):
    # first, last = input(" ").split("\n")
    a = ("Hello {} {}! You just delved into python.".format(first,last))
    return a



if __name__ == "__main__":
    first_name = input()
    last_name = input()
    print(print_full_name(first_name, last_name))


# output:- Hello sumit pujari! You just delved into python.
