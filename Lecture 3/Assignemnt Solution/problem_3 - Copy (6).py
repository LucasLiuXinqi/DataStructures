def unique(lis):
    # Please write your code here
    def helper(start, end):
        if start >= end:
            return True
        if lis[start] in lis[start+1:end]:
            return False
        return helper(start+1, end)

    return helper(0, len(lis))


def main():
    print(unique([1, 54, 3, 25, 39, 25, 2]))  # should print False
    print(unique([9, "a", [], [[35, 2], ["NYU"]], (100,)]))  # should print True


if __name__ == '__main__':
    main()
