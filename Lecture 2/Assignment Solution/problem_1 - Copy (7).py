def max_subarray_sum(nums):
    # Please write your code here
    max_sum = float('-inf')
    current_sum = 0

    for num in nums:
        current_sum += num
        max_sum = max(max_sum, current_sum)
        if current_sum < 0:
            current_sum = 0

    return max_sum


def main():
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result = max_subarray_sum(nums)
    print(result)  # should print 6, based on the subarray [4, -1, 2, 1]


if __name__ == '__main__':
    main()
