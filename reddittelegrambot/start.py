from reddittelegrambot.bots.reddit.RedditBot import RedditBot
from reddittelegrambot.bots.tg.TelegramBot import TelegramBot
from multiprocessing import Process

tg_bot = TelegramBot()
reddit_bot = RedditBot(tg_bot)


def run_tg_bot():
    tg_bot.run()


async def run_reddit_bot():
    await reddit_bot.run()


def run():

    telegram_process = Process(target=run_tg_bot)
    # reddit_process = Process(target=run_reddit_bot)
    
    telegram_process.start()
    # reddit_process.start()
