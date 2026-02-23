import java.util.*;

class Solution {
    public int singleNumber(int[] nums) {
        Arrays.sort(nums);
        int odd = 0;
        int i = 0;
        while( i != nums.length){
            if(i == nums.length - 1){
                odd = nums[i];
                break;
            }
            if(nums[i] == nums[i + 1]){
                i += 2;
            }
            else{
                odd = nums[i];
                i += 1;
            }
        }
        return odd;
    }
}