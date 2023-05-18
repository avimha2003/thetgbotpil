#"5924114524:AAH1hZCro20SmjHW5KXzB8WC9JC-pDlL4R0"
import telebot
import random
import time

bot = telebot.TeleBot("5924114524:AAH1hZCro20SmjHW5KXzB8WC9JC-pDlL4R0")
with open('mtvt.txt', 'r') as f:
  mtvttxt = [line.strip() for line in f]

with open('jk.txt', 'r') as f:
  jktxt = [line.strip() for line in f]

with open('links.txt', 'r') as f:
  linkstxt = [line.strip() for line in f]


@bot.message_handler(commands=['MotivateMe'])
def MotivateMe(message):
  mtvttxtline = random.choice(mtvttxt)
  bot.send_message(message.chat.id, mtvttxtline)


@bot.message_handler(
  commands=['Hi', 'Hey', 'hi', 'hey'], )
def Hi(message):
  bot.send_message(message.chat.id,
                   "Hello Pilluuu, I am here ALWAYS for you...")


# rss_url = "https://www.newindianexpress.com/Nation/rssfeed/?id=170&getXmlFeed=true"

# @bot.message_handler(commands=['News'])
# def News(message):
#   feed = feedparser.parse(rss_url)
#   latest_post = feed.entries[0]
#   bot.send_message(
#     message.chat.id,
#     latest_post.title + "\n" + latest_post.summary + "\n" + latest_post.link)


@bot.message_handler(commands=['TellMeJoke'])
def TellMeJoke(message):
  jktxtline = random.choice(jktxt)
  bot.send_message(message.chat.id, jktxtline)


@bot.message_handler(commands=['MissingU'])
def MissingU(message):
  linkstxtline = random.choice(linkstxt)
  bot.send_message(message.chat.id, linkstxtline)


@bot.message_handler(commands=['MakeEveryThingOkay'])
def MakeEveryThingOkay(message):
  bot.send_message(message.chat.id,
                   "Making eveything Okay... Take a Deep Breath...")
  for i in reversed(range(10)):
    bot.send_message(message.chat.id, i)
    time.sleep(1)
  bot.send_message(message.chat.id, "Eveything is Fine Now. DW. ")


@bot.message_handler(commands=['Help', 'help'])
def help(message):
  bot.send_message(
    message.chat.id,
    "Hello Piluu.. Here is List of Commands You Can use : \n /Hi \n /MotivateMe \n /TellMeJoke \n /MissingU \n /iloveyou \n /MakeEveryThingOkay \n /showmeyourcode \n /JumpScare \n /DontClick"
  )


@bot.message_handler(commands=['iloveyou', 'ily'])
def iloveyou(message):
  bot.send_message(message.chat.id, " But , Love You More Piluuu.... 10000x")

@bot.message_handler(commands=['showmeyourcode'])
def showmeyourcode(message):
  bot.send_message(message.chat.id, " LOL, Its Confidential...... Needs 10 kisses in row to unlock The Code.. ")

@bot.message_handler(commands=['JumpScare'])
def JumpScare(message):
  jps = ["https://media.tenor.com/4DmLh4-TPMoAAAAC/scare-jump.gif", "https://media.tenor.com/L-UOXYHL2xwAAAAC/jumpscare.gif", "https://i.pinimg.com/originals/1d/32/65/1d32658488e3814fd3a96b3f95024fa3.gif"]
  sjps = random.choice(jps)
  bot.send_message(message.chat.id, sjps)

#
@bot.message_handler(commands=['DontClick'])
def DontClick(message):
  bot.send_message(message.chat.id, "https://media.tenor.com/hZ_ch4aqRyIAAAAC/cute-kawaii.gif")



bot.polling()
