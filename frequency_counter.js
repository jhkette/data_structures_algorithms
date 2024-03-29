/* write a function same , which accepts two arrays. the function should return 
true if every value in the array has a corrosponding value in squared in the second array. The
frequency of values is the same. ie same ([1,2,1], [4,4,1])
*/

function same(arr1, arr2) {
    if (arr1.length !== arr2.length) {
        return false; // if array is not the same lenght return false 
    }
    let frequencyCounter1 = {} //instantiate objects
    let frequencyCounter2 = {}
    for (let val of arr1) { // for of val in arr1
        frequencyCounter1[val] = (frequencyCounter1[val] || 0) + 1 // add one to value of key
    }
    for (let val of arr2) {
        frequencyCounter2[val] = (frequencyCounter2[val] || 0) + 1 // add one to value of key
    }
    console.log(frequencyCounter1);// console log objects
    console.log(frequencyCounter2);
    for (let key in frequencyCounter1) { // for in frequencyCounter1
        if (!(key ** 2 in frequencyCounter2)) { // check key is in frequency2 by multiplying key value pow 2
            return false;
        }
        if (frequencyCounter1[key] == frequencyCounter2[key ** 2]) { // check if the values are equal ie 
            // if there are 2,2 == 4,4
            return false;
        }
    }
    return true;
}

same([1, 2, 3, 2, 5], [9, 1, 4, 4, 11])
same([1, 2, 3], [1, 4, 9])

function validAnagram(first, second){
    if(first.length !== second.length){
        return false
    }
    const lookup = {}
    for (let val of first){
      lookup[val] ? lookup[val] += 1 : lookup[val] = 1;
    }
    console.log(lookup)
    for(let val of second){
        let letter = val
        if(!lookup[letter]){
            return false
        } else{
            // we need to subtract one as for example
            // there are 3 as - so next time we check - when
            // we get to 0 the prior check will retrun falsey.
            lookup[letter] -=1;
        }
    }
    return true
        
}

validAnagram('anagrams', 'nagarams')

function sameFrequency(num1, num2){
    const number1 = num1.toString()
    const number2 = num2.toString()
    if(number1.length != number2.length){
        return false
    }
    let lookup = {}
    number1.split('').forEach(n => {
        return lookup[n] ? lookup[n] += 1 : lookup[n] =1;

    });
    console.log(lookup)
   
    for(let i of number2.split('')){
        if(!lookup[i]){
            return false
        }else{
            lookup[i] -= 1;
        }
    }
    return true
}
