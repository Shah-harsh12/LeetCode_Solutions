class Solution {
    public int findPeakElement(int[] nums) {
        int peak = Integer.MIN_VALUE;
        int pointer = 0;
        for(int i = 1; i < nums.length - 1 ; i++){
            if(nums[i] > nums[i+1] && nums[i]>nums[i-1]){
                if(nums[i] > peak){
                    peak = nums[i];
                    pointer = i;
                }
            }
        }
        if(nums[0] > peak){
            peak = nums[0];
            pointer = 0;
        }
        if(nums[nums.length - 1] > peak){
            peak = nums[nums.length - 1];
            pointer = nums.length - 1;
        }
        return pointer;
    }
}