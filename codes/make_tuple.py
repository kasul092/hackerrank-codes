if __name__ == '__main__':
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    print(hash(t))