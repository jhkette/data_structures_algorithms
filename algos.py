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


def is_palindrome_v2(str):
    k = s.strip(" ").lower()
    return k == k[::-1]

is_palindrome_v2('helleh')
