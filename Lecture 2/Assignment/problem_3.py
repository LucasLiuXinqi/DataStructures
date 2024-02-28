def solver(f, low, high):
    """
       This function solves f for provided low and high
    """

    # Please write your code here
    #### 两端同号, 全段无零点

    pass
    middle = None
    if f(low) == 0:
        return low
    elif f(high) == 0:
        return high

    else:
        for _ in range(1000):
            middle = (low + high) / 2
            f_middle = f(middle)
            if f_middle == 0:
                return middle
            else:
                if f_middle * f(low) > 0:
                    # if f_middle * f(high) > 0:
                    #     return None
                    low = middle
                else:
                    high = middle

    if f(high) * f(middle) > 0 and f(low) * f(middle) > 0:
        return None
    else:
        return round(middle, 2)



def main():
    # f1 = lambda x: x - 1  # f(x) = x - 1
    # f2 = lambda x: x ** 3 - 100 * x ** 2 - x + 100  # f(x) = x^3 - 100x^2 - x + 100
    # f3 = lambda x: 6 * x ** 3 - x ** 2 + 2 * x + 22
    #
    #
    # x = solver(f1, -50, 60)
    # print(x)  # should be one of [1.0]
    #
    # x = solver(f2, 0, 2)
    # print(x)  # should be one of [-1, 1, 100]
    #
    # x = solver(f3, -10, 10)
    # print(x)

    f4 = lambda x: 2**x

    x = solver(f4, -10, 10)
    print(x)

if __name__ == '__main__':
    main()