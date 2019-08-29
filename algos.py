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


# Given a sorted array nums, remove the duplicates 
# in-place such that each element appear only once and return the new length.
# Two pointer solution
def remove_duplicates(nums):
    idx = 1
    for n in nums[1:]:
        if n > nums[idx-1]:
            nums[idx], idx = n, idx+1
    return idx


arr = [0,0,1,1,1,2,2,3,3,4]
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
   
    return -1;

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
