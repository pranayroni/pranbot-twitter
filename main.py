import gspread
from lib2to3.pgen2 import token
from twitter import *
import random
from random import randrange



consumer_key = 'key'
consumer_secret = 'key'
token = 'key'
token_secret = 'key'
gc = gspread.service_account('credentials.json')
t = Twitter(
    auth=OAuth(token, token_secret, consumer_key, consumer_secret))
wks = gc.open("pranbot-twitter").sheet1




tweets = wks.col_values(1)


i = randrange(len(tweets))

next_tweet = tweets[i]
t.statuses.update(status=next_tweet)

wks.delete_row(i+1)





