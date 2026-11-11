class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        matched_positions = set()
        for triplet in triplets:
            if any(value > goal for value, goal in zip(triplet, target)):
                continue
            
            for position, (value, goal) in enumerate(zip(triplet, target)):
                if value == goal:
                    matched_positions.add(position)
        
        return len(matched_positions) == 3