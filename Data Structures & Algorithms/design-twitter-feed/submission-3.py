class Twitter:

    def __init__(self):
        # key is user, val is list[[interval, tweetId]].
        self.user_to_tweets = defaultdict(list)
        
        # key is user, val is the following
        self.user_to_following = defaultdict(set)

        self.interval = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_to_tweets[userId].append([self.interval, tweetId])
        self.interval += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        following_tweets = self.user_to_tweets[userId].copy()

        for following in self.user_to_following[userId]:
            following_tweets.extend(self.user_to_tweets[following])

        min_heap = [[-x, y] for x, y in following_tweets]
        heapq.heapify(min_heap)

        recents = []
        for i in range(10):
            if not min_heap:
                break

            recents.append(heapq.heappop(min_heap)[1])

        self.interval += 1

        return recents

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.user_to_following[followerId].add(followeeId)
        self.interval += 1

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId or followeeId not in self.user_to_following[followerId]:
            return
        self.user_to_following[followerId].remove(followeeId)
        self.interval += 1
