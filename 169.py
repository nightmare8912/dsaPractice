def majorityElement(nums):
    # since the question states that for and element to be majority, it needs to appear more than n//2 times
    # so we can take any element and decrement (starting from 1st), and increment the counter whenever we encounter the same element
    # as well as decrementing whenever we see another element, whenever the counter reaches 0, we can update the element with the
    # current element, this way at the end it is guaranteed that at the end we will have the majority element in the element variable
    majElement = nums[0]
    counter = 0
    
    idx = 0
    while idx < len(nums):
        if nums[idx] == majElement:
            counter += 1
        else:
            counter -= 1

        if counter == 0:
            majElement = nums[idx]
            counter = 1

        idx += 1
    return majElement

nums = [2,2,1,1,1,2,2]
print(majorityElement(nums))