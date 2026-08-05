class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out =1
        zero_flag = 0
        if not any(nums): return nums
        for i in nums:
            if i!=0:
                out *=i
            else: zero_flag += 1
        res = []
        for x in nums:
            if zero_flag==1:
                if x==0: res.append(out)
                else: res.append(0)
            elif zero_flag >=2:
                res.append(0)
            else:
                if x!=0: res.append(out//x)
                else: res.append(0)

        return res


        