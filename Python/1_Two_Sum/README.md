<h1>1. Two Sum

[![ENG](https://img.shields.io/badge/README-English-red.svg)](README.md)
[![RUS](https://img.shields.io/badge/README-Russian-blue.svg)](README.ru.md)
</h1>

Given an array of integers `nums` and an integer `target`, return _indices of the two numbers such that they add up to_ `target`.  
You may assume that each input would have __exactly one solution__, and you may not use the _same_ element twice.  
You can return the answer in any order.

__Example 1:__
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

__Example 2:__
```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

__Example 3:__
```
Input: nums = [3,3], target = 6
Output: [0,1]
```

__Constraints:__
- $2 <=$ `nums.length` $<= 10^4$
- $-10^9 <=$ `nums[i]` $<= 10^9$
- $-10^9 <=$ `target` $<= 10^9$
- __Only one valid answer exists.__
 
__Follow-up:__ Can you come up with an algorithm that is less than $O(n^2)$ time complexity?


<br>
<h2>Solution:</h2>

### 1. A straightforward solution (complexity $$O(n^2)$$)

Straightforward solution:  
1) Loop through each element of the `nums` list
2) Use a nested loop to check if there is a pair in the remaining elements that, when added to the current element of the list, equals `target`
   - If a pair is __found__, _return the corresponding pair of indices_ `return [i, j]`
3) If a suitable pair is __not found__, _return an empty set_ `return []`

### Code
```python
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
```

<br>

### 2. Solutions using Hash-Table (complexity $$O(n)$$)

Solution using hash table (using dictionary): 
1) Create a dictionary `numsCheck = {}` that acts as our _hash table_
2) In a loop, check the _indexed_ (using the `enumerate` function) list received as input.
3) We check each element of the cycle for presence in our hash table:
   - If the element is _missing_, then we add an entry to `numsCheck`: `numsCheck[num_diff] = i`
   where __key__ is _the difference between the sought value and the value of the current element of the array_ `num_diff = target - num`,
   and __value__ is _the index of the current element of the array_
   - If the element is _present_ in `numsCheck`, then we return a pair of indices that will be the solution:
   `return [numsCheck[num], i]`
   where `i` is _the index of the current element_,
   and `numsCheck[num]` is _the index of the element in the sum that gives the sought_ `target`
   i.e. `nums[numsCheck[num]] + nums[i] = target`
4) If a suitable pair __was not found__, _return an empty set_ `return []`

### Code
```python
class Solution(object):
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        numsCheck = {}
        for i, num in enumerate(nums):
            num_diff = target - num
            if num in numsCheck:
                return [numsCheck[num], i]
            numsCheck[num_diff] = i
        return []
```