// Description: My implementation for the solution for the Apply Transform Over Each Element in Array problem on leetcode
// Problem : Given an integer array arr and a mapping function fn, return a new array with a transformation applied to each element.
//          The returned array should be created such that returnedArray[i] = fn(arr[i], i).
//          Please solve it without the built-in Array.map method.
// Difficulty: easy
// Author: Elbert C.

/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    const transformedArr = [];
    let i = 0;
    for (const element of arr) {
        transformedArr[i] = fn(element, i);
        i++;
    }
    return transformedArr
};