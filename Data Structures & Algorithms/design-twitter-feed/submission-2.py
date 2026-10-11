class Twitter:
    """
    1) users can post tweets
    2) users can follow / unfollow other users
    3) view 10 recent tweets from their feed

    Notes:
    Users - ids (int)
    Tweets - ids (int)


    """

    def __init__(self):
        self.users = [] # contains user_ids
        self.tweets = [] # contains (tweet_id, user_id) where user_id posted tweet_id
        self.follows = {} # adjaceny list type way, key is user, values are followings

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((tweetId, userId))

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        for networkTweetId, networkUserId in self.tweets[::-1]:
            # if already 10 tweets, return
            if len(res) == 10:
                break
            # users themselves posted this tweet
            if networkUserId == userId:
                res.append(networkTweetId)
            # user follows this poster
            elif networkUserId in self.follows.get(userId, []):
                res.append(networkTweetId)
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows and followeeId not in self.follows.get(followerId, []):
            self.follows[followerId].append(followeeId)
        else:
            self.follows[followerId] = [followeeId]

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows and followeeId in self.follows.get(followerId, []):
            self.follows[followerId].remove(followeeId)
