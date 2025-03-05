// Description: My implementation for the solution for the Create Hello World Function problem on leetcode
// Problem : Write a function createHelloWorld. It should return a new function that always returns "Hello World".
// Difficulty: easy
// Author: Elbert C.

/**
 * @return {Function}
 */
var createHelloWorld = function() {
    
    return function(...args) {
        return "Hello World"
    }
};

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */