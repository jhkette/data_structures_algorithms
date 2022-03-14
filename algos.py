# Binary search
def binary_search(arr, elem):
    start = 0
    end = (len(arr) -1)
    middle = round((start + end)//2)
    while(arr[middle] != elem and start <= end):
        if (elem <arr[middle]):
            end = middle -1
        else:
            start = middle + 1
        middle = round(start + end)//2
    if arr[middle] == elem:
        return arr[middle]
    return -1
        
print(binary_search([0,1,2,3,4,5,6,10,12], 10))
print('This is binary search')


# // LEETCODE https://leetcode.com/problems/search-insert-position/
# Given a sorted array and a target value, return the index 
# if the target is found. If not, return the index where it would be 
# if it were inserted in order.

# You may assume no duplicates in the array

def search_insert(nums, target) -> int:
    low, high = 0, len(nums)-1 #find low high
    while low <= high: # low greater than high
        mid = low + (high-low)//2 # get middle
        if nums[mid] < target: # if nums greater than target mid+1
            low = mid+1
        else:
            high = mid-1 # if nums less than target mid-1
    return low # when while loop finishes return low
        
print(search_insert([1,3,5,6], 7))
print('search insert')




# Two pointer technique for finding two sum
# THIS IS THE WAY TO FIND A SUM FROM AN ARRAY -
# USING A TWO POINTER TECHNIQUE
def two_sum(numbers, target):
    n = len(numbers)
    i,j= 0, n-1
    while i < j:
        temp = numbers[i] + numbers[j]
        if temp == target:
            return i,j
        elif temp <target:
            i +=1
        else:
            j -=1
    return []


numbers = [2 ,7 ,11 ,15]  
target = 9
print(two_sum(numbers,target))
print('two pointer technique to find if there is a sum in array')


# https://www.geeksforgeeks.org/find-the-missing-number/
# // get the missing number in an array ie [1,2,3,4,6,7] => 5
def getMissingNo(a):
    n = len(a)
    total = (n+1) *(n+2)//2
    sum_of_A = sum(A)
    return total - sum_of_A

A = [1, 2, 4, 5, 6] 
miss = getMissingNo(A)
print('get misssing number') 
print(miss) 

# Given a sorted array nums, remove the duplicates 
# in-place such that each element appear only once and return the new length.
# Two pointer solution
# looping thourgh checking that n is bigger than preceding index. then moving along array
# now making nums[idx] =n and idx = idx +1
def remove_duplicates(nums):
    idx = 1
    for n in nums[1:]:
        if n > nums[idx-1]:
            nums[idx], idx = n, idx+1
    return idx


arr = [0,0,1,1,1,2,2,3,3,4]
print('this is the duplicates')
print(remove_duplicates(arr))

#check for palindrome
#using two pointer technique
def is_palindrome(s):
    l, r = 0, len(s)-1
    while l < r:
        if not s[l].isalnum(): #check for alnum
            l += 1
        elif not s[r].isalnum(): #check for alnum
            r -= 1
        else:
            if s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1
    return True

print(is_palindrome('madam'))


def is_palindrome_v2(s):
    k = s.strip(" ").lower()
    return k == k[::-1]

is_palindrome_v2('helleh')



#binary search

def search(nums, target) -> int:
    start = 0
    end = len(nums) -1
    while  start <= end:
        middle =  (start + end)// 2
        if nums[middle] == target:
            return middle
        else:
            # if the target is less than the
            #middle the end of search area becomes middle -1
            if  target < nums[middle]:
                end = middle -1
            # if not the search area become middle + 1
            else:
                start = middle + 1
   
    return -1

print(search([0,1,2,3,4,5,6,7], 10))
    
#remove the one index that is not a duplicate in an array
def duplicate_check(nums):
    hash_table ={}
    for i in nums:
        try:
            hash_table.pop(i)
        except:
            hash_table[i] = 1
    return hash_table.popitem()[0]
print('duplicate check')
print(duplicate_check([0,1,0,1,2,3,2]))


# Python code to remove duplicate elements 
def Remove(duplicate): 
    final_list = [] 
    for num in duplicate: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list 
      
# Driver Code 
duplicate = [2, 4, 10, 20, 5, 2, 20, 4] 
print(Remove(duplicate)) 

# Starting from the left every time we find a value that is the target value we swap it out with an item starting from the right. We decrement end each time as we know that the final item is the target value and only increment start once we know the value is ok. Once start 
# reaches end we know all items after that point are the target value so we can stop there.

def removeElement(self, nums, val):
    start, end = 0, len(nums) - 1
    while start <= end:
        if nums[start] == val:
            nums[start], nums[end], end = nums[end], nums[start], end - 1
        else:
            start +=1
    return start

