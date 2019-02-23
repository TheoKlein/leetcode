/*
 * @lc app=leetcode id=53 lang=c
 *
 * [53] Maximum Subarray
 *
 * https://leetcode.com/problems/maximum-subarray/description/
 *
 * algorithms
 * Easy (42.69%)
 * Total Accepted:    460K
 * Total Submissions: 1.1M
 * Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
 *
 * Given an integer array nums, find the contiguous subarray (containing at
 * least one number) which has the largest sum and return its sum.
 * 
 * Example:
 * 
 * 
 * Input: [-2,1,-3,4,-1,2,1,-5,4],
 * Output: 6
 * Explanation: [4,-1,2,1] has the largest sum = 6.
 * 
 * 
 * Follow up:
 * 
 * If you have figured out the O(n) solution, try coding another solution using
 * the divide and conquer approach, which is more subtle.
 * 
 */

#ifndef max
    #define max( a, b ) ( ((a) > (b)) ? (a) : (b) )
#endif

int maxSubArray(int* nums, int numsSize) {
    return getMax(nums, 0, numsSize - 1);
}

int getMax(int* nums, int l, int r) {
    if(l == r) return nums[l];

    int m = (l + r) / 2;
    int lMax = getMax(nums, l, m);
    int rMax = getMax(nums, m + 1, r);
    int crossMax = getCrossMax(nums, l, m, r);

    return max(max(lMax, rMax), crossMax);
}

int getCrossMax(int* nums, int l, int m, int r) {
    int lMax = nums[m], lSum = 0;
    int rMax = nums[m + 1], rSum = 0;
    int i = 0;

    for(i = m ; i >= l ; i--) {
        lSum += nums[i];
        lMax = max(lMax, lSum);
    }

    for(i = m + 1 ; i <= r ; i++) {
        rSum += nums[i];
        rMax = max(rMax, rSum);
    }

    return max(max(lMax, rMax), lMax + rMax);
}
