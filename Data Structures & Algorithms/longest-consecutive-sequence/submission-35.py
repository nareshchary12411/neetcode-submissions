class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums2 = list(set(nums))
        print(sorted(nums2))
        num1 = sorted(nums2)
        count = 0
        current_range = 1 
        lenn = len(num1)
        result_check = []
        if lenn == 1:
            return 1
        for x in range(1,lenn):
            if abs(num1[x]-num1[x-1]) == 1:
                current_range = current_range+1
                if x == lenn-1:
                    if current_range > count:
                        count=current_range 
                        current_range = 0

            else:
                if current_range > count:
                    count = current_range 
                current_range = 1
        print(result_check)
        return count

