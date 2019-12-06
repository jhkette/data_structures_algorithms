function maxSubArraySum(arr, num){
    let maxSum = 0;
    let tempSum = 0;
    if(arr.length < num) return null;
    for (let i = 0; i < num; i++){
        maxSum += arr[i] // get Maxsum - this is the sum of first 'num' indexes
    } 
    tempSum = maxSum; // assign tempsum
    for (let i = num; i <arr.length; i++){
        tempSum = tempSum - arr[i - num] + arr[i]; //'slidewindow' - delete last index and 
        // add the additional one
        //  this is now tempsum
        maxSum = Math.max(maxSum, tempSum);// maxsum is mathMax of tempsum
    }
    return maxSum
}

maxSubarraySum([2,6,9,2,1,8,5,6,3],3)

function findMaxAverage(nums, k){
    let maxSum = 0;
    let tempSum = 0;
    if(nums.length < k) return null;
    for(let i = 0; i < k; i++){
        maxSum += nums[i]
    }
    tempSum = maxSum;
    for (let i = k; i < nums.length; i++ ){
        tempSum = tempSum - nums[i - k] + nums[i];
        maxSum = Math.max(maxSum, tempSum)
    }
    return maxSum / k;
}

findMaxAverage([2,6,9,2,1,8,5,6,3],3)