var maxSubArray = function(nums) {
    let len = nums.length;
    if (len === 0) return 0;
    let max = nums[0];
    for (let i = 1; i < len; i++) {
        nums[i] = Math.max(nums[i]+nums[i-1],nums[i]);
        if (nums[i] > max) {
            max = nums[i];  
        }
    }
    return max;
};