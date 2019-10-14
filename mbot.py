from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging


logging.basicConfig(format='%(asctime)s-%(levelname)s-%(message)s',
					level=logging.INFO,	
					filename='bot.log'
					)



def start(bot, update):
	text='вызван /start еепта'
	logging.info(text) #если убрать то только в телеге
	update.message.reply_text(text) #если убрать то появл ток в консоли

def talk_to_me(bot,update):
	user_text='Привет {}! Ты написал: {}'.format(update.message.chat.first_name,update.message.text)
	logging.info('User:%s, chat_id: %s, message: %s', 
		update.message.chat.username,
		update.message.chat.id,
		update.message.text)
	update.message.reply_text(user_text)

def main():
	mybot=Updater('946052041:AAHkk-nFADmvDadN8t9LRzoQtC1JNZ4_XBE')
	logging.info('Bot starts')
	dp=mybot.dispatcher
	dp.add_handler(CommandHandler('start', start))
	dp.add_handler(MessageHandler(Filters.text, talk_to_me))



	mybot.start_polling()
	mybot.idle()
main()		