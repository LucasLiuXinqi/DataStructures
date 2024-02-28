def rotator(M,a,d):
    """
        a in {0, 90, 180}
        d in {"clockwise","anticlockwise"}
        You should change the value of M in this function
    """

    # Please write your code here
    line = len(M)
    column = len(M[0])

    if a == 0:
        pass

    elif a == 180:
        for i in range(line // 2):
            M[i], M[line - 1 - i] = M[line - 1 - i][::-1], M[i][::-1]

        if line % 2 == 1:
            M[line // 2] = M[line // 2][::-1]

    elif a == 90:
        if d == 'clockwise':
            for i in range(column // 2 + 1):
                for j in range(line // 2):
                    M[i][j], M[j][column - 1 - i], M[column - 1 - i][line - 1 - j], M[line - 1 - j][i] = \
                        M[line - 1 - j][i], M[i][j], M[j][column - 1 - i], M[column - 1 - i][line - 1 - j]

        elif d == 'anticlockwise':
            for i in range(column // 2 + 1):
                for j in range(line // 2):
                    M[i][j], M[j][column - 1 - i], M[column - 1 - i][line - 1 - j], M[line - 1 - j][i] = \
                        M[j][column - 1 - i], M[column - 1 - i][line - 1 - j], M[line - 1 - j][i], M[i][j]

    return M

def main():
    mat = [ [ 1, 2, 3, 4, 5], \
            [ 6, 7, 8, 9,10], \
            [11,12,13,14,15], \
            [16,17,18,19,20], \
            [21,22,23,24,25] ]
    rotator(mat,180,"anticlockwise")
    print(mat)
    # should print [ [ 5,10,15,20,25], \
            #        [ 4, 9,14,19,24], \
            #        [ 3, 8,13,18,23], \
            #        [ 2, 7,12,17,22], \
            #        [ 1, 6,11,16,21] ]
    rotator(mat,0,"anticlockwise")
    print(mat)
    # should print [ [ 5,10,15,20,25], \
            #        [ 4, 9,14,19,24], \
            #        [ 3, 8,13,18,23], \
            #        [ 2, 7,12,17,22], \
            #        [ 1, 6,11,16,21] ]


if __name__ == '__main__':
    main()