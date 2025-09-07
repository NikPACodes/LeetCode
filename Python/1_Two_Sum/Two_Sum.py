class Solution(object):
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        numsCheck = {}
        for i, num in enumerate(nums):
            num_diff = target - num
            if num in numsCheck:
                return [numsCheck[num], i]
            numsCheck[num_diff] = i
        return []
#
# #Examples
# test = Solution()
# # test1
# num1 = [2, 7, 11, 15]
# t1 = 9
# print(test.twoSum(num1, t1))
#
# # test2
# num2 = [3, 2, 4]
# t2 = 6
# print(test.twoSum(num2, t2))
#
# # test3
# num3 = [3, 3]
# t3 = 6
# print(test.twoSum(num3, t3))
#
# # test4
# num4 = [9, 7, 6, 4, 0, 1]
# t4 = 9
# print(test.twoSum(num4, t4))
#
# # test5
# num5 = [5, 3, 9, 5]
# t5 = 10
# print(test.twoSum(num5, t5))
#
# # test6
# num6 = [5, 2, 9, 5, -1, 6]
# t6 = 8
# print(test.twoSum(num6, t6))