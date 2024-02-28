def throw_stones(N, M):
    # Please write your code here
    return stone_counter(N, M, 1, [], [])


def stone_counter(N, M, c, res, total):
    if c > M:
        if N == 0:
            total.append(tuple(res))
    elif c % 2 == 0:
        temp = res[:]
        res.append(1)
        temp.append(3)
        stone_counter(N - 1, M, c + 1, res, total)
        stone_counter(N - 3, M, c + 1, temp, total)
    else:
        temp = res[:]
        temp1 = res[:]
        res.append(1)
        temp.append(2)
        temp1.append(3)
        stone_counter(N - 1, M, c + 1, res, total)
        stone_counter(N - 2, M, c + 1, temp, total)
        stone_counter(N - 3, M, c + 1, temp1, total)
    return total


def main():
    print(throw_stones(5, 3))  # Expect: [(1, 1, 3), (1, 3, 1), (2, 1, 2), (3, 1, 1)] or [[1, 1, 3], [1, 3, 1], [2, 1, 2], [3, 1, 1]]
    print(throw_stones(6, 2))  # Expect: [(3, 3)] or [[3, 3]]


if __name__ == '__main__':
    main()
