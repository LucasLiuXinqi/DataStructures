def solver(f, low, high, loop_times=0):
    """
       This function solves f for provided low and high
    """

    # Please write your code here
    f_low = f(low)
    f_high = f(high)

    if f_low == 0:
        return low
    if f_high == 0:
        return high

    mid = (low + high) / 2
    if high - low <= 0.00001 or loop_times >= 100:
        return round(mid, 2)

    f_mid = f(mid)
    if f_mid == 0:
        return mid

    if f_low * f_mid < 0:
        return solver(f, low, mid, loop_times + 1)
    else:
        return solver(f, mid, high, loop_times + 1)


def solver_2(f, low, high, limit=100):
    """
       This function solves f for provided low and high without using recursion
    """

    # Please write your code here
    mid = (low + high) / 2
    function_mid = f(mid)
    step = 0
    while abs(function_mid) > 0.0001 and step < limit:
        if function_mid * f(low) >= 0:
            low = mid
        else:
            high = mid
        mid = (low + high) / 2
        function_mid = f(mid)
        step += 1

    return round(mid, 2)


def main():
    f1 = lambda x: x ** 3 - 100 * x ** 2 - x + 100  # f(x) = x^3 - 100x^2 - x + 100
    f2 = lambda x: 6 * x ** 3 - x ** 2 + 2 * x + 22  # f(x) = 6x^3 - x^2 + 2x + 22
    f3 = lambda x: x - 1  # f(x) = x - 1
    f4 = lambda x: 2 * x + 3  # f(x) = 2x + 3
    f5 = lambda x: x + 100  # f(x) = x + 100

    x = solver(f1, 0, 2)
    print(x)  # should be one of [-1, 1, 100]

    x = solver(f2, -2, 0)
    print(x)  # should be one of [-1.42]

    x = solver(f3, -50, 60)
    print(x)  # should be one of [1.0]

    x = solver(f4, -2, 0)
    print(x)  # should be one of [-1.5]

    x = solver(f5, -100, 100)
    print(x)  # should be one of [-100]


if __name__ == '__main__':
    main()
