def removeElement( nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    i = 0
    j = len(nums)
    print(j) 
    
    while(i<j):
        if nums[i] == val:
            print(str([j-1])+ 'this is j')
            nums[i] = nums[j-1] #swap out with last index in array
            j -= 1
        else:
            i += 1
    return j

print(removeElement([3,2,2,2,2,2,3], 3))