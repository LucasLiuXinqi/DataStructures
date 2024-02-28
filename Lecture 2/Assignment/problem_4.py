def find_missing(lis):
    """
       This function finds a missing element
    """

    # Please write your code here
    # pass
    max_num = 0
    for i in lis:
        if i >= max_num:
            max_num = i

    standard_sum = 0
    for j in range(1, max_num + 1):
        standard_sum ^= j

    real_sum = 0
    for k in range(len(lis)):
        real_sum ^= lis[k]

    if standard_sum ^ real_sum != 0:
        return standard_sum ^ real_sum
    else:
        return None


def main():
    lis = [i for i in range(1, 5) if i != 2]
    print(find_missing(lis))  # should print 2

    lis = [i for i in range(1, 49) if i != 40]
    print(find_missing(lis))  # should print 40

    lis = [4, 1, 3]
    print(find_missing(lis))  # should print 2


if __name__ == '__main__':
    main()
