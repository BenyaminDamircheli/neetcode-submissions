"""
[s1, e1), [s2,e2)

s1 < e2 and s2 < e1

keep bookings in a sorted list (start, end) tuples
on book call find the insertion index for the new interval
check the neighbor before and after to check that preceding ends before start and after must start after our end
if both pass, insert and return true.
"""

import bisect

class MyCalendar:
    
    def __init__(self):
        self.bookings: list[tuple[int, int]] = []

    def book(self, startTime: int, endTime: int) -> bool:
        index = bisect.bisect_left(self.bookings, (startTime, endTime))

        if index > 0 and self.bookings[index - 1][1] > startTime:
            return False
        
        if index < len(self.bookings) and self.bookings[index][0] < endTime:
            return False
        
        self.bookings.insert(index, (startTime, endTime))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)