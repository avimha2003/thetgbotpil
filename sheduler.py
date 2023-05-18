import requests
from datetime import datetime
import pytz
import time
import random

# read the quotes from a gm file
with open('gm.txt', 'r') as f:
  gmline = [line.strip() for line in f]

with open('studystart.txt', 'r') as f:
  studystarttxt = [line.strip() for line in f]

with open('iasfct.txt', 'r') as f:
  iasfcttxt = [line.strip() for line in f]

with open('nap.txt', 'r') as f:
  naptxt = [line.strip() for line in f]

with open('stdtech.txt', 'r') as f:
  stdtechtxt = [line.strip() for line in f]

with open('jk.txt', 'r') as f:
  jktxt = [line.strip() for line in f]

with open('tblend.txt', 'r') as f:
  tblendtxt = [line.strip() for line in f]

with open('rews.txt', 'r') as f:
  rewstxt = [line.strip() for line in f]

with open('cute.txt', 'r') as f:
  cutetxt = [line.strip() for line in f]


def sendmessage(message):
  base_url = "https://api.telegram.org/bot5924114524:AAH1hZCro20SmjHW5KXzB8WC9JC-pDlL4R0/sendmessage?chat_id=-885775007&text=" + message
  requests.get(base_url)
  print("Message is sent")


datetime_in_india = datetime.now(pytz.timezone('Asia/Kolkata'))
print(datetime_in_india)

while True:
  datetime_in_india = datetime.now(pytz.timezone('Asia/Kolkata'))
  if datetime_in_india.hour == 7 and datetime_in_india.minute == 00:
    # send a random quote
    gmtxt = random.choice(gmline)
    sendmessage("Good Morning piluu... Listen.... " + gmtxt +
                " Have a nice Day. ")
  elif datetime_in_india.hour == 10 and datetime_in_india.minute == 00:
    # send a random quote
    studystartline = random.choice(studystarttxt)
    sendmessage("Start your study session Piluuu.. Keep In Mind That " +
                studystartline + " So Study Well. All The Best..")

  elif datetime_in_india.hour == 12 and datetime_in_india.minute == 00:
    iasfctline = random.choice(iasfcttxt)
    sendmessage(
      "WOW! You Did it baal. Now go and eat your lunch. Going good, if you study like this you will defenalty become IAS. Have a look at this Fun Fact about IAS : "
      + iasfctline)

  elif datetime_in_india.hour == 13 and datetime_in_india.minute == 00:
    napline = random.choice(naptxt)
    sendmessage(
      "I guess you are Done with your lunch now, can take a nap now, dont use your phone.. zop atta thod aram kr.. Benefits of Nap :  "
      + napline)
  elif datetime_in_india.hour == 14 and datetime_in_india.minute == 30:
    # napline = random.choice(naptxt)
    sendmessage(
      'How is your day going so far?, i guess its going good.. Now wake up baal, get fresh and start your next study session at 3.'
    )

  elif datetime_in_india.hour == 15 and datetime_in_india.minute == 00:
    stdtechtxtline = random.choice(stdtechtxt)
    sendmessage(
      'Its 3 now. Start your next session now.. Dont feel demotivated baaal, you can do it. i belive in you. Study Tip For You : '
      + stdtechtxtline)

  elif datetime_in_india.hour == 16 and datetime_in_india.minute == 30:
    jktxtline = random.choice(jktxt)
    sendmessage(
      " Listen This : " + jktxtline + "!!!" +
      "  Hureyy.. Now Its your Break time now. go take your tea and start your studies at 5 again till 6 or 6:30"
    )

  elif datetime_in_india.hour == 17 and datetime_in_india.minute == 00:

    sendmessage(
      'Break is over now, Get back to studies. Jusr Imaginne how happy your mom and family will be if you become IAS. atleast dont give up for them.. '
    )

  elif datetime_in_india.hour == 18 and datetime_in_india.minute == 00:
    tblendtxtline = random.choice(tblendtxt)
    sendmessage(
      'WOW!! You are done for today. You Did it. ilove you so much!! i am proud of you my pilluu... now you can do anything you want with your time till 10 '
      + '\n' + tblendtxtline)

  elif datetime_in_india.hour == 20 and datetime_in_india.minute == 00:
    sendmessage(
      'Eat Your Dinner Baaal. You did lot of work today. Maz Bal Damal asel... '
    )

  elif datetime_in_india.hour == 20 and datetime_in_india.minute == 30:
    sendmessage('i\n love \n You ')

  elif datetime_in_india.hour == 22 and datetime_in_india.minute == 00:
    rewstxtline = random.choice(rewstxt)
    sendmessage(
      'Revision Helps you For : ' + rewstxtline + "\n" +
      " Now Have a Revision Session. Go through all stuff u studies Today...")
  elif datetime_in_india.hour == 22 and datetime_in_india.minute == 30:
    sendmessage('Dont get distracted.. ')

  elif datetime_in_india.hour == 23 and datetime_in_india.minute == 30:
    cutetxtline = random.choice(cutetxt)
    sendmessage(
      'OMG! NOW COME HERE MAZI PILUU... I WANNA HUG YOU RN.. I KNEW IT PILUU YOU WILL DO IT.. AND U OFC DID IT. I AM PROUD OF YOU BACHUU.... \n '
      +
      'You Know What Pillu? What make me love you the most? List is Endless but will tell one thing at a day, that is : \n  '
      + cutetxtline)

  time.sleep(60)
