def max_subarray_sum(nums):
    # Please write your code here
    pass
    if not nums:
        return 0
    current_sum = nums[0]
    max_sum = nums[0]
    prev_sum = nums[0]
    prev_idx = 0

    for i in range(1,len(nums)):
        current_sum += nums[i]
        if i-1 != prev_idx:
            prev_sum += nums[i - 1]

        if current_sum >= max_sum:
            max_sum = current_sum



        if current_sum - prev_sum >= max_sum:
            max_sum = current_sum - prev_sum
            prev_sum = nums[i]
            prev_idx = i
            current_sum = max_sum


    return max_sum


def main():
    nums = [-1, -2, 4, -1, 2, 1]
    result = max_subarray_sum(nums)
    print(result)  # should print 6, based on the subarray [4, -1, 2, 1]


if __name__ == '__main__':
    main()
