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
countUnique([0,0,0,1,1,1,2,2,2,3,3,4])
