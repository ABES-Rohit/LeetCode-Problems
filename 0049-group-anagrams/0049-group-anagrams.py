class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        if(len(strs)==0):
            return [[]]
        d=defaultdict(list)    
        for i in strs:
            x=tuple(sorted(i))
            d[x].append(i)
        return list(d.values())    
        