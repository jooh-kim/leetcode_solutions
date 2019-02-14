package

import java.io.*;
import java.lang.Object;
import sun.security.util.Length;

class Solution {
    public static void main(String [] args){
        //int[] arr = {1,4,7,9,5,8};
        //new Solution().twoSum(arr,10);
        new Solution().reverse(321);
    }

    public int[] twoSum(int[] nums, int target){
        /*Given an array of integers, return indices of the two numbers such that they add up to a specific target.
        You may assume that each input would have exactly one solution, and you may not use the same element twice.
        Example:
        Given nums = [2, 7, 11, 15], target = 9,
        Because nums[0] + nums[1] = 2 + 7 = 9,
        return [0, 1].
        */
        //Brute Force method
        int[] sol = new int[2];
        for (int i = 0; i < nums.length ; i++){
            for (int j = 0; j < nums.length; j++){
                if (j != i){
                    if (nums[i] + nums[j] == target){
                        sol[0] = i;
                        sol[1] = j;
                        return sol;
                    }
                }

            }

        }
        return sol;
    }

    public int reverse(int x){
        /*
            Given a 32-bit signed integer, reverse digits of an integer.
        */
        String str1 = Integer.toString(x);
        System.out.println(str1);
        //if (str[0] == '-'){
        return 0;
        //}
    }
}

