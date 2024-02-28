def throw_stones(N, M):
    # Please write your code here
    pass

    sequence = []

    def helper(N, M, D, sub_sequence):
        if N == 0 and M == 0:
            sequence.append(sub_sequence)
            return None

        elif N < 0 or M < 0:
            return None


        if D % 2 == 0:
            helper(N-1, M-1, D+1, sub_sequence + [1])
            helper(N-3, M-1, D+1, sub_sequence + [3])

        else:
            helper(N-1, M-1, D+1, sub_sequence + [1])
            helper(N-2, M-1, D+1, sub_sequence + [2])
            helper(N-3, M-1, D+1, sub_sequence + [3])


    helper(N, M, 1, [])

    return sequence


def main():
    print(throw_stones(5, 3))  # Expect: [(1, 1, 3), (1, 3, 1), (2, 1, 2), (3, 1, 1)] or [[1, 1, 3], [1, 3, 1], [2, 1, 2], [3, 1, 1]]
    print(throw_stones(6, 2))  # Expect: [(3, 3)] or [[3, 3]]


if __name__ == '__main__':
    main()
