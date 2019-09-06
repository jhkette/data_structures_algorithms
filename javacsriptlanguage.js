/************* Objects  *******************/

var empty = {}; //empty object

var o = new Object();


// change values
var author = book.author;      // Get the "author" property of the book.
var name = author.surname      // Get the "surname" property of the author.
var title = book["main title"] // Get the "main title" property of the book.

// add values
book.edition = 6;                   // Create an "edition" property of book.
book["main title"] = "ECMAScript";  // Set the "main title" property.

//DELETE
delete book.author;          // The book object now has no author property.
delete book["main title"];   // Now it doesn't have "main title", either.


// Every object has associated prototype, class, and extensible attributes.

// the prototype attribute
/* objects prototpye specifies the object from which it inherits properties. 
The prototype attribute is set when an object is created.

// performssame function as isinstanceof */
isPrototypeOf()

var p = {x:1};                    // Define a prototype object.
var o = Object.create(p);         // Create an object with that prototype.
p.isPrototypeOf(o)                // => true: o inherits from p
Object.prototype.isPrototypeOf(p) // => true: p inherits from Object.prototype


/* the Class Attribute
An object’s class attribute is a string that provides information about the 
type of the object. */



// ***************ARRAYS********************** //

const x = [] //array literal
//Array literals can contain object literals or other array literals: ​ 
var b = [[1,{x:1, y:2}], [2, {x:3, y:4}]];

var a = new Array(10); //This technique creates an array with the specified length.

a = [];              // Start with an empty array
a.push("zero")       // Add a value at the end.  a = ["zero"]
a.push("one", "two") // Add two more values.  a = ["zero", "one", "two"]
a.unshift("minus one") //adds element at beginning
a.shift() //remove elements at beginning
a.pop() //remove element at end

/*METHODS */
// JOIN
var a = [1, 2, 3];     // Create a new array with these three elements
a.join();              // => "1,2,3"
a.join(" ");           // => "1 2 3"
a.join("");            // => "123"
var b = new Array(10); // An array of length 10 with no elements
b.join('-')            // => '---------': a string of 9 hyphens

//REVERSE

var a = [1,2,3];
a.reverse().join()  // => "3,2,1" and a is now [3,2,1]


//sort
/* Array.sort() sorts the elements of an array in place 
and returns the sorted array. When sort() is called with no arguments, 
it sorts the array elements in alphabetical order (temporarily converting them to strings 
to perform the comparison, if necessary):​​ ​  */


var a = new Array("banana", "cherry", "apple");
a.sort();
var s = a.join(", ");  // s == "apple, banana, cherry"


var a = [33, 4, 1111, 222];
a.sort();                 // Alphabetical order:  1111, 222, 33, 4
a.sort(function(a,b) {    // Numerical order: 4, 33, 222, 1111
    return a-b;    // Returns < 0, 0, or > 0, depending on order
});
a.sort(function(a,b) {
    return b-a
});   // Reverse numerical order

// FOREACH()

var data = [1,2,3,4,5];                           // An array to sum
// Compute the sum of the array elements
var sum = 0;                                      // Start at 0
data.forEach(function(value) { sum += value; });

//MAP()

a = [1, 2, 3];
b = a.map(function(x) { return x*x; });  // b is [1, 4, 9]

// FILTER()

a = [5, 4, 3, 2, 1];
smallvalues = a.filter(function(x) { return x < 3 });   // [2, 1]
everyother = a.filter(function(x,i) { return i%2==0 }); // [5, 3, 1] Note that filter() skips missing


// SOME()

// The some() method is like the mathematical “there exists” quantifier ∃: it returns 
// true if there exists at least one element in the array for which the predicate returns 
// true, and returns false if and only if the predicate returns false for all elements of the 
//array:​ ​ 
a = [1,2,3,4,5];
a.some(function(x) { return x%2===0; })  // => true a has some even numbers.
a.some(isNaN)                            // => false: a has no non-numbers.

//REDUCE()

// The reduce() method combine the elements of an array, using the function you 
// specify, to produce a single value. This is a common operation in functional programming 
// and also goes by the names “inject” and “fold.” Examples help illustrate how it works:​​​


var a = [1,2,3,4,5]
var sum = a.reduce(function(x,y) { return x+y }, 0);     // Sum of values
var product = a.reduce(function(x,y) { return x*y }, 1); // Product of values
var max = a.reduce(function(x,y) { return (x>y)?x:y; }); // Largest value


// reduce() takes two arguments. The first is the function that performs the reduction operation. 
// The task of this reduction function is to somehow combine or reduce two values into a single value, 
// and to return that reduced value. In the examples above, the functions combine two values by 
// adding them, multiplying them, and choosing the largest. The second (optional) argument is 
// an initial value to pass to the function. Functions used with reduce() are different than the 
// functions used with forEach() and map(). The familiar value, index, and array values are passed 
// as the second, third, and fourth arguments. The first argument is the accumulated result of the 
// reduction so far. On the first call to the function, this first argument is the initial value you 
// passed as the second argument to reduce(). On subsequent calls, it is the value returned by the 
// previous invocation of the function. In the first example above, the reduction function is first 
// called with arguments 0 and 1. It adds these and returns 1. It is then called again with 
// arguments 1 and 2 and it returns 3. Next it computes 3+3=6, then 6+4=10, and finally 10+5=15. 
// This final value, 15, becomes the return value of reduce(). 
// You may have noticed that the third call to reduce() above has only a single argument: 
// there is no initial value specified. When you invoke reduce() like this with no initial value, 
// it uses the first element of the array as the initial value. This means that the first call to 
// the reduction function will have the first and second array elements as its first and second 
// arguments. In the sum and product examples above, we could have omitted the initial value argument.

