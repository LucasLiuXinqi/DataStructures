def rotator(M, a, d):
    """
        a in {0, 90, 180}
        d in {"clockwise","anticlockwise"}
        You should not change the value of M in this function.
    """
    # Please write your code here
    column = len(M[0])
    line = len(M)
    matrix = [[0] * column for i in range(line)]
    if a == 0:
        matrix = M

    elif a == 90:
        if d == 'clockwise':
            for i in range(line):
                for j in range(column):
                    matrix[j][column - i - 1] = M[i][j]


        elif d == 'anticlockwise':
            for i in range(line):
                for j in range(column):
                    matrix[line - j - 1][i] = M[i][j]

    elif a == 180:
        for i in range(line):
            for j in range(column):
                matrix[line - i - 1][column - j - 1] = M[i][j]

    return matrix

def main():
    mat = [ [ 1, 2, 3, 4, 5], \
            [ 6, 7, 8, 9,10], \
            [11,12,13,14,15], \
            [16,17,18,19,20], \
            [21,22,23,24,25] ]
    new_mat = rotator(mat,180,"anticlockwise")
    print(new_mat)
    # should print [ [ 5,10,15,20,25], \
            #        [ 4, 9,14,19,24], \
            #        [ 3, 8,13,18,23], \
            #        [ 2, 7,12,17,22], \
            #        [ 1, 6,11,16,21] ]
    new_mat = rotator(mat,0,"anticlockwise")
    print(new_mat)
    # should print [ [ 1, 2, 3, 4, 5], \
            #        [ 6, 7, 8, 9,10], \
            #        [11,12,13,14,15], \
            #        [16,17,18,19,20], \
            #        [21,22,23,24,25] ]


if __name__ == '__main__':
    main()