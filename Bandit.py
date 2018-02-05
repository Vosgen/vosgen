# -*- coding: utf-8 -*-
import config
import telebot
import requests

bot = telebot.TeleBot(config.token)

from telebot import types

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#markup.row('Привет', 'Текст')
markup.row('/start')
@bot.message_handler(commands=['start'])
def first(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('/start')
    bot.send_message(message.chat.id, 'Вы всегда можете вернуться в главное меню нажав "/start"',
     reply_markup=keyboard,parse_mode='Markdown')
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in
    ['🎁Покупка','📄Отзывы','📈Вакансии',
    '📍Помощь']])
    bot.send_message(message.chat.id, 'Приветсвуем вас в магазине ГРЯДКА - rediskaeppnonytq.onion'
    '\nоткрывается только через TOR браузер.'
    '\nНА ТЕЛЕФОНЕ ОТКРЫВАТЬ ПРИЛОЖЕНИЯМИ orbot + orfox.'+'\n'+13*'➖'+ '\nДоступна оплата киви',parse_mode='Markdown', reply_markup=keyboard)
    #bot.register_next_step_handler(first, inline)
@bot.callback_query_handler(func=lambda c: True)
def inline(c):
    if c.data == '🏠Главное меню':
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in
        ['🎁Покупка','📄Отзывы','📈Вакансии',
        '📍Помощь']])
        bot.edit_message_text(
        chat_id=c.message.chat.id,
        message_id=c.message.message_id,
        text = 'Приветсвуем вас в магазине ГРЯДКА - rediskaeppnonytq.onion'
         '\nоткрывается только через TOR браузер.'
         '\nНА ТЕЛЕФОНЕ ОТКРЫВАТЬ ПРИЛОЖЕНИЯМИ orbot + orfox.'+'\n'+13*'➖'+ '\nДоступна оплата киви',parse_mode='Markdown', reply_markup=keyboard)
    elif c.data == '🎁Покупка' or c.data == '🎁К покупкам':
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in
        ['ОМСК','СУРГУТ','🏠Главное меню']])
        bot.edit_message_text(
        chat_id=c.message.chat.id,
        message_id=c.message.message_id,
        text=13*'➖' + '\nСейчас в наличии в следующих городах:',
        parse_mode='Markdown', reply_markup=keyboard)
    elif c.data == '📄Отзывы' or c.data == '📄Ещё отзыв':
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in
        ['📄Ещё отзыв ','📝Оставить отзыв','🏠Главное меню']])
        import random
        import datetime
        now = datetime.datetime.now()
        O1 = random_item = random.SystemRandom().choice(['darnVader / круть','Jonny / пойдёт',
        'guffiman / Мука от разных дилеров не впечатляет, впечатлила только когда почти 2 года назад попробовал первый раз. Однако за последний год только тут я восхищаюсь здешними криссами',
        'veckk / Описание превосходное, все ясно и понятно, на уровне.',
        'paifist / Брали 2г муки у данного селлера. Были приятно удивлены четкому описанию и быстрому находу. упаковка фольга, 2 флопа',
        'xuysgorky / По весу очень радует, магазин не жалеет и сыпит от души. Эффекты прекрасные, две небольшие дорожки и на целый час в эйфорию с головой))',
        'NarkoSSHa / пацаны вообще ребята','Aqx1988 / Побежал как соник пыхать🏃'])
        time = now.strftime("%d-%B-%Y")
        bot.edit_message_text(
        chat_id=c.message.chat.id,
        message_id=c.message.message_id,
        text='➖➖'+ O1 + '➖➖\n➖➖'+ time +'➖➖', parse_mode='Markdown',reply_markup=keyboard)
    elif c.data == '📄Ещё отзыв ':
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in
        ['📄Ещё отзыв','📝Оставить отзыв','🏠Главное меню']])
        import random
        import datetime
        now = datetime.datetime.now()
        O1 = random_item = random.SystemRandom().choice(['darkVader / круть','Jonny01001 / пойдёт','NarkoSSHka / пацаны вообще ребята','Aqx1989 / Побежал как соник пыхать🏃',
        'riogrand / Мука.Начал с 250 по носу.Приход в течении 10- 15 минут.Накрыло сдержанной эйфорией и качественно держало в пределах часа.Затем плавный спад, дискомфорт присутствует конечно,но он минимальный.Догнался остатками и все повторилось,но менее ярко.',
'SugarCroisd / юзер мефа, до этого пробывал всего пару раз, поэтому позвал с собой на тест опытного друга, при этом я пил, а он нюхал, полный тест так сказать.Друг после одной хорошей дорожки,ощутил эффект достаточно быстро, и начал с огромным удовольствием много разговаривать, но мне пришлось еще подождать для эффекта!',
'Putinteam4 / Обращался 2 раза, клады и качество стафа всегда достойные','Zhiza1996 / Клады надежные, места безлюдные и доступные. Ребята щедрые, по весам всегда перевес.'])
        time = now.strftime("%d-%B-%Y")
        bot.edit_message_text(
        chat_id=c.message.chat.id,
        message_id=c.message.message_id,
        text='➖➖'+ O1 + '➖➖\n➖➖'+ time +'➖➖', parse_mode='Markdown',reply_markup=keyboard)
    elif c.data == '📝Оставить отзыв':
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in
        ['📄Отзывы','🏠Главное меню']])
        bot.edit_message_text(
        chat_id=c.message.chat.id,
        message_id=c.message.message_id,
        text='📝Оставлять отзывы можно только после покупки!!\n'+13*'➖', parse_mode='Markdown',reply_markup=keyboard)
    elif c.data == '📈Вакансии':
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in
        ['👨‍💻Оператор','🏃Курьер','🏠Главное меню']])
        bot.edit_message_text(
        chat_id=c.message.chat.id,
        message_id=c.message.message_id,
        text='{:^45}'.format('*Вакансии:*') + '\n' + 13*'➖' + '\nТребуются работники:\n Омск - оператор, курьер\n Сургут - курьер\n'+13*'➖', parse_mode='Markdown',reply_markup=keyboard)
    elif c.data == '👨‍💻Оператор':
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in
        ['📋Анкета','🏃Курьер','🏠Главное меню']])
        bot.edit_message_text(
        chat_id=c.message.chat.id,
        message_id=c.message.message_id,
        text='*Оператор*'+ '\n' + 13*'➖' + '\nОплата:\n40-60к в неделю\nВыплата на Qiwi или BitCoin' + '\n' + 13*'〰' +
        '\nТребования:\n1. Умение ориентироваться в улицах г.Омска\n2. Понимание функционирования данной сферы деятельности'
        '\n3. Умение пользоваться анонимизаторами (ТОР, ВПН и т.д.)\n4. Иметь залог 15т.р.\n5. Быть в сети исходя из индивиуального расписания'+ '\n' + 13*'〰' +
        '\nОбязанности:\n1. Координирование курьеров\n2. Работа с базой адрресов\n3. Консультация по ненаходам\n4.Обслуживание кошельков\n' + 13*'➖' +
        '\nЕсли вас устраивают условия и вы готовы работать, заполните анкету👇', parse_mode='Markdown',reply_markup=keyboard)
    elif c.data == '🏃Курьер':
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in
        ['📋Анкета','👨‍💻Оператор','🏠Главное меню']])
        bot.edit_message_text(
        chat_id=c.message.chat.id,
        message_id=c.message.message_id,
        text='*Курьер*'+ '\n' + 13*'➖' + '\nОплата:\nПо факту,за клад\n🔸300-500р - природа\n🔸600-1000р\nОбъём работы в день 20-30 кладов\nВыплата на Qiwi или BitCoin' + '\n' + 13*'〰' +
        '\nТребования:\n1. Знание города\n2. Высокая работоспособность и умение чётко описать место закладки'
        '\n3. Возможность делать адреса в формате координаты+опиание+фото. Плюсом будет умение пользоваться анонимизаторами (ТОР, ВПН и т.д.)\n4. Иметь залог от 5000 руб с последующей наработкой\n5. Быть онлайн 2-3 раза в сутки'
        '\n6. Предпочтение отдается кандидатам с наличием автомобиля\n' + 13*'➖' +
        '\nЕсли вас устраивают условия и вы готовы работать, заполните анкету👇', parse_mode='Markdown',reply_markup=keyboard)
    elif c.data == '📋Анкета':
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in
        ['🏠Главное меню']])
        bot.edit_message_text(
        chat_id=c.message.chat.id,
        message_id=c.message.message_id,
        text='!                       *АНКЕТА*                       !'+ '\n' + 13*'➖' + '\n1. Возраст\n2. Город\n3. Условия проживания (живете один или с кем-то, снимаете жилье или своё)'
        '\n4. Работали ли вы ранее в подобной сфере? Если да, то как вы оцените свою производительность (сколько кладов в день)'
        '\n5. Наличие авто\n6. Какой залог готовы внести? ( Меньше 5к не писать)\n7. Есть ли у Вас возможность находиться на связи весь рабочий день?'
        '\n8. В какое время суток Вы готовы работать (утро, день, ночь)?\n9. Есть ли у Вас основная работа (если да, то какая, и сколько занимает времени)?\n'
         + 13*'➖' +
        '\nОтправлять анкету на любой из адресов:\nTelegram: @vosgen\nJabber: будет позже\nПочта: будет позже\n\nОтвет в течение 24 часов!!!', parse_mode='Markdown',reply_markup=keyboard)
    elif c.data == '📍Помощь':
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in
        ['🏠Главное меню']])
        bot.edit_message_text(
        chat_id=c.message.chat.id,
        message_id=c.message.message_id,
        text='Если у вас возникли проблемы, пишите нам в автомагазине.\nrediskaeppnonytq.onion \nоткрывается только через TOR браузер \nНА ТЕЛЕФОНЕ ОТКРЫВАТЬ ПРИЛОЖЕНИЯМИ orbot + orfox\nTelegram поддержка @helpgrydka', parse_mode='Markdown',reply_markup=keyboard)
    elif c.data == 'ОМСК' or c.data == 'Другая категория':
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in
        ['🌿Природа💨','❄Кристалы/Порошки💨','💊Пилюли👄','🏠Главное меню']])
        bot.edit_message_text(
        chat_id=c.message.chat.id,
        message_id=c.message.message_id,
        text='Выберите категорию товара:'+ '\n' + 13*'➖' + '\nВ наличии👇👇👇', parse_mode='Markdown',reply_markup=keyboard)
    elif c.data == '🌿Природа💨' or c.data == 'Назад':
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in
        ['NY 1г 1400р','NY 3г 4750р','NY 4г 5850р','NY 5г 6600р','AK47 1г 1200р','АК47 3г 2800р','Гарик 4г 4200р','Гарик 6г 5500р','Другая категория','🏠Главное меню']])
        bot.edit_message_text(
        chat_id=c.message.chat.id,
        message_id=c.message.message_id,
        text='{:^45}'.format('🌿Природа💨') + '\n' + 13*'➖' + '\nВ наличии👇👇👇' '\n' + 13*'➖' + '\n*New York ШИШ*\n1г за 1400 руб\n3г за 4750 руб \n4г за 5850 руб\n5г за 6600 руб\n\n*АК47*\n1г 1200р\n3г 2800р\n\n*Porshe Гарик*\n4г за 4200 руб\n6г за 5500 руб'+ '\n' + 13*'➖'
        + '\n     👇👇👇', parse_mode='Markdown',reply_markup=keyboard)
    elif c.data == 'NY 1г 1400р':
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in
        ['Кировск / КАО','Нефты / САО','Чкаловск / ОАО','Назад','🏠Главное меню']])
        a = 'Вы выбрали:' + '\n' + 13*'➖' + '\nСумма руб.: 1400   \nNew York ШИШ - 1г     '
        bot.edit_message_text(
        chat_id=c.message.chat.id,
        message_id=c.message.message_id,
        text=a + '\n' + 13*'➖' + '\nВыберите район:\n     👇👇👇', parse_mode='Markdown',reply_markup=keyboard)
    elif c.data == 'NY 3г 4750р':
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in
        ['Кировск / КАО','Нефты / САО','Ленинск / ЛАО','Чкаловск / ОАО','Назад','🏠Главное меню']])
        a = 'Вы выбрали:' + '\n' + 13*'➖' + '\nСумма руб.: 4750   \nNew York ШИШ - 3г     '
        bot.edit_message_text(
        chat_id=c.message.chat.id,
        message_id=c.message.message_id,
        text=a + '\n' + 13*'➖' + '\nВыберите район:\n     👇👇👇', parse_mode='Markdown',reply_markup=keyboard)
    elif c.data == 'NY 4г 5850р':
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in
        ['Кировск / КАО','Нефты / САО','Центр / ЦАО','Чкаловск / ОАО','Назад','🏠Главное меню']])
        a = 'Вы выбрали:' + '\n' + 13*'➖' + '\nСумма руб.: 5850   \nNew York ШИШ - 4г     '
        bot.edit_message_text(
        chat_id=c.message.chat.id,
        message_id=c.message.message_id,
        text=a + '\n' + 13*'➖' + '\nВыберите район:\n     👇👇👇', parse_mode='Markdown',reply_markup=keyboard)
    elif c.data == 'NY 5г 6600р':
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in
        ['Нефты / САО','Центр / ЦАО','Назад','🏠Главное меню']])
        a = 'Вы выбрали:' + '\n' + 13*'➖' + '\nСумма руб.: 6600   \nNew York ШИШ - 5г     '
        bot.edit_message_text(
        chat_id=c.message.chat.id,
        message_id=c.message.message_id,
        text=a + '\n' + 13*'➖' + '\nВыберите район:\n     👇👇👇', parse_mode='Markdown',reply_markup=keyboard)
    elif c.data == 'AK47 1г 1200р':
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in
        ['Кировск / КАО','Нефты / САО','Ленинск / ЛАО','Центр / ЦАО','Чкаловск / ОАО','Назад','🏠Главное меню']])
        a = 'Вы выбрали:' + '\n' + 13*'➖' + '\nСумма руб.: 1200  \nAK47 - 1г           '
        bot.edit_message_text(
        chat_id=c.message.chat.id,
        message_id=c.message.message_id,
        text=a + '\n' + 13*'➖' + '\nВыберите район:\n     👇👇👇', parse_mode='Markdown',reply_markup=keyboard)
    elif c.data == 'АК47 3г 2800р':
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in
        ['Нефты / САО','Назад','🏠Главное меню']])
        a = 'Вы выбрали:' + '\n' + 13*'➖' + '\nСумма руб.: 2800   \nAK47 - 3г           '
        bot.edit_message_text(
        chat_id=c.message.chat.id,
        message_id=c.message.message_id,
        text=a + '\n' + 13*'➖' + '\nВыберите район:\n     👇👇👇', parse_mode='Markdown',reply_markup=keyboard)
    elif c.data == 'Гарик 4г 4200р':
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in
        ['Кировск / КАО','Ленинск / ЛАО','Назад','🏠Главное меню']])
        a = 'Вы выбрали:' + '\n' + 13*'➖' + '\nСумма руб.: 4200   \nPorshe Гарик - 4г     '
        bot.edit_message_text(
        chat_id=c.message.chat.id,
        message_id=c.message.message_id,
        text=a + '\n' + 13*'➖' + '\nВыберите район:\n     👇👇👇', parse_mode='Markdown',reply_markup=keyboard)
    elif c.data == 'Гарик 6г 5500р':
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in
        ['Кировск / КАО','Назад','🏠Главное меню']])
        a = 'Вы выбрали:' + '\n' + 13*'➖' + '\nСумма руб.: 5500   \nPorshe Гарик - 6г     '
        bot.edit_message_text(
        chat_id=c.message.chat.id,
        message_id=c.message.message_id,
        text=a + '\n' + 13*'➖' + '\nВыберите район:\n     👇👇👇', parse_mode='Markdown',reply_markup=keyboard)
    elif c.data == 'Кировск / КАО':
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in
        ['🐤Qiwi','💰BitCoin','Назад','Другая категория','🏠Главное меню']])
        f = c.message.text
        bot.edit_message_text(
        chat_id=c.message.chat.id,
        message_id=c.message.message_id,
        text=f[0:65] + '\nРайон: Кировск / КАО' + '\n' + 13*'➖' + '\nВыберите способ оплаты:\n     👇👇👇', parse_mode='Markdown',reply_markup=keyboard)
    elif c.data == 'Нефты / САО':
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in
        ['🐤Qiwi','💰BitCoin','Назад','Другая категория','🏠Главное меню']])
        f = c.message.text
        bot.edit_message_text(
        chat_id=c.message.chat.id,
        message_id=c.message.message_id,
        text=f[0:65] + '\nРайон: Нефты / САО  ' + '\n' + 13*'➖' + '\nВыберите способ оплаты:\n     👇👇👇', parse_mode='Markdown',reply_markup=keyboard)
    elif c.data == 'Ленинск / ЛАО':
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in
        ['🐤Qiwi','💰BitCoin','Другая категория','🏠Главное меню']])
        f = c.message.text
        bot.edit_message_text(
        chat_id=c.message.chat.id,
        message_id=c.message.message_id,
        text=f[0:65] + '\nРайон: Ленинск / ЛАО' + '\n' + 13*'➖' + '\nВыберите способ оплаты:\n     👇👇👇', parse_mode='Markdown',reply_markup=keyboard)
    elif c.data == 'Центр / ЦАО':
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in
        ['🐤Qiwi','💰BitCoin','Другая категория','🏠Главное меню']])
        f = c.message.text
        bot.edit_message_text(
        chat_id=c.message.chat.id,
        message_id=c.message.message_id,
        text=f[0:65] + '\nРайон: Центр / ЦАО ' + '\n' + 13*'➖' + '\nВыберите способ оплаты:\n     👇👇👇', parse_mode='Markdown',reply_markup=keyboard)
    elif c.data == 'Чкаловск / ОАО':
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in
        ['🐤Qiwi','💰BitCoin','Другая категория','🏠Главное меню']])
        f = c.message.text
        bot.edit_message_text(
        chat_id=c.message.chat.id,
        message_id=c.message.message_id,
        text=f[0:65] + '\nРайон: Чкаловск / ОАО' + '\n' + 13*'➖' + '\nВыберите способ оплаты:\n     👇👇👇', parse_mode='Markdown',reply_markup=keyboard)
    elif c.data == '🐤Qiwi':
        import random
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in
        ['Запомнить','Проверка оплаты','🏠Главное меню']])
        z0 = c.message.text
        z1 = (z0[0:87])
        z2 = ('➖➖➖➖➖➖➖➖➖➖➖➖➖\n')
        z3 = ('Qiwi кошелёк: +79026797658')
        z4 = ('\nКод при оплате:')
        z5 = (' {r1}'.format(r1=random.randint(100,999)))
        z6 = ('\n')
        z7 = ('➖➖➖➖➖➖➖➖➖➖➖➖➖\n!!!Переведите на QIWI  в течение 24 часов!!!\n➖➖➖➖➖➖➖➖➖➖➖➖➖\nПеред покупкой необходимо нажать кнопку запомнить👇')
        z=z1+z2+z3+z4+z5+z6+z7
        bot.edit_message_text(
        chat_id=c.message.chat.id,
        message_id=c.message.message_id,
        text = z,
        parse_mode='Markdown', reply_markup=keyboard)
    elif c.data == '💰BitCoin':
        import requests
        r = requests.get("https://api.coinmarketcap.com/v1/ticker/bitcoin/?convert=RUB")
        a = r.json()
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in
        ['Зафиксировать','Проверка оплаты','🏠Главное меню']])
        f = c.message.text
        z1 = (f[0:25])
        z2 = (f[45:87])
        z3 = ('BTC кошелёк: ' + ' *16AyNkfmA6rbDyncwY1qsxUDbHud5az9pH*\n')
        z5 = ('Курс: ')
        z6 = ('1 ' + a[0]["id"] + ' = '+ a[0]['price_rub'] + ' руб.')
        z7 = ('\nСумма: ' + f[38:44] + 'рублей' + '\nСумма в BTC (5% скидка) = ')
        a = float(a[0]['price_rub'])
        b = float(f[38:44])
        z8 = (str(round(float(1)/a*b*0.95,6)))
        z9 = ('\n' + 13*'➖' + '\nПеред покупкой необходимо нажать кнопку зафиксировать.\nПроизойдёт фиксация заявки на покупку и будет выслан отдельным сообщением биткоин кошелёк.')
        x1 = [z1 + z2 + z3 + z5 + z6 + z7 + z8 +z9]
        bot.edit_message_text(
        chat_id=c.message.chat.id,
        message_id=c.message.message_id,
        text = x1,
        parse_mode='Markdown', reply_markup=keyboard)
    elif c.data == 'Зафиксировать':
        bot.send_message(c.message.chat.id,'*16AyNkfmA6rbDyncwY1qsxUDbHud5az9pH*', parse_mode='Markdown')
        a=c.message.text
        d=c.message.chat.first_name
        e=c.message.chat.last_name
        b=str(c.message.chat.id)
        c=str(c.message.chat.username)
        bot.send_message(
        chat_id=355755238,
        text=a[26:207]+'\nЧат №: ' + b + '\nusername ' + c + '\nПользователь: ' + d + ' ' + e,
        parse_mode='Markdown')
    elif c.data == 'Запомнить':
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in
        ['Проверка оплаты','🏠Главное меню']])
        a=c.message.text
        bot.send_message(c.message.chat.id,a[0:206], parse_mode='Markdown',reply_markup=keyboard)
        a=c.message.text
        d=c.message.chat.first_name
        e=c.message.chat.last_name
        b=str(c.message.chat.id)
        c=str(c.message.chat.username)
        bot.send_message(
        chat_id=355755238,
        text=a[26:207]+'\nЧат №: ' + b + '\nusername ' + c + '\nПользователь: ' + d + ' ' + e,
        parse_mode='Markdown')
    elif c.data == 'Проверка оплаты':
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in
        ['Проверка оплаты','🏠Главное меню']])
        import time
        a=c.message.text[0:206]
        bot.edit_message_text(
        chat_id=c.message.chat.id,
        message_id=c.message.message_id,
        text = a + '\n' + 13*'➖' + '\n' + 'Проверка оплаты .',
        parse_mode='Markdown')
        time.sleep(1)
        bot.edit_message_text(
        chat_id=c.message.chat.id,
        message_id=c.message.message_id,
        text = a + '\n' + 13*'➖' + '\n' + 'Проверка оплаты ..',
        parse_mode='Markdown')
        time.sleep(1)
        bot.edit_message_text(
        chat_id=c.message.chat.id,
        message_id=c.message.message_id,
        text = a + '\n' + 13*'➖' + '\n' + 'Проверка оплаты ...',
        parse_mode='Markdown')
        bot.edit_message_text(
        chat_id=c.message.chat.id,
        message_id=c.message.message_id,
        text = a + '\n' + 13*'➖' + '\n' + 'Проверка оплаты . ',
        parse_mode='Markdown')
        time.sleep(1)
        bot.edit_message_text(
        chat_id=c.message.chat.id,
        message_id=c.message.message_id,
        text = a + '\n' + 13*'➖' + '\n' + 'Проверка оплаты .. ',
        parse_mode='Markdown')
        time.sleep(1)
        bot.edit_message_text(
        chat_id=c.message.chat.id,
        message_id=c.message.message_id,
        text = a + '\n' + 13*'➖' + '\n' + 'Проверка оплаты ... ',
        parse_mode='Markdown')
        bot.edit_message_text(
        chat_id=c.message.chat.id,
        message_id=c.message.message_id,
        text = a + '\n' + 13*'➖' + '\n' + 'Проверка оплаты .  ',
        parse_mode='Markdown')
        time.sleep(1)
        bot.edit_message_text(
        chat_id=c.message.chat.id,
        message_id=c.message.message_id,
        text = a + '\n' + 13*'➖' + '\n' + 'Проверка оплаты ..  ',
        parse_mode='Markdown')
        time.sleep(1)
        q = bot.edit_message_text(
        chat_id=c.message.chat.id,
        message_id=c.message.message_id,
        text = a + '\n' + 13*'➖' + '\n' + 'Получено 0 рублей\nСписок поступивших платежей обновляется раз в пять минут, пожалуйста, подождите...',
        parse_mode='Markdown', reply_markup=keyboard)
    elif c.data == '❄Кристалы/Порошки💨' or c.data == 'Назад ':
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in
        ['Мадам crystals\n1г 3900р','Мадам crystals\n2г 6700р','Меф кристаллический\n1г 2750р','Меф кристаллический\n2г 5000р','Меф Мука\n1г 1800р','Меф Мука\n2г 3200р','Другая категория','🏠Главное меню']])
        bot.edit_message_text(
        chat_id=c.message.chat.id,
        message_id=c.message.message_id,
        text='{:^45}'.format('❄Кристалы/Порошки💨') + '\n' + 13*'➖' + '\nВ наличии👇👇👇' '\n' + 13*'➖' + '\n*Мадам crystals*\n1г за 3900 руб\n2г за 6700 руб'
        '\n\n*Меф кристаллический*\n1г за 2750 руб\n3г за 7250 руб'
        '\n\n*Меф Мука*\n1г за 1800 руб\n2г за 3200 руб'+ '\n' + 13*'➖'
        + '\n     👇👇👇', parse_mode='Markdown',reply_markup=keyboard)
    elif c.data == 'Мадам crystals\n1г 3900р':
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in
        ['Кировск / КАО','Нефты / САО','Ленинск / ЛАО','Чкаловск / ОАО','Назад ','🏠Главное меню']])
        a = 'Вы выбрали:' + '\n' + 13*'➖' + '\nСумма руб.: 3900   \nМадам crystals - 1г     '
        bot.edit_message_text(
        chat_id=c.message.chat.id,
        message_id=c.message.message_id,
        text=a + '\n' + 13*'➖' + '\nВыберите район:\n     👇👇👇', parse_mode='Markdown',reply_markup=keyboard)
    elif c.data == 'Мадам crystals\n2г 6700р':
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in
        ['Кировск / КАО','Ленинск / ЛАО','Назад ','🏠Главное меню']])
        a = 'Вы выбрали:' + '\n' + 13*'➖' + '\nСумма руб.: 6700   \nМадам crystals - 2г     '
        bot.edit_message_text(
        chat_id=c.message.chat.id,
        message_id=c.message.message_id,
        text=a + '\n' + 13*'➖' + '\nВыберите район:\n     👇👇👇', parse_mode='Markdown',reply_markup=keyboard)
    elif c.data == 'Меф кристаллический\n1г 2750р':
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in
        ['Кировск / КАО','Нефты / САО','Ленинск / ЛАО','Чкаловск / ОАО','Назад ','🏠Главное меню']])
        a = 'Вы выбрали:' + '\n' + 13*'➖' + '\nСумма руб.: 6700   \nМеф кристаллический - 1г      '
        bot.edit_message_text(
        chat_id=c.message.chat.id,
        message_id=c.message.message_id,
        text=a + '\n' + 13*'➖' + '\nВыберите район:\n     👇👇👇', parse_mode='Markdown',reply_markup=keyboard)
    elif c.data == 'Меф кристаллический\n2г 5000р':
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in
        ['Нефты / САО','Назад ','🏠Главное меню']])
        a = 'Вы выбрали:' + '\n' + 13*'➖' + '\nСумма руб.: 6700   \nМеф кристаллический - 2г      '
        bot.edit_message_text(
        chat_id=c.message.chat.id,
        message_id=c.message.message_id,
        text=a + '\n' + 13*'➖' + '\nВыберите район:\n     👇👇👇', parse_mode='Markdown',reply_markup=keyboard)
    elif c.data == 'Меф Мука\n1г 1800р':
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in
        ['Кировск / КАО','Нефты / САО','Ленинск / ЛАО','Назад ','🏠Главное меню']])
        a = 'Вы выбрали:' + '\n' + 13*'➖' + '\nСумма руб.: 1800   \nМеф Мука - 1г        '
        bot.edit_message_text(
        chat_id=c.message.chat.id,
        message_id=c.message.message_id,
        text=a + '\n' + 13*'➖' + '\nВыберите район:\n     👇👇👇', parse_mode='Markdown',reply_markup=keyboard)
    elif c.data == 'Меф Мука\n2г 3200р':
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in
        ['Нефты / САО','Ленинск / ЛАО','Назад ','🏠Главное меню']])
        a = 'Вы выбрали:' + '\n' + 13*'➖' + '\nСумма руб.: 3200   \nМеф Мука - 2г        '
        bot.edit_message_text(
        chat_id=c.message.chat.id,
        message_id=c.message.message_id,
        text=a + '\n' + 13*'➖' + '\nВыберите район:\n     👇👇👇', parse_mode='Markdown',reply_markup=keyboard)
    elif c.data == '💊Пилюли👄' or c.data == ' Назад':
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in
        ['2шт 2600 руб','5шт 5500 руб','10шт 10000 руб','25шт 20500 руб','Другая категория','🏠Главное меню']])
        bot.edit_message_text(
        chat_id=c.message.chat.id,
        message_id=c.message.message_id,
        text='{:^45}'.format('💊Пилюли👄') + '\n' + 13*'➖' + '\nВ наличии👇👇👇' '\n' + 13*'➖' + '\n*Трансформеры пилюли*\n2шт за 2600 руб\n5шт за 5500 руб\n10шт за 10000 руб\n25шт за 20500 руб'+ '\n'
        + 13*'➖' + '\n     👇👇👇', parse_mode='Markdown',reply_markup=keyboard)
    elif c.data == '2шт 2600 руб':
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in
        ['Кировск / КАО','Чкаловск / ОАО',' Назад','🏠Главное меню']])
        a = 'Вы выбрали:' + '\n' + 13*'➖' + '\nСумма руб.: 2600   \nТрансформеры пилюли - 2шт        '
        bot.edit_message_text(
        chat_id=c.message.chat.id,
        message_id=c.message.message_id,
        text=a + '\n' + 13*'➖' + '\nВыберите район:\n     👇👇👇', parse_mode='Markdown',reply_markup=keyboard)
    elif c.data == '5шт 5500 руб':
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in
        ['Кировск / КАО','Ленинск / ЛАО','Чкаловск / ОАО',' Назад','🏠Главное меню']])
        a = 'Вы выбрали:' + '\n' + 13*'➖' + '\nСумма руб.: 5500   \nТрансформеры пилюли - 5шт        '
        bot.edit_message_text(
        chat_id=c.message.chat.id,
        message_id=c.message.message_id,
        text=a + '\n' + 13*'➖' + '\nВыберите район:\n     👇👇👇', parse_mode='Markdown',reply_markup=keyboard)
    elif c.data == '10шт 10000 руб':
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in
        ['Кировск / КАО','Ленинск / ЛАО','Чкаловск / ОАО',' Назад','🏠Главное меню']])
        a = 'Вы выбрали:' + '\n' + 13*'➖' + '\nСумма руб.: 10000   \nТрансформеры пилюли - 10шт        '
        bot.edit_message_text(
        chat_id=c.message.chat.id,
        message_id=c.message.message_id,
        text=a + '\n' + 13*'➖' + '\nВыберите район:\n     👇👇👇', parse_mode='Markdown',reply_markup=keyboard)
    elif c.data == '25шт 20500 руб':
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in
        ['Чкаловск / ОАО',' Назад','🏠Главное меню']])
        a = 'Вы выбрали:' + '\n' + 13*'➖' + '\nСумма руб.: 20500   \nТрансформеры пилюли - 25шт        '
        bot.edit_message_text(
        chat_id=c.message.chat.id,
        message_id=c.message.message_id,
        text=a + '\n' + 13*'➖' + '\nВыберите район:\n     👇👇👇', parse_mode='Markdown',reply_markup=keyboard)
    elif c.data == 'СУРГУТ' or c.data == 'Другая категория ':
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in
        ['🌿Природа💨','❄Кристалы/Порошки❄','🏠Главное меню']])
        bot.edit_message_text(
        chat_id=c.message.chat.id,
        message_id=c.message.message_id,
        text='Выберите категорию товара:'+ '\n' + 13*'➖' + '\nВ наличии👇👇👇', parse_mode='Markdown',reply_markup=keyboard)
    elif c.data == '❄Кристалы/Порошки❄' or c.data == ' Назад ':
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in
        ['Мадам crystals\n1 г 3900р','Мадам crystals\n2 г 6700р','Другая категория ','🏠Главное меню']])
        bot.edit_message_text(
        chat_id=c.message.chat.id,
        message_id=c.message.message_id,
        text='{:^45}'.format('❄Кристалы/Порошки❄') + '\n' + 13*'➖' + '\nВ наличии👇👇👇' '\n' + 13*'➖' + '\n*Мадам crystals*\n1г за 3900 руб\n2г за 6700 руб'
        + '\n' + 13*'➖'
        + '\n     👇👇👇', parse_mode='Markdown',reply_markup=keyboard)
    elif c.data == 'Мадам crystals\n1 г 3900р':
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in
        ['Солнечный','Автомобилист',' Назад ','🏠Главное меню']])
        a = 'Вы выбрали:' + '\n' + 13*'➖' + '\nСумма руб.: 3900   \nМадам crystals - 1г     '
        bot.edit_message_text(
        chat_id=c.message.chat.id,
        message_id=c.message.message_id,
        text=a + '\n' + 13*'➖' + '\nВыберите район:\n     👇👇👇', parse_mode='Markdown',reply_markup=keyboard)
    elif c.data == 'Мадам crystals\n2 г 6700р':
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in
        ['Солнечный','Автомобилист',' Назад ','🏠Главное меню']])
        a = 'Вы выбрали:' + '\n' + 13*'➖' + '\nСумма руб.: 6700   \nМадам crystals - 2г     '
        bot.edit_message_text(
        chat_id=c.message.chat.id,
        message_id=c.message.message_id,
        text=a + '\n' + 13*'➖' + '\nВыберите район:\n     👇👇👇', parse_mode='Markdown',reply_markup=keyboard)
    elif c.data == '🌿Природа🌿' or c.data == ' Назад  ':
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in
        ['AK47 1 г 1200р','АК47 3 г 2800р','Другая категория ','🏠Главное меню']])
        bot.edit_message_text(
        chat_id=c.message.chat.id,
        message_id=c.message.message_id,
        text='{:^45}'.format('🌿Природа🌿') + '\n' + 13*'➖' + '\nВ наличии👇👇👇' '\n' + 13*'➖' + '\n*New York ШИШ*\n1г за 1400 руб\n3г за 4750 руб \n4г за 5850 руб\n5г за 6600 руб\n\n*АК47*\n1г 1200р\n3г 2800р\n\n*Porshe Гарик*\n4г за 4200 руб\n6г за 5500 руб'+ '\n' + 13*'➖'
        + '\n     👇👇👇', parse_mode='Markdown',reply_markup=keyboard)
    elif c.data == 'AK47 1 г 1200р':
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in
        ['Солнечный','Автомобилист',' Назад  ','🏠Главное меню']])
        a = 'Вы выбрали:' + '\n' + 13*'➖' + '\nСумма руб.: 1200  \nAK47 - 1г           '
        bot.edit_message_text(
        chat_id=c.message.chat.id,
        message_id=c.message.message_id,
        text=a + '\n' + 13*'➖' + '\nВыберите район:\n     👇👇👇', parse_mode='Markdown',reply_markup=keyboard)
    elif c.data == 'АК47 3 г 2800р':
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in
        ['Солнечный',' Назад  ','🏠Главное меню']])
        a = 'Вы выбрали:' + '\n' + 13*'➖' + '\nСумма руб.: 2800   \nAK47 - 3г           '
        bot.edit_message_text(
        chat_id=c.message.chat.id,
        message_id=c.message.message_id,
        text=a + '\n' + 13*'➖' + '\nВыберите район:\n     👇👇👇', parse_mode='Markdown',reply_markup=keyboard)
    elif c.data == 'Солнечный':
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in
        ['🐤Qiwi','💰BitCoin','Другая категория ','🏠Главное меню']])
        f = c.message.text
        bot.edit_message_text(
        chat_id=c.message.chat.id,
        message_id=c.message.message_id,
        text=f[0:65] + '\nРайон: Солнечный     ' + '\n' + 13*'➖' + '\nВыберите способ оплаты:\n     👇👇👇', parse_mode='Markdown',reply_markup=keyboard)
    elif c.data == 'Автомобилист':
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in
        ['🐤Qiwi','💰BitCoin','Другая категория ','🏠Главное меню']])
        f = c.message.text
        bot.edit_message_text(
        chat_id=c.message.chat.id,
        message_id=c.message.message_id,
        text=f[0:65] + '\nРайон: Автомобилист  ' + '\n' + 13*'➖' + '\nВыберите способ оплаты:\n     👇👇👇', parse_mode='Markdown',reply_markup=keyboard)





if __name__ == '__main__':
    bot.polling(none_stop=True)
