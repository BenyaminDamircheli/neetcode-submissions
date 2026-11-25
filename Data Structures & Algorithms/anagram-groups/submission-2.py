class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            entry = res.get(tuple(count))
            if entry is None:
                res[tuple(count)] = []
            res[tuple(count)].append(s)
        
        return list(res.values())