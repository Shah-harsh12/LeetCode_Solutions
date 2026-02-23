/**
 * // This is MountainArray's API interface.
 * // You should not implement it, or speculate about its implementation
 * interface MountainArray {
 *     public int get(int index) {}
 *     public int length() {}
 * }
 */
 
class Solution {
    public int findInMountainArray(int target, MountainArray mountainArr) {
        int n = mountainArr.length();
        
        // 1. Find the Peak Index (O(log n))
        int low = 0, high = n - 1;
        while (low < high) {
            int mid = low + (high - low) / 2;
            if (mountainArr.get(mid) < mountainArr.get(mid + 1)) {
                low = mid + 1;
            } else {
                high = mid;
            }
        }
        int peak = low;

        int res = binarySearch(mountainArr, target, 0, peak, true);
        if (res != -1) return res;

        return binarySearch(mountainArr, target, peak + 1, n - 1, false);
    }

    private int binarySearch(MountainArray mountainArr, int target, int low, int high, boolean isIncreasing) {
        while (low <= high) {
            int mid = low + (high - low) / 2;
            int midVal = mountainArr.get(mid);
            if (midVal == target) return mid;

            if (isIncreasing) {
                if (midVal < target) low = mid + 1;
                else high = mid - 1;
            } else {
                if (midVal > target) low = mid + 1;
                else high = mid - 1;
            }
        }
        return -1;
    }
}