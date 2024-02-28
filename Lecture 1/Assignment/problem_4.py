def is_palindrome(num):
    """
        A function to check whether an integer represents a palindrome in binary
        @num: the integer to verify
        @return: True or False
    """
    # Please write your code here
    pass
    left = num // 2
    right = num // 2 + 1
    test = left ^ right
    result = num ^ test
    if result | test == num:
        return True

    else:
        return False



def main():
    print(is_palindrome(220395))  # should print True
    # 220395 is 110101110011101011 in binary (valid palindrome)

    print(is_palindrome(1060))  # should print False
    # 220395 is 10000100100 in binary (not a palindrome)

    print(is_palindrome(75817))  # should print True
    # 220395 is 10010100000101001 in binary (valid palindrome)

    print(is_palindrome(820))  # should print False
    # 220395 is 1100110100 in binary (not a palindrome)

    print(is_palindrome(5557))  # should print True
    # 220395 is 1010110110101 in binary (valid palindrome)
    print(is_palindrome(47))


if __name__ == '__main__':
    main()
