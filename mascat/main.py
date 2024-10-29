import telebot
from telebot import types

bot = telebot.TeleBot('7021337881:AAEql-VBvCqNokN_iQB7XMIAvXiYnN6S_Yk')

@bot.message_handler(commands=['start'])
def main(msg):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Расскажи о колледже💘')
    btn2 = types.KeyboardButton('Расскажи информацию абитуриенту💘')
    markup.row(btn1, btn2)
    btn3 = types.KeyboardButton('Расскажи информацию студентам💘')
    btn4 = types.KeyboardButton('Скинь структурные подразделения💘')
    markup.row(btn3, btn4)
    btn5 = types.KeyboardButton('Расскажи об олимпиадах и конкурсах💘')
    btn6 = types.KeyboardButton('Что говорит СМИ о колледже💘')
    markup.row(btn5, btn6)

    bot.send_message(msg.chat.id, f'Привет, {msg.from_user.first_name} 🐱 🐈! Чем могу помочь?😻', reply_markup=markup)
    bot.register_next_step_handler(msg, on_click)
def on_click(msg):
    if msg.text == 'Расскажи о колледже💘':
        bot.send_message(msg.chat.id, 'Мурмяу😽! Тут ты можешь почитать основные сведения о колледже:'
                                      ' https://xn----7sb4abld2ae.xn--p1ai/main/history/')
        bot.register_next_step_handler(msg, on_click)

    elif msg.text == 'Расскажи информацию абитуриенту💘':
        bot.send_message(msg.chat.id, 'Мрмрмр😽! Тут ты можешь почитать о специальнотсях, приёмной комиссии и другом:'
                                      'https://xn----7sb4abld2ae.xn--p1ai/abiturient/')
        bot.register_next_step_handler(msg, on_click)

    elif msg.text == 'Расскажи информацию студентам💘':
        bot.send_message(msg.chat.id, 'Мяу😽! Тут ты можешь узнать о расписании, частых вопросах и тому подобном: '
                                      'https://xn----7sb4abld2ae.xn--p1ai/student/')
        bot.register_next_step_handler(msg, on_click)

    elif msg.text == 'Скинь структурные подразделения💘':
        bot.send_message(msg.chat.id, 'Замуррчательно😽! Вот ссылочка на твой вопрос: '
                                      'https://xn----7sb4abld2ae.xn--p1ai/spk/')
        bot.register_next_step_handler(msg, on_click)

    elif msg.text == 'Расскажи об олимпиадах и конкурсах💘':
        bot.send_message(msg.chat.id, 'Мяфффффф😽! Почитать о мероприятиях, олимпиадах и конкурсах можно тут: '
                                      'https://xn----7sb4abld2ae.xn--p1ai/konferentsii/')
        bot.register_next_step_handler(msg, on_click)

    elif msg.text == 'Что говорит СМИ о колледже💘':
        bot.send_message(msg.chat.id, 'Мурррк😽! Здесь есть информация про СМИ о нашем колледже: '
                                      'https://xn----7sb4abld2ae.xn--p1ai/more/')
        bot.register_next_step_handler(msg, on_click)

@bot.message_handler()
def meow(msg):
    if msg.text.lower() != '/start':
        bot.send_message(msg.chat.id, f'Мяу, {msg.from_user.first_name}! Я отвечаю на кнопки, а не обычные сообщения😿')
        bot.register_next_step_handler(msg, on_click)

bot.polling(none_stop=True)