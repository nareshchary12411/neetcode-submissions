class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = []
        extra_list = []
        c = strs.count("")
        if c>0:
            out.append(c*[""])
        for a in range(0,len(strs)):
            if strs[a]!="":
                li = []
                sort_a = sorted(strs[a])
                for b in range(a,len(strs)):
                    if sort_a== sorted(strs[b]): 
                        if b not in extra_list:
                            li.append(strs[b])
                            extra_list.append(b)
                        # strs.pop(b)
                if len(li)>0:
                    out.append(li)
        return out
            
