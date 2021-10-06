/***
 * multiple pointers
 * creating pointers or values that corrospond to an index or position and move
 * towards the beginning end or middle based on a certain condition
 * 
 * VERY efficient for solving problems
 */


// find a sum that sums to zero from array return false
// if it doesn't
function sumZero(nums){
    i = 0;
    j = nums.length -1
    while(i < j){
        if(nums[i] + nums[j] ==0){
            return [nums[i], nums[j]]
        }else if(nums[i] + nums[j] < 0){
            i++
        }else{
            j --
        }
    }
    return false
}
sumZero([-4,-3,-2,-1,0,1,2,3,4,5,6,10,11])

function countUniqueValues(arr){
    if(arr.length === 0) return 0;
    var i = 0;
    for(var j = 1; j < arr.length; j++){
        if(arr[i] !== arr[j]){
            i++;
            arr[i] = arr[j]
        }
    }
    return i + 1;
}
countUniqueValues([1,2,2,5,7,7,99])