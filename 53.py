def maxSubarray(nums):
    if len(nums) == 1:
        return nums[0]

    sumsMap = {} # {0: [idx(0): ], 1: [idx(0): , idx(1): ], 2: [idx(0): , idx(1): , idx(2): ]}
    sumsMap[0] = [nums[0]] 
    maxSum = nums[0]

    idx = 1 # 1
    while idx < len(nums): # 1 < 9
        sumsMap[idx] = [] # []
        j = 0 # 0
        while j < idx: # 0 < 1
            _sum = sumsMap[idx - 1][j] + nums[idx]
            sumsMap[idx].append(_sum) # [-1]
            maxSum = max(maxSum, _sum)
            # print(sumsMap)
            j += 1
        else:
            sumsMap[idx].append(nums[idx])
            maxSum = max(maxSum, nums[idx])
        idx += 1
    return maxSum

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubarray(nums))