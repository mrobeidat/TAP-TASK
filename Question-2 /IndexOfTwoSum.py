def idxOfTwoSum(nums, target):
    num_arr = {}

    for i in range(len(nums)):
        sum = target - nums[i]

        if sum in num_arr:
            return [num_arr[sum], i]

        num_arr[nums[i]] = i

    return []
