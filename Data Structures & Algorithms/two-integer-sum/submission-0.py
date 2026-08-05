class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        outl = {}
        for n in range(len(nums)):
            diff = target - nums[n]
            if diff in outl: return [outl[diff],n]
            else: outl[nums[n]] = n
        