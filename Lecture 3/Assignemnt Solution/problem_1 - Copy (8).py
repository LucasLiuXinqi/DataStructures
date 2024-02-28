def deepest(lis):
    """
       This function finds the deepest nested element in a list
    """
    # Please write your code here
    _, deepest_list = deepest_helper(lis)
    return deepest_list


def deepest_helper(lis):
    depth, deepest_list = 0, []
    signal = False
    for item in lis:
        if type(item) == list:
            signal = True
            _depth, _deepest_list = deepest_helper(item)
            _depth += 1
            if _depth > depth:
                depth, deepest_list = _depth, _deepest_list
    if not signal:
        return depth, lis
    return depth, deepest_list


def main():
    l1 = [[[1, 2]]]
    l2 = [1, [2, [3]]]
    l3 = [[[1]], [2], [3]]

    print(deepest(l1))  # should print [1, 2]
    print(deepest(l2))  # should print [3]
    print(deepest(l3))  # should print [1]


if __name__ == '__main__':
    main()
