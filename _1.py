nums = [2,7,11,15]
target = 9

hsh_map = {}

"""

  [2,7,11,15]

  n = len(nums)
  
  nums.sort()
  start, end = 0, n-1

  while start < end:
    if nums[start] + nums[end] == target:
      return [start, end]

    elif nums[start] + nums[end] < target:
      end -= 1

    else:
      start += 1

"""