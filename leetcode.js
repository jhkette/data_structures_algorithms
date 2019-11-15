// Write a function that reverses a string. The input string 
// is given as an array of characters char[].

// Do not allocate extra space for another array, you must do this by modifying 
// the input array in-place with O(1) extra memory.
// @param s - an array of characters
function reverseString(s){
    var i = 0,
    n = s.length,
    middle = Math.floor(n / 2),
    temp = null;

    for (; i < middle; i += 1) {
        temp = s[i];
        s[i] = s[n - 1 - i];
        s[n - 1 - i] = temp;
    }
    return s
}

// Find the middle of the array. Then, you find the index which is symmetric to the 
//current index relative  to the middle, using the formula n - 1 - i, where i 
//is the current index. Then you swap the elements using a temp variable. 
// The formula is correct, because 
// it will swap:

//     0 <-> n - 1
//     1 <-> n - 2

function reverseString2(s){
    return s.reverse
}

// majority element
// Given an array of size n, find the majority element. 
// The majority element is the element that appears more than ⌊ n/2 ⌋ times.

// You may assume that the array is non-empty and the majority 
// element always exist in the array.

// Example 1:

// Input: [3,2,3]
// Output: 3

/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    const hash = {};
    for(i = 0; i < nums.length; i++){
        if(hash[nums[i]]){
            hash[nums[i]] += 1
        }else{
            hash[nums[i]] =1
        }
         
    }
    return Object.keys(hash).reduce((a, b) => hash[a] > hash[b] ? a : b); 
};

majorityElement([2,2,1,1,1,2,2])


// Given a word, you need to judge whether the usage of capitals in it is right or not.

// We define the usage of capitals in a word to be right when one of the following cases
// holds:

// All letters in this word are capitals, like "USA".
// All letters in this word are not capitals, like "leetcode".
// Only the first letter in this word is capital, like "Google".
// Otherwise, we define that this word doesn't use capitals in a right way.



// Example 1:

// Input: "USA"
// Output: True
 

// Example 2:

// Input: "FlaG"
// Output: False


var detectCapitalUse = function(word) {
    // either all capitals, all small cases, or Capital follow by small cases
    return /^[A-Z]+$|^[a-z]+$|^[A-Z][a-z]+$/.test(word);
};

// or

var detectCapitalUse = function(word) {
    return word === word.toUpperCase() || word === word[0] + word.substr(1).toLowerCase();
};