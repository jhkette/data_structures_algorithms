function maxSubArraySum(arr, num){
    let maxSum = 0;
    let tempSum = 0;
    if(arr.length < num) return null;
    for (let i = 0; 1 < num; i++){
        maxSum += arr[i]
    } // get Maxsum - this is the sum of first 'num' indexes
    tempSum = maxSum; // assign tempsum
    for (let i = num; i <arr.length; i++){
        tempSum = tempSum - arr[i - num] + arr[i]; //'slidewindow' - delete last index and add the additional one
        //  this is now tempsum
        maxSum = Math.max(maxSum, tempSum);// maxsum is mathMax of tempsum
    }
    return maxSum
}