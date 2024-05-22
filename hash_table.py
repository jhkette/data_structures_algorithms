# Given an array of integers, return indices of the two numbers such 
# that they add up to a specific target.

# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.

# Example:

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1]. ie the indexes

# 1. Two Sum

# THE ARRAY IS NOT SORTED - TWO POINTER ARRAY WILL NOT WORK

def two_sum(nums, target):
    dic = {}
    for i, num in enumerate(nums):
        if num in dic:
            return [dic[num], i]
        else:
            dic[target - num] = i
            

print(two_sum([0,2,5,3,6,5], 11))
print(two_sum([0,2,5,3,6,3,4,5,6,9,11,5], 20))



import collections

# A Counter is a container that keeps track of how many times equivalent 
# values are added. It can be used to implement the same algorithms for which 
# bag or multiset data structures are commonly used in other languages.


# find the first uniqe chrecter. collections.counter creates the hash table
# that takes a parameter an creates a dictionary from it. 
def first_unique(s):
    count = collections.Counter(s)
        # find the index
    for idx, ch in enumerate(s):
        if count[ch] == 1:
            return idx     
    return -1

print(first_unique('helloh'))


# Time complexity : 0(n) since we go through the string of length N two times.
# Space complexity 0(n) since we have to keep a hash map with N elements.