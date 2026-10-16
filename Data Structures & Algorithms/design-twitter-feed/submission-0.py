"""
tweets dict = userId -> (time, tweetId)
following = userId -> set of FolloweeIds
global timestamp to assign to each tweet
getNewsFeed = gather last 10 tweets of user and each followee, then sort by ts using max heap to get 10 newest. So take 10 from user and 10 from each followee  
"""

import heapq
from collections import defaultdict

class Twitter:

    FEED_SIZE = 10

    def __init__(self):
        self.timestamp = 0
        self.tweets: dict[int, list(tuple[int, int])] = defaultdict(list)
        self.following: dict[int, set[int]] = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        candidates: list[tuple[int, int]] = []
        sources = self.following[userId] | {userId}

        for source in sources:
            candidates.extend(self.tweets[source][-self.FEED_SIZE:])
        
        heap = [(-time, tweetId) for time, tweetId in candidates]
        heapq.heapify(heap)

        feed = []
        while heap and len(feed) < self.FEED_SIZE:
            _, tweetId = heapq.heappop(heap)
            feed.append(tweetId)
        return feed



    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
        
