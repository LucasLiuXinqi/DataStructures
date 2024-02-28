def is_palindrome(num):
    # Please write your code here
    reverse = 0
    temp = num
    while temp > 0:
        reverse = (reverse << 1) | (temp & 1)
        temp = temp >> 1

    return reverse == num


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


if __name__ == '__main__':
    main()
