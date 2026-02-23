class Solution {
    public static boolean isPrime(int n) {
        if (n <= 1) {
            return false;
        }

        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) {

                return false;
            }
        }

        return true;
    }
    public int countPrimeSetBits(int left, int right) {
        int count = 0;
        for(int i = left ; i <= right ; i++){
            int n = Integer.bitCount(i);
            boolean Flag = isPrime(n);
            if(Flag){
                count++;
            }
        }
        return count;
    }
}