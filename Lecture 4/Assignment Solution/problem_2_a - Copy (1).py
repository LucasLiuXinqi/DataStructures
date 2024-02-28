def intersect(l1, l2):
    """
       This function returns the intersection of lists l1 and l2
    """
    # Please write your code here
    res = []
    i, j = 0, 0
    while i < len(l1) and j < len(l2):
        if l1[i] == l2[j]:
            res += [l1[i]]
            i += 1
            j += 1
        elif l1[i] > l2[j]:
            j += 1
        else:
            i += 1
    return res


def main():
    l1 = [1, 3, 5, 7, 9]
    l2 = [3, 4, 5, 6, 7]

    l = intersect(l1, l2)
    l.sort()
    print(l)  # should print [3,5,7]


if __name__ == '__main__':
    main()