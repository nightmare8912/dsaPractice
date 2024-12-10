def rearrangeArray(nums):
    finalList = []
    posP, negP = -1, -1

    while len(finalList) != len(nums):
        nextP, nextN = posP + 1, negP + 1
        idx = nextP
        while idx < len(nums) and nums[idx] < 0:
            idx += 1
        nextP = idx
        idx = nextN
        while idx < len(nums) and nums[idx] > 0:
            idx += 1
        nextN = idx
        finalList.append(nums[nextP])
        finalList.append(nums[nextN])
        posP, negP = nextP, nextN

    return finalList

print(rearrangeArray([-1, 1]))