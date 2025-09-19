class Solution(object):
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        numsCheck = {}
        for i, num in enumerate(nums):
            num_diff = target - num
            if num in numsCheck:
                return [numsCheck[num], i]
            numsCheck[num_diff] = i
        return []