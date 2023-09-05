

                

// Merges two already sorted arrays
function merge(arr1, arr2){
    let results = []; // new restults array for ordered results
    let i = 0; // i variable
    let j = 0; // j variable
    while(i < arr1.length && j < arr2.length){
        if(arr2[j] > arr1[i]){
            results.push(arr1[i]); // push array i if it is smaller and add i
            i++; // add to i
        } else {
            results.push(arr2[j]) // else push j if it is smaller than i
            j++; // add to j
        }
    }
    while(i < arr1.length) { // add the rest of results i if array length is larger than 
        results.push(arr1[i])
        i++;
    }
    while(j < arr2.length) { // add the rest of results j if it is smaller than j
        results.push(arr2[j]) //
        j++;
    }
    return results;
}

// Recrusive Merge Sort
function mergeSort(arr){
    if(arr.length <= 1) return arr; // when array length is less that one
    let mid = Math.floor(arr.length/2); // mid math - to find mid poiint
    let left = mergeSort(arr.slice(0,mid)); // split left in half again
    let right = mergeSort(arr.slice(mid)); // split right in half again
    return merge(left, right);
}

mergeSort([10,24,76,73])


//O(n log n) complexity