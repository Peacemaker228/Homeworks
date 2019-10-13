import telebot
TOKEN='946052041:AAHkk-nFADmvDadN8t9LRzoQtC1JNZ4_XBE'

bot=telebot.TeleBot(TOKEN)

keyb=telebot.types.ReplyKeyboardMarkup()
keyb.row('ВПР', 'ВИС')
keyb.row('МКИС', 'ВПМ')

@bot.message_handler(commands=['button'])
def groups(message):
	bot.send_message(message.chat.id,'Отправь название группы', reply_markup=keyb)

@bot.message_handler(commands=['get_sp'])
def link(message):
	line_kb=telebot.types.InlineKeyboardMarkup() #pole pustoe dlya bota
	url_btn=telebot.types.InlineKeyboardButton(text='Жми и перейдешь на сайт', url='https://donstu.ru/')
	line_kb.add(url_btn)

	my_button=telebot.types.InlineKeyboardButton(text='Пополнение счета', callback_data='1000')
	line_kb.add(my_button)

	bot.send_message(message.chat.id, 'Нажимай, пора в кальянную! ', reply_markup=line_kb)

@bot.callback_query_handler(func=lambda call:True)
def do_callback(call):
	if call.data=='1000':
		bot.send_message(call.message.chat.id, 'вы получили'+call.data)

@bot.message_handler(func=lambda message:True)		
def gr_ans(message):
	if message.text == 'ВПР':
		bot.send_message(message.chat.id, 'чекай на сайте лох')
	elif message.text=='ВИС':
		bot.send_message(message.chat.id, 'на сайте информация актуальней')
	elif message.text=='МКИС':
		bot.send_message(message.chat.id, '12.00 - встреча с Б.Ч. Месхи')	
	elif message.text=='ВПМ':
		bot.send_message(message.chat.id, 'ну нахер переводись на соцгум')

if __name__=='__main__':
	bot.polling()