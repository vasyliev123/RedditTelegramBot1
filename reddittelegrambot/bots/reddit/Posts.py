from reddittelegrambot.apis.reddit.RedditBotAPI import RedditBotAPI

class Posts:
    
    def __init__(self,):
        self.reddit = RedditBotAPI()
        self.api = RedditBotAPI().api
        self.posts = None
    
    def get_posts(self, subreddit = None, limit=10):
        self.posts = self.reddit.get_posts(subreddit, limit)
        for post in self.posts:
            print(post.title)  # Title of the post
            print(post.url)  # URL of the post
            print(post.score)  # Number of upvotes for the post
            print('------------')