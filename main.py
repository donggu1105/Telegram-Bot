import telepot

token = "1698758222:AAFbYkMBmDck-bP_wi7vlayqyZ5c0rGn5U0" # 봇의 주민등록번호
mc = "1611694077" # 나의 이름
bot = telepot.Bot(token) # 봇을 구동하기위해 껍데기 + token = > 진정한 봇


def handle(msg):

    print(msg)
    bot.sendMessage(msg["from"]["id"], msg["text"])

bot.message_loop(handle)



while True:
    pass



