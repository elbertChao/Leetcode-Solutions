// Description: My implementation for the solution for the Counter problem on leetcode
// Problem : Given an integer n, return a counter function. This counter function initially
//           returns n and then returns 1 more than the previous value every subsequent time it is called (n, n + 1, n + 2, etc).
// Difficulty: easy
// Author: Elbert C.

/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
    let count = 0
    return function() {
        return n + (count++);
    };
};

/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */