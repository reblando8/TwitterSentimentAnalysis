import tweepy
import configparser
import pandas as pd
# read configs
config = configparser.ConfigParser()
config.read('config.ini')

api_key = 'kJoL4Xq7umeCUuNv8LDy8aP9G'
api_key_secret = 'P6d4MCWzIRQlnWTSO06jgKyyAwfKep7FG3kwNtjlIblMMv1XF8'

access_token = '1589711541858754560-yTjOdrvwrMHVj76qYyftUS8Pjmw7lF'
access_token_secret = 'faviBsCdNVjoeYaqqMqpUALFkpr0W2YbbGnFo87kppX8S'


# authentification.
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("working")
except:
    print("something wrong")

searchMethod = "1"

while (searchMethod == "1" or searchMethod == "2"):
    searchMethod = input("Search by User: 1 || Search by ticker: 2 || Exit: 0")
    if searchMethod == "1":
        # searches the actual tweets from the tweets and replies section on a user account.
        user = input("User: ")
        limit = 10
        tweets = tweepy.Cursor(api.user_timeline, screen_name = user, count = 15, tweet_mode = 'extended').items(limit)
        columns = ['User', 'Data']
        data = []
        for tweet in tweets:
            data.append([tweet.user.screen_name, tweet.full_text])
        df = pd.DataFrame(data, columns = columns)
        print(df)
        df.to_csv('/Users/roquereblando/PersonalProjects/data.csv')

    if searchMethod == "2":
        keyword = input("Ticker: ")
        keyword = '$' + keyword
        limit = 10
        tweets = tweepy.Cursor(api.search_tweets, q = keyword, count = 15, tweet_mode = 'extended').items(limit)
        columns = ['User', 'Data']
        data = []
        for tweet in tweets:
            data.append([tweet.user.screen_name, tweet.full_text])
        df = pd.DataFrame(data, columns = columns)
        print(df)
        df.to_csv('/Users/roquereblando/PersonalProjects/data.csv')
    else:
        print("Bye")



