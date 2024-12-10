# inp: nums array
# ret: all permutations of nums array

def nextPermutation(nums):
    def getAllPermutations(nums, permutedArray, isElementUsed, allPermutations):

        if all(isElementUsed):
            allPermutations.append(permutedArray.copy())

        for i in range(len(nums)):

            if permutedArray[i] is not None:
                continue

            numToUseIndex = isElementUsed.index(False)
            permutedArray[i] = nums[numToUseIndex]
            isElementUsed[numToUseIndex] = True
            getAllPermutations(nums, permutedArray, isElementUsed, allPermutations)
            permutedArray[i] = None
            isElementUsed[numToUseIndex] = False

    permutedArray = [None] * len(nums)
    isElementUsed = [False] * len(nums)
    allPermutations = []

    getAllPermutations(nums, permutedArray, isElementUsed, allPermutations)
    allPermutations.sort()
    print(allPermutations)

    for i in range(len(allPermutations)):
        if allPermutations[i] == nums and allPermutations[(i + 1) % len(nums)] != nums:
            nums[:] = allPermutations[(i + 1) % len(nums)]
            # print(nums)
            break

nums = [1, 2, 3]
nextPermutation(nums)
print(nums)