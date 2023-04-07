from praw import Reddit
from reddittelegrambot.configs.reddit_config import REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT, REDDIT_PASSWORD, REDDIT_USERNAME
from reddittelegrambot.data.DataHandler import DataHandler
from . import ImportedPosts
import random
class RedditBotAPI:

    def __init__(self,) -> None:
                #  client_id: str,
                #  client_secret: str,
                #  password: str,
                #  user_agent: str,
                #  username: str,):
        
        self.api = Reddit(client_id=REDDIT_CLIENT_ID,
                             client_secret=REDDIT_CLIENT_SECRET,
                             password=REDDIT_PASSWORD,
                             user_agent=REDDIT_USER_AGENT,
                             username=REDDIT_USERNAME,)
        
        self.data_handler = DataHandler("reddittelegrambot\data\data.json")
        
        
    def get_post(self, subreddits = None, user_id = None):
        subreddit = self.api.subreddit(random.choice(subreddits))
        post = subreddit.hot(limit=1)[0]
        if post.url in self.data_handler.read_dict()[user_id]["imported_posts"]:
            return self.get_post(subreddits, user_id)
        else:
            return post
        