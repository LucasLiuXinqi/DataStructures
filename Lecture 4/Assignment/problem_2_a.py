def intersect(l1, l2):
    """
       This function returns the intersection of lists l1 and l2
    """
    # Please write your code here
    len_1 = len(l1)
    len_2 = len(l2)
    current_position = 0
    target_position = 0
    intersection = []
    while current_position < len_1 and target_position < len_2:
        if l1[current_position] < l2[target_position]:
            current_position += 1

        elif l1[current_position] == l2[target_position]:
            intersection.append(l1[current_position])
            current_position += 1
            target_position += 1

        elif l1[current_position] > l2[target_position]:
            target_position += 1

    return intersection


def main():
    l1 = [1, 3, 5, 7, 9]
    l2 = [3, 4, 5, 6, 7]

    l = intersect(l1, l2)
    l.sort()
    print(l)  # should print [3, 5, 7]


if __name__ == '__main__':
    main()
