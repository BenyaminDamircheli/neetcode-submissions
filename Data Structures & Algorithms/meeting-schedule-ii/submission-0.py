"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

sort both start and end times in increasing order
keep 2 pointers, 1st pointer s will move as we iterate through start times
    - for 2nd pointer in ending times e, if ends[e] <= s then decrement rooms and advance e pointer 
    - if ends[e] > s then increment rooms
- best (largest) number of rooms seen so far
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted(i.start for i in intervals)
        ends = sorted(i.end for i in intervals)

        rooms = best = e = 0

        for s in starts:
            while ends[e] <= s:
                rooms -= 1
                e += 1
            
            rooms += 1
            best = max(best, rooms)
        
        return best


        