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


# Given an input string, reverse the string word by word.
# Example 1:

# Input: "the sky is blue"
# Output: "blue is sky the"

def reverseWords(s):
    return " ".join(s.strip().split()[::-1])

# DOne without strip, join, split etc
# @param s, a string
# @return a string
def reverseWords(s):
    # First reverse entire string, then iterate over reversed string
    # and again reverse order of characters within a word. Append each word to words.
    word = ""
    words = ""
    s = s[::-1]
    for j, i in enumerate(s):
        # character is not space, a current word exists, 
        # and previous character is space, e.g. i=b in " a b":
        if i != " " and word != "" and s[j-1] == " ":
            # add current word to words and append " " to later add this i
            words += (word + " ")
            word = i
        # character is not space, but it's either first character in string
        # or is part of current word, e.g. i=b in "b", " b" "ab", "a ab "
        elif i != " ":
            word = i + word
        else:
            continue

    words += word
    
    return(words)

# Write a function that reverses a string. 
# The input string is given as an array of characters char[].

# Do not allocate extra space for another array, you must do this 
# by modifying the input array in-place with O(1) extra memory.

# Example 1:

# Input: ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

def reverse_string (s):
    """
    Do not return anything, modify s in-place instead.
    """
    left = 0        # left index border
    right = len(s)-1        # right index border
    while(left < right):        # as long as left and right don't meet
        s[left], s[right] = s[right], s[left]       # exchange both elements
        left += 1       # move left index to the right
        right -= 1      # move right index to the left
    return s


# // majority element
# // Given an array of size n, find the majority element. 
# // The majority element is the element that appears more than ⌊ n/2 ⌋ times.

# // You may assume that the array is non-empty and the majority 
# // element always exist in the array.

# // Example 1:

# // Input: [3,2,3]
# // Output: 3


def majorityElement(nums) -> int:
    obj = {}
    for n in nums:
        if n in obj:
            obj[n] += 1
        else:
            obj[n] = 1
            
    return max(obj, key=obj.get) #nb other way below actually better for specific question
    # as it anwser will be half of array. This method good for finding largest num in object


def majorityElement2(nums) -> int:
    obj = {}
    for n in nums:
        if n in obj:
            obj[n] += 1
        else:
            obj[n] = 1
            
    for k,v in obj.items():
        if v > len(nums)//2:
            return k

print(majorityElement2([2,2,1,1,1,2,2]))


# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".
# Otherwise, we define that this word doesn't use capitals in a right way.



#  Example 1:

# Input: "USA"
# Output: True
 

# Example 2:

# Input: "FlaG"
# Output: False

def detectCapitalUse(word):
    """
    :type word: str
    :rtype: bool
    """
    if word.lower()==word or word.upper()==word:
        return True
    elif word[0].lower()!=word[0] and word[1:].lower()==word[1:]:
        return True
    else:
        return False
print(detectCapitalUse('USA'))


""""
Sell stock problem
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
"""""
def max_profit(prices: list[int])->int:
    l,r = 0,1 #left = buy, right = sell
    maxP = 0

    while r < len(prices): # while r is less than the length of prices
        if prices[l] < prices[r]: #if there is a profit
            # calculate proft
            profit = prices[r] - prices[l] #calc proftit
            maxP = max(maxP, profit) #get the max
        else:
            l =r #if prices isn't greater move the left pointer
        r+=1
    return maxP


prices = [7,1,5,3,6,4]
print(max_profit(prices)) # should be 5