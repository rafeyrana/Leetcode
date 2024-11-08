import heapq
from typing import List

class Twitter:

    def __init__(self):
        self.time = 0
        self.following = {}  # Dictionary to store follow relationships
        self.tweets = {}      # Dictionary to store tweets for each user

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Initialize the user's tweet list if it doesn't exist
        if userId not in self.tweets:
            self.tweets[userId] = []
        # Add the tweet with a negative timestamp for recent tweets to come first in heap
        self.tweets[userId].append((-self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # Create a fresh min-heap for each call to getNewsFeed
        minHeap = []

        # Add the user's own tweets to the minHeap
        if userId in self.tweets:
            for tweet in self.tweets[userId]:
                heapq.heappush(minHeap, tweet)
                if len(minHeap) > 10:
                    heapq.heappop(minHeap)

        # Add tweets from the users that userId is following
        if userId in self.following:
            for followeeId in self.following[userId]:
                if followeeId in self.tweets:
                    for tweet in self.tweets[followeeId]:
                        heapq.heappush(minHeap, tweet)
                        if len(minHeap) > 10:
                            heapq.heappop(minHeap)
        print(minHeap)
        print([tweetId for _, tweetId in sorted(minHeap, reverse=True)])
        # Extract tweets in descending order of time
        return [tweetId for _, tweetId in sorted(minHeap, reverse=True)]

    def follow(self, followerId: int, followeeId: int) -> None:
        # Prevent users from following themselves
        if followerId != followeeId:
            if followerId not in self.following:
                self.following[followerId] = set()
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Safely remove followee if they exist
        if followerId in self.following and followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
