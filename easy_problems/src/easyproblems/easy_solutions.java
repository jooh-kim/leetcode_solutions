package easyproblems;

import java.lang.Integer;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class easy_solution {
    public static void main(String[] args) {

        easy_solution var1 = new easy_solution();

        // twoSum Problem
        /*
        int[] arr = {1,4,7,9,5,8};
        int[] ans;
        ans = var1.twoSum(arr,10);
        System.out.println(Arrays.toString(ans));
        */

        //int rel = var1.reverse(-123);
        //boolean result = var1.isPalindrome(10);
        //System.out.println(result);
        String[] strs = {"flower","flow","flight"};
        var1.longestCommonPrefix(strs);
    }

    public int[] twoSum(int[] nums, int target) {
        /*Given an array of integers, return indices of the two numbers such that they add up to a specific target.
        You may assume that each input would have exactly one solution, and you may not use the same element twice.
        Example:
        Given nums = [2, 7, 11, 15], target = 9,
        Because nums[0] + nums[1] = 2 + 7 = 9,
        return [0, 1].
        */
        //Brute Force method
        int[] sol = new int[2];
        for (int i = 0; i < nums.length; i++) {
            for (int j = 0; j < nums.length; j++) {
                if (j != i) {
                    if (nums[i] + nums[j] == target) {
                        sol[0] = i;
                        sol[1] = j;
                        return sol;
                    }
                }

            }

        }
        return sol;
    }

    public int reverse(int x) {
        /*
            Given a 32-bit signed integer, reverse digits of an integer.
            Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1].
            For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
        */
        try {
            //convert int to string
            String str1 = Integer.toString(x);

            //reverse the string (char array)
            char[] numchar = str1.toCharArray();
            int numlength = numchar.length;
            //check if neg or not
            int i;
            if (numchar[0] == '-') {
                numlength = numlength-1;
                i = 1;
            }
            else
                i = 0;

            double a = Math.ceil(((double)(numlength)/2));
            System.out.printf("a%f",a);
            int limit = (int)a;
            System.out.println(limit);
            for (; i < a; i++) {
                System.out.println(i);
                System.out.println(numchar[i]);
                char temp = numchar[i];
                numchar[i] = numchar[numlength - 1 - i];
                numchar[numlength - 1 - i] = temp;
            }
            //convert char array to string
            str1 = new String(numchar);
            System.out.println(str1);
            Integer result = Integer.parseInt(str1);

            if (result < -2147483648 || result > 2147483647) {
                return 0;
            } else
                return result;
        } catch (NumberFormatException ex) {
            return 0;
        }
    }

    public boolean isPalindrome(int x) {
        /*
        * Determine whether an integer is a palindrome.
        * An integer is a palindrome when it reads the same backward as forward.
        * */
        if (x < 0)
            return false;
        else{
            List<Integer> lst = new ArrayList<Integer>();
            //turn x into int array
            while (x > 0){
                int val = x%10;
                lst.add(val);
                x = x / 10;
            }
            //check palindrome
            for (int i = 0;i < lst.size()/2; i++){
                if(lst.get(i) != lst.get(lst.size()-i-1))
                    return false;
            }
            return true;
        }

    }

    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {

        //initialize result listnode
        ListNode head = new ListNode(0);
        head.next = null;


        while(l1 != null && l2 != null){
            if(l1.val >= l2.val){
                head.next = l1;
                l1 = l1.next;
            }
            else{
                head.next = l2;
                l2 = l2.next;
            }
        }
        if (l1 != null){
            head.next = l1;
        }
        else if (l2 != null){
            head.next = l2;
        }

        return head.next;
    }
}

class ListNode {
    int val;
    ListNode next;

    //Constructor
    ListNode(int x) { val = x; }
}

