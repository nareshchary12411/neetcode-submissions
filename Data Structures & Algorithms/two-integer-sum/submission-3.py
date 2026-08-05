class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        outl = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in outl: 
                return [outl[diff],i]
            outl[n] = i
        