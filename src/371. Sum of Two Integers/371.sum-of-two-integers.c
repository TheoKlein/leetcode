/*
 * @lc app=leetcode id=371 lang=c
 *
 * [371] Sum of Two Integers
 *
 * https://leetcode.com/problems/sum-of-two-integers/description/
 *
 * algorithms
 * Easy (50.97%)
 * Total Accepted:    132.6K
 * Total Submissions: 260.1K
 * Testcase Example:  '1\n2'
 *
 * Calculate the sum of two integers a and b, but you are not allowed to use
 * the operator + and -.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: a = 1, b = 2
 * Output: 3
 * 
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: a = -2, b = 3
 * Output: 1
 * 
 * 
 * 
 * 
 */


int getSum(int a, int b){
    int carry = 0;
    while(b){
        carry = a & b;
        a = a ^ b;
        b = (carry & 0xffffffff) << 1;
    }
    return a;
}



