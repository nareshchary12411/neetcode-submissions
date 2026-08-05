class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for i in nums:
            dic[i] = dic.get(i,0)+1
        arr =[]
        for num,cnt in dic.items():
            arr.append([cnt,num])
        arr.sort(reverse=True)


        i=0
        out = []
        for key,value in arr:
            if i<k:
                out.append(value)
                i +=1
        return out
            