def find_missing(lis):
    """
       This function finds a missing element
    """

    # Please write your code here
    if not lis:
        return None

    n = len(lis) + 1
    expected_sum = (n * (n + 1)) // 2
    actual_sum = sum(lis)

    return expected_sum - actual_sum if (expected_sum - actual_sum) < max(lis) else None


def main():
    lis = [i for i in range(1, 3000)]
    print(find_missing(lis))  # should print 2

    lis = [i for i in range(1, 49) if i != 40]
    print(find_missing(lis))  # should print 40

    lis = [4, 1, 3]
    print(find_missing(lis))  # should print 2


if __name__ == '__main__':
    main()
