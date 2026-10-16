class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for s in strs:
            frequency = [0] * 26
            for c in s:
                frequency[ord(c) - ord("a")] += 1
            
            frequency = tuple(frequency)
            
            if frequency not in res:
                res[frequency] = [s]
            else:
                res[frequency].append(s)
        
        return res.values()