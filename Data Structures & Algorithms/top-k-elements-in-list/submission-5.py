class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] += 1
        
        for n,f in count.items():
            freq[f].append(n)
        
        result = []

        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                result.append(n)

        
        return result[:k]
