// Optimized BubbleSort with noSwaps
function bubbleSort(arr){
   
    var noSwaps; // bubble sort optimisation - if there are no swaps - se set

    for(var i = arr.length; i > 0; i--){ // we do i-- because we want to shrink the number of comparisaons
        // once we have looped through once '8' will be at the end - so we don't need to check again. 
      noSwaps = true;
      for(var j = 0; j < i - 1; j++){
        if(arr[j] > arr[j+1]){ // compare j to J+1
          var temp = arr[j]; // assign temp
          arr[j] = arr[j+1]; // SWAP
          arr[j+1] = temp; // reassign temp
          noSwaps = false;   // we have swapped so no swaps is false       
        }
      }
      if(noSwaps) break; // if swaps is true break out of the loop to stop unnessary loops
    }
    return arr;
  }
  
  bubbleSort([8,1,2,3,4,5,6,7]);