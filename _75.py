nums = [2,0,2,1,1,0]

# i, j = 0, 0
# n = len(nums)

# while i < n:
#     j = i + 1
#     while j < n:
#         if nums[i] > nums[j]:
#             nums[i], nums[j] = nums[j], nums[i]
#         j += 1
#     i += 1

# print(nums)



i = 0
n = len(nums)

counter = {
    0: 0, 
    1: 0,
    2: 0,
}

while i < n:
    counter[nums[i]] += 1
    i += 1

# print(counter)

# i = 0
# while i < n:
nums = ([0] * counter[0]) + ([1] * counter[1]) + ([2] * counter[2])
print(nums)