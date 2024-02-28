def union(l1, l2):
    """
       This function returns the union of lists l1 and l2
    """
    # Please write your code here
    len_1 = len(l1)
    len_2 = len(l2)
    current_position = 0
    target_position = 0
    uni = []

    while current_position < len_1 and target_position < len_2:
        if l1[current_position] < l2[target_position]:
            uni.append(l1[current_position])
            current_position += 1

        elif l1[current_position] == l2[target_position]:
            uni.append(l1[current_position])
            current_position += 1
            target_position += 1

        elif l1[current_position] > l2[target_position]:
            uni.append(l2[target_position])
            target_position += 1

    if current_position < len_1:
        uni += l1[current_position:]

    if target_position < len_2:
        uni += l2[target_position:]


    return uni


def main():
    l1 = [1, 3, 5, 7, 9]
    l2 = [3, 4, 5, 6, 7]

    l = union(l1, l2)
    #l.sort()
    print(l)  # should print [1, 3, 4, 5, 6, 7, 9]


if __name__ == '__main__':
    main()