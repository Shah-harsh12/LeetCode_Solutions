public class Solution {
    public int countBinaryPalindromes(long n) {
        if (n == 0) return 1;

        int count = 1; 
        int maxLen = 64 - Long.numberOfLeadingZeros(n);

        for (int len = 1; len < maxLen; len++) {
            if (len == 1) {
                count += 1; 
            } else {
                count += (1 << ((len - 1) / 2));
            }
        }

        int halfLen = (maxLen + 1) / 2;
        long smallestHalf = 1L << (halfLen - 1); 
        long prefix = n >> (maxLen - halfLen);

        long candidate = createPalindrome(prefix, maxLen % 2 == 0);

        if (candidate <= n) {
            count += (int)(prefix - smallestHalf + 1);
        } else {
            count += (int)(prefix - smallestHalf);
        }

        return count;
    }

    private long createPalindrome(long prefix, boolean isEven) {
        long res = prefix;
        long temp = isEven ? prefix : (prefix >> 1);
        while (temp > 0) {
            res = (res << 1) | (temp & 1);
            temp >>= 1;
        }
        return res;
    }
}