def encrypt(input_string, row_count):
    """
       This function receives a string and the row count for the matrix.
       Implement the algorithm and return the encrypted text.
    """

    # Please write your code here
    row = [[] for i in range(row_count)]

    line = 0
    upward = True
    output = []
    for i in range(len(input_string)):
        row[line].append(input_string[i])
        if line != 0 and line != (row_count - 1):
            if upward:
                line -= 1

            else:
                line += 1

        elif line == 0:
            line += 1
            upward = False

        else:
            line -= 1
            upward = True

    for i in row:
        output += i

    return ''.join(output)






def decrypt(input_string, row_count):
    """
       This function receives a string and the row count for the matrix.
       Implement the algorithm and return the decrypted text.
    """

    # Please write your code here



def main():
    res = encrypt("DATASTRUCTURES", 3)
    print(res)  # should print DSCEAATUTRSTRU
    res = decrypt("DSCEAATUTRSTRU", 3)
    print(res)  # should print DATASTRUCTURES

    res = decrypt("CSORCMEIEPTECUN", 5)
    print(res)  # should print COMPUTERSCIENCE
    res = encrypt("COMPUTERSCIENCE", 5)
    print(res)  # should print CSORCMEIEPTECUN


if __name__ == '__main__':
    main()
