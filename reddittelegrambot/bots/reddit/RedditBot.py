from reddittelegrambot.apis.reddit.RedditBotAPI import RedditBotAPI
from reddittelegrambot.logs.logger import log
from reddittelegrambot.bots.reddit.Posts import Posts
from reddittelegrambot.configs.reddit_config import SUBS_TO_SCRAPE
import sys
import time
class RedditBot:
    
    def __init__(self, tg_bot=None):
        
        self.tg_bot = tg_bot
        self.reddit = RedditBotAPI()
        self.api = RedditBotAPI().api
        self.user = None
        # self.posts = Posts()
        
    
    def _init(self):
        self.user = self.api.user.me()
        
        if self.user is None:
            log.info("User is None, exiting...")
            sys.exit(1)
        else:
            log.info("RedditBot running as: " + str(self.user))
        
    def get_post(self, subreddits = None, user_id = None):
        return self.reddit.get_post(subreddits, user_id)
    def run(self):
        self._init()
        # time.sleep(15)
        # await self.tg_bot.send_message("Bot started")
        