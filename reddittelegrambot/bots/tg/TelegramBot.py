from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from reddittelegrambot.configs.telegram_config import TELEGRAM_BOT_TOKEN
import reddittelegrambot.configs.telegram_config as config
from reddittelegrambot.logs.logger import log
from reddittelegrambot.bots.tg.handlers.Handlers import Handlers
from reddittelegrambot.data.DataHandler import DataHandler

from multiprocessing import Process

class TelegramBot:
    
    
    def __init__(self, reddit_bot=None):
        
        self.reddit_bot = reddit_bot
        self.token = TELEGRAM_BOT_TOKEN
        self.app = None
        self.data_handler = DataHandler("reddittelegrambot\data\data.json")
        self.handlers = None
        self._init()
        
        self.start_sending()


    def _init(self):

        self.app = ApplicationBuilder().token(self.token).build()
        self.handlers = Handlers(self.data_handler, self.app.bot).get_handlers()
        self.app.add_handlers(self.handlers)
        
        # log.info("TelegramBot running as: " + str(self.app.bot.get_me()))
        
    def start_sending(self):
        
        users = self.data_handler.read_dict()
        reddit_bot = self.reddit_bot
        bot = self.app.bot
        send_posts = self._send_posts
        for user in users:
            Process(target=send_posts, args=(reddit_bot, bot, user, users[user]["subreddits"])).start()
        
    @staticmethod
    def _send_posts(reddit_bot, bot, user_id, subreddits):
        
        post = reddit_bot.get_post(subreddits, user_id)    
        
        bot.send_message(user_id, post.url)
        
        
    def run(self):
        self.app.run_polling()

    # async def make_post(self, post) -> None:
    #     for channel_id in config.CHANNEL_IDS:
    #         await self.app.bot.send_message(channel_id, post)
            
    # @staticmethod
    # def send_message(message):
    #     for channel_id in config.CHANNEL_IDS:
    #         log.info("Sending message to channel: " + str(channel_id))
    #         multiprocessing.Process(target=TelegramBot._send_message, args=(channel_id, message)).start()
    
    # def _send_message(channel_id, message):