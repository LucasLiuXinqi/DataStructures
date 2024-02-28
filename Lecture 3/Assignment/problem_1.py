def deepest(lis):
    """
       This function finds the deepest nested element in a list
    """
    # Please write your code here
    pass

    def deepest_helper(lst):
        state = True
        if type(lst) != list:
            return lst, 0
        else:
            for i in lst:
                if type(i) == list:
                    state = False

            if state is True:
                return lst, 1

            else:
                deepest_lis = None
                max_depth = -1
                for i in lst:
                    deep_i, depth_i = deepest_helper(i)
                    depth_i += 1
                    if depth_i > max_depth:
                        max_depth = depth_i
                        deepest_lis = deep_i

                return deepest_lis, max_depth

    return deepest_helper(lis)[0]


def main():
    l1 = [[[1]]]
    l2 = [1, [2, [3]]]
    l3 = [[[1]], [2], [3]]

    print(deepest(l1))  # should print [1]
    print(deepest(l2))  # should print [3]
    print(deepest(l3))  # should print [1]
    print(deepest([[[2,2]],[[[[4,4,4]]]]]))


if __name__ == '__main__':
    main()
