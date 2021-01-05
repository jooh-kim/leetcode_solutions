import math
import sys
import collections

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

""" 
TO-DO List
Fix and Finish
    - 134
    
Update
    - 2 - #Try to solve with recusion later

"""


""" 
Problem: Movies On Flight - From Discussion

You are on a flight and wanna watch two movies during this flight.
You are given List<Integer> movieDurations which includes all the movie durations.
You are also given the duration of the flight which is d in minutes.
Now, you need to pick two movies and the total duration of the two movies is less than or equal to (d - 30min).

Find the pair of movies with the longest total duration and return they indexes. If multiple found, return the pair with the longest movie.

Input: movieDurations = [90, 85, 75, 60, 120, 150, 125], d = 250
Output: [0, 6]
"""
def moviesOnFlight(movies, d):
    d -= 30
    if len(movies) < 2:
        return None
    if len(movies) == 2:
        return [0,1]

    movies_sorted = movies[:]
    movies_sorted.sort()
    i = 0
    j = 0
    left = 0
    right = len(movies) - 1
    max_duration = 0
    while left < right:
        cur = movies_sorted[left] + movies_sorted[right]
        if cur <= d:
            if cur > max_duration:
                max_duration = cur
                i = left
                j = right
                left += 1
            else:
                right -= 1
        else:
            left += 1
    
    return [movies.index(movies_sorted[i]),movies.index(movies_sorted[j])]    

""" 
Problem: Treasure Island 1 - From Discussion

Assume the map area is a two dimensional grid, represented by a matrix of characters. 
You must start from the top-left corner of the map and can move one block up, down, left or right at a time. 
The treasure island is marked as X in a block of the matrix. X will not be at the top-left corner. 
Any block with dangerous rocks or reefs will be marked as D. You must not enter dangerous blocks. 
You cannot leave the map area. Other areas O are safe to sail in. The top-left corner is always safe. 
Output the minimum number of steps to get to the treasure.

Input:
[['O', 'O', 'O', 'O'],
 ['D', 'O', 'D', 'O'],
 ['O', 'O', 'O', 'O'],
 ['X', 'D', 'D', 'O']]

Output: 5
"""
def treasureIslandOne(graph):
    # BFS solution

    if graph == None or len(graph) == 0:
        return 0
    min_steps = 0

    queue = []
    visited = []

    rows = len(graph)
    cols = len(graph[0])
    i = 0
    # Turn 'O' into Coordinates
    for row in graph:
        j = 0
        for col in row:
            if col == 'O':
                graph[i][j] = (i,j)
            j+=1
        i+=1
    
    visited.append(graph[0][0])
    directions = [(1,0), (0,1), (-1,0), (0,-1)]
    queue.append(graph[0][0])

    while queue != []:
        queue_size = len(queue)
        i = 0
        while i < queue_size:
            cur_state = queue.pop(0)
            if cur_state == 'X':
                return min_steps
            for dir in directions:
                next_x = cur_state[0] + dir[0]
                next_y = cur_state[1] + dir[1]
                # next_state = graph[next_x][next_y]
                
                if next_x >= 0 and next_x < rows and next_y >= 0 and next_y < cols and graph[next_x][next_y] != 'D' and graph[next_x][next_y] not in visited:
                    next_state = graph[next_x][next_y]
                    queue.append(next_state)
                    visited.append(next_state)
            
            i+=1
        min_steps +=1
    return 0

"""  
20 Valid Parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
"""
def isValid(s):
    
    stack = []
    paren_mapping = {")":'(', ']':'[', '}':'{'}

    for char in s:
        #closing parentheses
        if char in paren_mapping:
            top_elem = stack.pop() if stack else '#'
            if top_elem != paren_mapping[char]:
                return False
        #opening parentheses
        else:
            stack.append(char)

    if stack == []:
        return True
    else:
        return False

"""  
53 - Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""
def maxSubArray(nums):
        max_global = nums[0]
        max_soFar = 0
        i = 0
        while i < len(nums):
            max_soFar = max(nums[i],max_soFar + nums[i])
            if max_soFar > max_global:
                max_global = max_soFar
            i += 1
        return max_global

""" 
49 - Group Anagrams    

Given an array of strings, group anagrams together.

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
"""
def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """

    """
    My thought process:
        1. I can sort the words so that if two words are anagrams, they will have the same order.
        2. create a dictionary with the sorted word as a key, any that match include it in.
    """
    anagram_dict = dict()
    i = 0
    while i < len(strs):
        word = ''.join(sorted(strs[i]))
        if word not in anagram_dict:
            # anagramed word not in dict
            anagram_dict[word] = [strs[i]]
        else:
            # anagramed word in dict, search the list
            lst = anagram_dict[word]
            # if strs[i] not in anagram_dict[word]:
            anagram_dict[word].append(strs[i])
        i+=1
    result = []
    for key in anagram_dict:
        result.append(anagram_dict[key])
    print(result)

"""  
134 - Gas Station

There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). 
You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.

Note:

If there exists a solution, it is guaranteed to be unique.
Both input arrays are non-empty and have the same length.
Each element in the input arrays is a non-negative integer.
"""
def canCompleteCircuit(gas, cost):
    """
    :type gas: List[int]
    :type cost: List[int]
    :rtype: int
    """
    if (sum(gas) - sum(cost)) < 0:
        return -1
    else:
        i = 0
        while i < len(gas):
            if gas[i] > cost[i]:
                return i
            i+=1
        return i

""" 
2 - Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""
def addTwoNumbers(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    result_head = ListNode(0)
    temp = result_head
    carryover = 0
    # remainder = 0
    while l1 != None and l2 != None:
        cur_sum = l1.val + l2.val + carryover
        if cur_sum > 9:
            cur_sum = cur_sum % 10
            carryover = 1
        else:
            carryover = 0
        temp.next = ListNode(cur_sum)
        temp = temp.next
        l1 = l1.next
        l2 = l2.next
    
    if l1 == None and l2 != None:
        while l2 != None:
            cur_sum = l2.val + carryover
            if cur_sum > 9:
                cur_sum = cur_sum % 10
                carryover = 1
            else:
                carryover = 0
            temp.next = ListNode(cur_sum)
            temp = temp.next
            l2 = l2.next
    elif l1 != None and l2 == None:
        while l1 != None:
            cur_sum = l1.val + carryover
            if cur_sum > 9:
                cur_sum = cur_sum % 10
                carryover = 1
            else:
                carryover = 0
            temp.next = ListNode(cur_sum)
            temp = temp.next
            l1 = l1.next
    
    return result_head.next

""" 
3 - Longest Substring Without Repeating Characters  

Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
"""
def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    sub_dict = {}
    max_cur = ""
    max_so_far = ""
    i = 0

    while i < len(s):
        if s[i] not in sub_dict:
            sub_dict[s[i]] = i
            max_cur = max_cur + s[i]
        else:
            # letter in dict, so new index is the index after the initial duplicate
            i = sub_dict[s[i]] + 1
            sub_dict.clear()

            max_cur = s[i]
            sub_dict[s[i]] = i
        if len(max_cur) >= len(max_so_far):
                max_so_far = max_cur
        i+=1
            
    return len(max_so_far)

def lengthOfLongestSubstring2(s):
    dicts = {}
    maxlength = start = 0
    for i,value in enumerate(s):
        if value in dicts:
            sums = dicts[value] + 1
            if sums > start:
                start = sums
        num = i - start + 1
        if num > maxlength:
            maxlength = num
        dicts[value] = i
    return maxlength


""" 
if input array is {1, 2, 3, 4} and r is 2, 
then output should be {1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4} and {3, 4}.
"""
def allPossibleComb(arr, r):
    if r > len(arr):
        print("Wrong input, r is greater than arr")
        return 0

    # current combination
    result = [0]*r
    allPossibleCombHelper(arr, result, 0, len(arr)-1, 0, r)

def allPossibleCombHelper(arr, result, start, end, index, r):
    # current result is full, print
    if index == r:
        print(result)
        return
    i = start
    while i <= end and end - i + 1 >= r - index:
        result[index] = arr[i]
        allPossibleCombHelper(arr, result, start+1, end, index+1, r)
        i+=1

i = 0


""" 
5 - Longest Palindromic Substring    

Given a string s, find the longest palindromic substring in s. 
You may assume that the maximum length of s is 1000.
"""
def longestPalindrome(s):
    """
    :type s: str
    :rtype: str

    Input: "babad"
    Output: "bab"
    Note: "aba" is also a valid answer.
    """
    start_index = 0
    end_index = 0
    max_len = 0
    if s == "":
        return ""
    elif len(s) == 1:
        return s[0]
    for index in range(len(s)-1):
        len1, x1, y1 = longestPalindrome_Helper(s,index,index)
        len2, x2, y2 = longestPalindrome_Helper(s,index,index+1)
        if len1 > len2 and len1 > max_len:
            max_len = len1
            start_index = x1
            end_index = y1
        elif len2 > len1 and len2 > max_len:
            max_len = len2
            start_index = x2
            end_index = y2
    answer = s[start_index:end_index+1]
    return answer

    
def longestPalindrome_Helper(s,start,end):
    if s[start] != s[end]:
        return 0, start, end
    while start - 1 >= 0 and end + 1 < len(s):
        # there is room to expand.
        if s[start-1] != s[end+1]:
            break
        else:
            start -= 1
            end += 1
    length = end + 1 - start
    return length, start, end

"""
11 - Container With Most Water
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Input: [1,8,6,2,5,4,8,3,7]
Output: 49
"""
def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    i = 0
    j = len(height) -1
    maxArea = 0

    while i < j:
        h = height[i] if height[i] < height[j] else height[j]
        width = j - i
        if maxArea < h * width:
            maxArea = h * width
        
        if height[i] < height[j]:
            i+=1
        else:
            j-=1
    return maxArea
        
""" 
15 - 3Sum

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

Example:
Given array nums = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
result = []
def threeSum(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    x1 = nums.pop()

""" 
55 - Jump Game

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index. 
"""
def canJump(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    if len(nums) < 1:
        return False
    return canJumpHelper(nums,0, 0)

def canJumpHelper(nums, index, steps):
    arr_len = len(nums)
    max_step = nums[index]
    # possible steps from the value of this index
    if index == len(nums)-1:
        return True
    if max_step == 0 and arr_len > 0:
        return False
    for steps in range(nums[index]):
        steps += 1      # can't step with 0
        if steps > len(nums):
            return False
        else:
            index += steps
            return canJumpHelper(nums, index,  steps)

""" 
121 - Best Time to Buy and Sell Stock
Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), 
design an algorithm to find the maximum profit.
Note that you cannot sell a stock before you buy one.

Example 1:
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
"""
def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if len(prices) < 2:
        return 0
    max_profit = 0
    lowest_price = sys.maxsize
    for p in prices:
        if p < lowest_price:
            lowest_price = p
        else:
            # current price is higher than the lowest_price
            if p - lowest_price > max_profit:
                max_profit = p - lowest_price
    return max_profit

"""
61 - Rotate List
Given a linked list, rotate the list to the right by k places, where k is non-negative.
Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
"""
def rotateRight(head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    if head == None:
        return None
    #   put them into a list
    lst = []
    while head != None:
        temp = head
        lst.append(temp)
        head = head.next
    linkedListLen = len(lst)
    if k > linkedListLen:
        k = k % linkedListLen
        print(k)
    while k > 0:
        end_item = lst.pop()
        lst.insert(0,end_item)
        k -= 1
    
    temp = ListNode(0)
    head = temp
    for node in lst:
        temp.next = node
        temp = temp.next
    temp.next = None
    return head.next


""" 
13 - Roman to Integer  
"""
def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    roman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    if s == "":
        return 0
    i = 0
    result = 0
    while i < len(s):
        if i + 1 < len(s):
            if s[i] == "I" and (s[i+1] == "V" or s[i+1] == "V"):
                result = result + roman[s[i+1]] - roman[s[i]]
                i += 2
            elif s[i] == "X" and (s[i+1] == "L" or s[i+1] == "C"):
                result = result + roman[s[i+1]] - roman[s[i]]
                i += 2
            elif s[i] == "C" and (s[i+1] == "D" or s[i+1] == "M"):
                result = result + roman[s[i+1]] - roman[s[i]]
                i += 2
            else:
                result = result + roman[s[i]]
                i += 1
        else:
            result = result + roman[s[i]]
            i += 1
    return result


""" 
14 - Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""
def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    lcp = ""
    if strs == []:
        return lcp
    
    i = 0
    flag = True
    while i < len(strs[0]) and flag == True:
        c = strs[0][i]
        j = 1
        while j < len(strs) and i < len(strs[j]):
            if c != strs[j][i]:
                flag = False
                break
            if j == len(strs)-1 and flag == True:
                lcp += c    
            j+=1
        if flag == False:
            break
        i += 1 
    return lcp

"""  
26 - Remove Duplicates from Sorted Array

Given a sorted array nums, 
remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, 
you must do this by modifying the input array in-place with O(1) extra memory.
"""
def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # My thought and intuition at first.
    # hold the item as a comparator and pop the duplicates as you see it.
    # if they are not the same, then you have a new comparative itme.
    if nums == []:
        return 0
    if len(nums) == 1:
        return 1
    i = 1
    item = nums[0]
    while i < len(nums):
        if item == nums[i]:
            nums.pop(i)
        else:
            item = nums[i]
            i += 1
    print(nums)
    return len(nums)

""" 
28 - Implement strStr()

Implement strStr().

Return the index of the first occurrence of needle in haystack, 
or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
"""
def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if needle == "":
        return 0
    if haystack == "" or len(needle) > len(haystack):
        return -1
    hay_len = len(haystack)
    # needle_len = len(needle)
    i = 0
    while i + len(needle) - 1 < hay_len:
        if haystack[i:i+len(needle)] == needle:
            return i
        else:
            i +=1 
    return -1


""" 
24 - Swap Nodes in Pairs

Swap Nodes in Pairs
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.
Example:
Given 1->2->3->4, you should return the list as 2->1->4->3.
"""
def swapPairs(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if head == None or head.next == None:
        return head
    dummy = ListNode(0)
    dummy.next = head
    cur = dummy

    while cur.next and cur.next.next:
        f = cur.next
        s = cur.next.next
        f.next = s.next
        s.next = f
        cur.next = s
        cur = f
    return dummy.next


""" 
42. Trapping Rain Water
Given n non-negative integers representing an elevation map 
where the width of each bar is 1, 
compute how much water it is able to trap after raining.

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""
def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """
    total_water = 0
    i = 1
    j = len(height) - 1
    if len(height) < 3:
        return total_water
    left = height[0]
    while i < len(height):
        if i == len(height) -1:
            break
        right = height[i]
        if left > right:
            total_water += left-right
        else:
            left = right
        i += 1
    return total_water


""" 
324 - Wiggle Sort II

Given an unsorted array nums, reorder it such that 
nums[0] < nums[1] > nums[2] < nums[3]....

Input: nums = [1, 5, 1, 1, 6, 4]
Output: One possible answer is [1, 4, 1, 5, 1, 6].
"""
def wiggleSort(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    i = 0
    j = 1
    # 0 = '<', 1 = '>'
    sign = 0
    if len(nums) < 2:
        return
    while j < len(nums):
        if sign == 0:
            if nums[i] >= nums[j]:
                # 'i' less than 'j'
                k = j
                while k < len(nums):
                    if nums[k] > nums[i]:
                        temp = nums[j]
                        nums[j] = nums[k]
                        nums[k] = temp
                        break
                    k+=1
            sign = 1
        else:
            # 'i' greater than 'j'
            if nums[i] <= nums[j]:
                k = j
                while k < len(nums):
                    if nums[i] > nums[k]:
                        temp = nums[j]
                        nums[j] = nums[k]
                        nums[k] = temp
                        break
                    k+=1
            sign = 0
        i += 1
        j += 1



def main():
    # result = []
    # consecutive_sum([1,2,3,4,5],result)
    # print(result)
    # test = [1,2,3,4,5]
    # allPossibleComb(test, 3)
    # s = "cbbd"
    # s = "bb"
    # print(longestPalindrome(s))
    # # print(maxProfit([1,2,3,1,1,1,1,3,2,1]))
    # l1 = ListNode(1)
    # l2 = ListNode(2)
    # l3 = ListNode(3)
    # l4 = ListNode(4)
    # l5 = ListNode(5)
    # l1.next = l2
    # l2.next = l3
    # l3.next = l4
    # l4.next = l5
    # l3.next = None
    # answer = rotateRight(l1, 20)
    # answer = swapPairs(l1)
    # while answer != None:
    #     print(answer.val)
    #     answer = answer.next
    # haystack = "aa"
    # needle = "a"
    # print(strStr(haystack, needle))
    # print("answer: ", romanToInt("XXXLIV"))
    # print("answer: ", longestCommonPrefix(["aa","a"]))
    # print ("answer: ", removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
    # print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
    nums = [1, 3, 2, 2, 3, 1]
    wiggleSort(nums)
    print(nums)

if __name__== "__main__":
    main()
