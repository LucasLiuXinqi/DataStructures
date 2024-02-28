def rotate90degree(res):
    """
       This helper function rotates a given matrix 90 degree inplace anticlockwise
    """
    n = len(res)
    for x in range(0, int(n / 2)):
        for y in range(x, n - x - 1):
            tmp = res[x][y]  # Store top. Note: this is O(1) space.
            res[x][y] = res[y][n - 1 - x]  # Move right to top.
            res[y][n - 1 - x] = res[n - 1 - x][n - 1 - y]  # Move bottom to right.
            res[n - 1 - x][n - 1 - y] = res[n - 1 - y][x]  # Move left to bottom.
            res[n - 1 - y][x] = tmp  # Assign top to left.


def rotator(M, a, d):
    """
       This function rotates the square matrix in anti-clockwise.
    """
    # Please write your code here
    if a == 0:
        return M
    cycles = 1
    if d == "clockwise":
        cycles = -1
    cycles *= a // 90
    if cycles < 0:  # Correct cycles if negative
        cycles += 4
    for _ in range(cycles):
        rotate90degree(M)


def main():
    mat = [[1, 2, 3, 4, 5],
           [6, 7, 8, 9, 10],
           [11, 12, 13, 14, 15],
           [16, 17, 18, 19, 20],
           [21, 22, 23, 24, 25]]
    rotator(mat, 90, "anticlockwise")
    print(mat)
    # should print [ [ 5,10,15,20,25],
    #                [ 4, 9,14,19,24],
    #                [ 3, 8,13,18,23],
    #                [ 2, 7,12,17,22],
    #                [ 1, 6,11,16,21] ]
    rotator(mat, 0, "anticlockwise")
    print(mat)
    # should print [ [ 5,10,15,20,25],
    #                [ 4, 9,14,19,24],
    #                [ 3, 8,13,18,23],
    #                [ 2, 7,12,17,22],
    #                [ 1, 6,11,16,21] ]


if __name__ == '__main__':
    main()