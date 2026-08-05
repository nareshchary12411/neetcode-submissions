class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        outt, outs = {}, {}
        a = len(s)
        if a != len(t):
            return False
        for x in range(0,a):
            outs[s[x]] = 1+ outs.get(s[x],0)
            outt[t[x]] = 1+ outt.get(t[x],0)
        if outt == outs:
            return True
        else: 
            return False