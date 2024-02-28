def add_numbers(b1, b2):
    """
       This functions performs a logical addition
    """

    # Please write your code here
    while b2 != 0:
        carry = b1 & b2
        b1 = b1 ^ b2
        b2 = carry << 1

    return b1


def mul_numbers(b1, b2):
    """
       This functions performs a logical multiplication
    """

    # Please write your code here
    result = 0
    while b2 != 0:
        if b2 & 1:
            result = add_numbers(result, b1)
        b1 = b1 << 1
        b2 = b2 >> 1

    return result


def and_numbers(b1, b2):
    """
       This functions performs a logical and
    """

    # Please write your code here
    return b1 & b2


def or_numbers(b1, b2):
    """
       This functions performs a logical or
    """

    # Please write your code here
    return b1 | b2


def xor_numbers(b1, b2):
    """
       This functions performs a logical xor
    """

    # Please write your code here
    return b1 ^ b2


def main():
    print(add_numbers(3, 12))  # should return 15
    print(mul_numbers(3, 12))  # should return 36
    print(and_numbers(3, 12))  # should return 0
    print(or_numbers(3, 12))  # should return 15
    print(xor_numbers(3, 12))  # should return 15


if __name__ == '__main__':
    main()
