def knapsack_recursive(weights, values, capacity, n):
    # Please write your code here
    pass
    if capacity == 0 or n == 0:
        return 0

    elif weights[n-1] > capacity:
        return knapsack_recursive(weights, values, capacity, n-1)

    else:
        value_include = values[n-1] + knapsack_recursive(weights, values, capacity-weights[n-1], n-1)

        value_exclude = knapsack_recursive(weights, values, capacity, n-1)

        return max(value_exclude, value_include)



def main():
    weights, values = [1, 3, 4, 5], [1, 4, 5, 7]
    capacity, n = 7, len(weights)
    result = knapsack_recursive(weights, values, capacity, n)
    print(result)  # Output: 9 because of weights four and five with value 5 and 7


if __name__ == '__main__':
    main()
