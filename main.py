from pyrogram import Client
from random import randint

app = Client('my_account', api_id=10995021, api_hash='6e6e20c7ac263fe5a4360c599fbed835')
enable = True


@app.on_message()
def hello(client, message):
    global enable
    try:
        # print(message.text)
        if message.text == 'بخواب ربات':
            if message.from_user.username == 'ER_Hamed':
                message.reply('اوکی')
                enable = False
            else:
                message.reply('نخوندم')

        elif message.text == 'بیدار شو ربات':
            if message.from_user.username == 'ER_Hamed':
                message.reply('اوکی')
                enable = True
                return
            else:
                message.reply('نخوندم')

        if enable:
            client.send_chat_action(chat_id=message.chat.id, action="typing")
            if message.text[0:3] == 'بگو':
                message.reply(message.text[3:])
            if message.text[0:4] == 'اسپم':
                try:
                    msg = str(message.text).split()
                    for _ in range(int(msg[2])):
                        message.reply(msg[5])
                except:
                    message.reply('داش نشد بگو: اسپم کن ۱۰ بار بگو سلام')
            elif message.text == 'سلام':
                message.reply('سلام ' + message.from_user.first_name)
            elif message.text == 'عالی ربات':
                message.reply('عالی')

            elif message.text == 'ربات':
                message.reply('جان ربات')
            elif message.text == 'ربات خودم':
                message.reply('جانم ' + message.from_user.first_name)
            elif message.text == 'کجایی':
                message.reply('همین جا')

            elif message.text == 'صلوات بفرست ربات':
                message.reply('اللهم صل علی محمد و آل محمد و عجل فرجهم')

            elif message.text == 'عع شرک':
                message.reply('جان شرک')
            elif message.text == 'شرک':
                message.reply('جان شرک')
            elif message.text == 'خوبی؟':
                message.reply('عالی سید')
            elif message.text == 'عشقی':
                message.reply('فدات سید')
            elif message.text == 'عالی':
                message.reply('عشقی')
            elif '?' in message.text:
                message.reply('نمیدونم حاجی')
            elif message.text == 'آفرین' or message.text == 'افرین':
                message.reply('آفرین به خودم')
            else:
                num = randint(1, 10)
                if num == 1:
                    message.reply('درسته')
                elif num == 2:
                    message.reply('چطوری سید')
                elif num == 3:
                    message.reply('خوبی؟')
                elif num == 4:
                    message.reply('چجولی؟')
                elif num == 5:
                    message.reply('سید')
                elif num == 6:
                    message.reply('اوکی')
                elif num == 7:
                    message.reply('اها')
                elif num == 8:
                    message.reply('باشه')
                elif num == 9:
                    message.reply('متوجه نشدم')
                else:
                    message.reply('چی؟')
    except:
        message.reply('این چیه؟')


app.run()
