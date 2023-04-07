from telegram.ext import CommandHandler, ContextTypes, ConversationHandler, filters, MessageHandler, Updater
from telegram import Update

from reddittelegrambot.logs.logger import log
import reddittelegrambot.configs.telegram_config as config
class Handlers:

    def __init__(self, data_handler, bot):
        
        self.bot = bot
        self.data_handler = data_handler
        pass

    # async def hello(self,update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    #     await update.message.reply_text(f'Hello {update.effective_user.first_name}')

    async def info(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await update.message.reply_text(f'Created by @vasyliev123\n\nVersion 0.1 alpha\n\nSource code:https://www.github.com/vasyliev123/reddittelegrambot\n')

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        # self.data_handler.add_dict({str(update.effective_user.id): {"username": update.effective_user.username, "first_name": update.effective_user.first_name, "last_name": update.effective_user.last_name}})
        # await update.message.reply_text(f'AutoPoster bot activated\n\nThis bot will post the best posts from reddit to your telegram channel\n')
        # config.CHANNEL_IDS.append(update.message.chat.id)
        # await self.bot.send_message(-1001846421327, "Bot started")
        await update.message.reply_text("Welcome to AutoPoster bot\n\nThis bot will post the best posts from reddit to your telegram channel\n\nPlease forward a message from the channel you want to post to this bot")
        # await update.message.reply_text("Please forward a message from the channel you want to post to this bot")
        
        return 1
    
    async def start_bot(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        
        
        
        if update.message.forward_from_chat.type == "channel":
            user_id = update.effective_user.id
            channel_id = update.message.forward_from_chat.id
            bot_id = self.bot.id
            admins = []
            for chat_member in await context.bot.get_chat_administrators(channel_id):  
                admins.append(chat_member.user.id)
                    
            print (admins)
            print (user_id)
            if user_id not in admins:
                await update.message.reply_text("You are not an admin of this channel")
                return ConversationHandler.END

            if bot_id not in admins:
                await update.message.reply_text("Bot is not an admin of this channel")
                return ConversationHandler.END
            
            
            self.data_handler.add_dict({str(update.effective_user.id): {"username": update.effective_user.username,
                                                                        "first_name": update.effective_user.first_name,
                                                                        "last_name": update.effective_user.last_name,
                                                                        "channel_id": update.message.forward_from_chat.id,
                                                                        "subreddits": [],
                                                                        "schedule": [],
                                                                        "imported_posts": [],}}) 
                                                                        
            
            await update.message.reply_text("Channel added")
            await update.message.reply_text("Please enter subreddits you want to post from, separated by commas")

            return 2
        else:
            await update.message.reply_text("Please forward a message from the channel you want to post to this bot")
            return 1
        
    async def set_subreddits(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        
        subreddits = [x.strip() for x in update.message.text.split(',')]
        self.data_handler.add_subreddits(str(update.effective_user.id), subreddits)
        await update.message.reply_text("Subreddits added")
        return ConversationHandler.END
    
  
        
    
        
        
    def get_handlers(self):
        return [CommandHandler('info', self.info),
                ConversationHandler(
                    entry_points=[CommandHandler('start', self.start)],
                    states={
                        1: [MessageHandler(filters.FORWARDED, self.start_bot)],
                        2: [MessageHandler(filters.TEXT, self.set_subreddits)],
                        # 3: [MessageHandler(filters.Filters.text, self.set_schedule)],
                    },
                    fallbacks={})]