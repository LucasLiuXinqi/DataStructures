def unique(lis):
    # Please write your code here
    pass
    if len(lis) == 0:
        return True

    else:
        element = lis[0]
        lis.pop(0)
        return (help_unique(element, lis, 0) and unique(lis))


def help_unique(element, sub_list, index):
    if index == len(sub_list):
        return True
    else:
        return not(element == sub_list[index]) and help_unique(element, sub_list, index + 1)


def main():
    print(unique([1, 54, 3, 25, 39, 25, 2]))  # should print False
    print(unique([9, "a", [], [[35, 2], ["NYU"]], (100,)]))  # should print True


if __name__ == '__main__':
    main()
