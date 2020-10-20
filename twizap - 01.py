from twilio.rest import Client
from pprint import pprint 
import time
import tweepy
import sys 

##Tweepy
api_key = ""
api_secret_key = ""
access_token = ""
access_secret_token = ""

auth_handler = tweepy.OAuthHandler(consumer_key=api_key, consumer_secret=api_secret_key)
auth_handler.set_access_token(access_token, access_secret_token)

api = tweepy.API(auth_handler)
##Whats-Twilio
account_sid =  ""
auth_token = ""

client = Client(account_sid, auth_token)

from_zap_number = 'whatsapp:+'
to_zap_number = 'whatsapp:+'
##Get Tweet
target = ""
target_user = api.get_user(target)
user_tl = api.user_timeline(screen_name=target_user.screen_name, count=1)
last_tweet_id = user_tl[0].id
#Check New Tweet
while True:
    new_tweet = api.user_timeline(screen_name = target_user.screen_name, since_id = last_tweet_id, count = 1)
    if new_tweet == []:
        print('Nothing new')
        time.sleep(20)
    else:
        try:
            #Send Tweet
            last_tweet_id=new_tweet[0].id
            client.messages.create(body=f"{target_user.screen_name}- Posted:{new_tweet[0].text}",
                                   from_= from_zap_number,
                                   to=to_zap_number)
            print("Sent Tweed")
        except:
            print('Error sending tweet')