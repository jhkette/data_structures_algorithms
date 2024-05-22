 

def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for i, num in enumerate(nums):
            if num in dictionary:
                return [dictionary[num], i]
            else:
                dictionary[target - num] = i

            


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

"""""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""""
def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set()
        for num in nums:
            if num in num_set:
                return True
            else:
                num_set.add(num)
        return False
        

containsDuplicate([1,1,1,3,3,4,3,2,4,2])
