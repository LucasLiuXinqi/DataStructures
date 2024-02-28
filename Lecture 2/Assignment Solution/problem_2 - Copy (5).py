def sort_enchanted_trees(tree_values):
    """
       This function solves f for provided low and high
    """

    # Please write your code here
    for i in range(1, len(tree_values)):
        key = tree_values[i]
        j = i - 1
        while j >= 0 and key < tree_values[j]:
            tree_values[j + 1] = tree_values[j]
            j -= 1
        tree_values[j + 1] = key

    return tree_values


def main():
    tree_values = [30, 20, 40, 10, 50, 15, 35, 25, 45]
    sorted_trees = sort_enchanted_trees(tree_values)
    print(sorted_trees)  # should print [10, 15, 20, 25, 30, 35, 40, 45, 50]


if __name__ == '__main__':
    main()
