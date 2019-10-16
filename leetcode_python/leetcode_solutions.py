""" 
Problem: Movies On Flight 

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
Problem: Treasure Island 1

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

    