def union(l1, l2):
    """
       This function returns the union of lists l1 and l2
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
            res += [l2[j]]
            j += 1
        else:
            res += [l1[i]]
            i += 1

    if i < len(l1):
        res += l1[i:]
    else:
        res += l2[j:]

    return res


def main():
    l1 = [1, 3, 5, 7, 9]
    l2 = [3, 4, 5, 6, 7]

    l = union(l1, l2)
    l.sort()
    print(l)  # should print [1,3,4,5,6,7,9]


if __name__ == '__main__':
    main()