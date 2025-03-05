// Description: My implementation for the solution for the Counter II problem on leetcode
// Problem : Write a function createCounter. It should accept an initial integer init. It should return an object with three functions.
//          The three functions are:
//          increment() increases the current value by 1 and then returns it.
//          decrement() reduces the current value by 1 and then returns it.
//          reset() sets the current value to init and then returns it.
// Difficulty: easy
// Author: Elbert C.

/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let resetVal = init;
    return {
        increment: () => {
            return init += 1;
        },
        decrement: () => {
            return init -= 1;
        },
        reset: () => {
            init = resetVal;
            return init;
        },
    }
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */