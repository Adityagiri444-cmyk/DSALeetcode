class Solution {

    public boolean isPalindrome(int x) {

        int originalNum = x;
        int reverseNum = 0;

        if (x < 0) {
            return false;
        }

        while (x > 0) {
            int digit = x % 10;
            reverseNum = reverseNum * 10 + digit;
            x = x / 10;
        }

        return originalNum == reverseNum;
    }

    public static void main(String[] args) {

        Solution obj = new Solution();

        boolean ans = obj.isPalindrome(121);

        System.out.println(ans);
    }
}