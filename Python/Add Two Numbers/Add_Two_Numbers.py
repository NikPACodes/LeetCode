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

# #Examples
# test = Solution()
#
# test1_l1 = ListNode()
# test1_l1_first = test1_l1
# test1_l2 = ListNode()
# test1_l2_first = test1_l2
#
# test1_l1.val = 9
# test1_l1.next = ListNode(9)
# test1_l1 = test1_l1.next
# test1_l1.next = ListNode(9)
# test1_l1 = test1_l1.next
# test1_l1.next = ListNode(9)
# test1_l1 = test1_l1.next
# test1_l1.next = ListNode(9)
# test1_l1 = test1_l1.next
# test1_l1.next = ListNode(9)
# test1_l1 = test1_l1.next
# test1_l1.next = ListNode(9)
#
# test1_l2.val = 9
# test1_l2.next = ListNode(9)
# test1_l2 = test1_l2.next
# test1_l2.next = ListNode(9)
# test1_l2 = test1_l2.next
# test1_l2.next = ListNode(9)
#
# list = test.addTwoNumbers(test1_l1_first, test1_l2_first)
# while list:
#     print(list.val)
#     list = list.next




