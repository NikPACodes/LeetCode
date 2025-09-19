<h1>2.Add Two Numbers

[![ENG](https://img.shields.io/badge/README-English-red.svg)](README.md)
[![RUS](https://img.shields.io/badge/README-Russian-blue.svg)](README.ru.md)
</h1>

You are given two __non-empty__ linked lists representing two non-negative integers. 
The digits are stored in __reverse order__, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.  
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

__Example 1:__  
![ex1](https://assets.leetcode.com/uploads/2020/10/02/addtwonumber1.jpg)

```
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
```

__Example 2:__
```
Input: l1 = [0], l2 = [0]
Output: [0]
```

__Example 3:__
```
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
```

__Constraints:__
- _The number of nodes in each linked list is in the range [1, 100]_.
- $0 <=$ `Node.val` $<= 9$
- _It is guaranteed that the list represents a number that does not have leading zeros_.


<br>
<h2>Solution:</h2>

To solve this problem, it is necessary to iterate over all the values of the passed lists `l1`, `l2` and sum their values into the resulting linked list.
Since the list value can only contain one digit, we will create a variable for additional storage of the decimal point.

1) Initialize a linked list node and a reference to this node (_the first node of our list_):  
   ```
   result = ListNode()
   result_first = result
   ```
2) We create a variable `intDiv` to store __decimal places__ during calculation, since, according to the condition, the node value _can only take on a single digit_.
3) To calculate the sum of the nodes of two lists, initialize the variable `sumLists` by default equal to `intDiv` (_to carry the decimal place when moving to the next node_)
4) We start iterating and checking the linked lists `l1` and `l2` passed to the input:
   - If the node `l1` is __initialized__ (`l1 != None`), then __add__ the node value to `sumLists` and __move__ to the next node of the list `l1.next`:
   ```python
    if l1:
        sumLists += l1.val
       l1 = l1.next
    ```
   - We do the same with node `l2`:
     ```python
     if l2:
          sumLists += l2.val
          l2 = l2.next
     ```
5) We put the __units digit__ of the `sumLists` value into the node of our `result` list, and the __decimal digit__ into the `intDiv` variable:
   ```python
    result.val = sumLists % 10
    intDiv = sumLists // 10
   ```
6) Check:
   - If we have __initialized__ node `l1`, or `l2`, or `intDiv` not equal to `0`, then __initialized__ the next element of our table `result` and __move__ to it.
   - Otherwise, __exit__ the loop.
   ```python
    if l1 or l2 or intDiv:
        result.next = ListNode()
        result = result.next
    else:
        break
    ```
7) _Repeat steps 3-6_ until the input lists run out (i.e. `l1 = None` and `l2 = None`) and there is no decimal place left (i.e. `intDiv = 0`)
8) Returns `result_first` - __the first element node__ of our resulting linked list.

### Code
```python
from typing import Optional

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode])->Optional[ListNode]:
        result = ListNode()
        result_first = result
        intDiv = 0
        while True:
            sumLists = intDiv
            if l1:
                sumLists += l1.val
                l1 = l1.next
            if l2:
                sumLists += l2.val
                l2 = l2.next

            result.val = sumLists % 10
            intDiv = sumLists // 10
            if l1 or l2 or intDiv:
                result.next = ListNode()
                result = result.next
            else:
                break
        return result_first
```