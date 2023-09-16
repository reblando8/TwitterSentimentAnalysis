from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax
import tweepy
import configparser
import pandas as pd

user = 'Veritasium'
limit = 1
tweet = "@HarryReblando I think this day is normal"
tweet_words = []
# process tweet
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



# loading model and tokenizer



# code for setntiment analysisrx


searchMethod = "1"
while (searchMethod == "1" or searchMethod == "2"):
    searchMethod = input("Search by User: 1 || Search by ticker: 2 || Exit: 0\n")
    
    if searchMethod == "1":
        # searches the actual tweets from the tweets and replies section on a user account.
        user = input("User: ")
        limit = 30
        tweets = tweepy.Cursor(api.user_timeline, screen_name = user, count = 40, tweet_mode = 'extended').items(limit)
        columns = ['User', 'Data', 'SentimentVal']
        data = []
        sentimentVal = "Nothing"
        roberta = "cardiffnlp/twitter-roberta-base-sentiment"
        model = AutoModelForSequenceClassification.from_pretrained(roberta)
        tokenizer = AutoTokenizer.from_pretrained(roberta)
        labels = ["Negative", "Neutral", "Positive"]
        count = 1
        for tweet in tweets:
            tweet_words = []
            # tweet_proc = ""
            for word in tweet.full_text.split(' '):
                if word.startswith('@') and len(word) > 1:
                    word = '@user'
                elif word.startswith('http'):
                    word = "http"
                tweet_words.append(word)
                
                
            tweet_proc = " ".join(tweet_words)
            encoded_tweet = tokenizer(tweet_proc, truncation = True, return_tensors = 'pt')
            output = model(**encoded_tweet)
            scores = output[0][0].detach().numpy()
            scores = softmax(scores)
            print(scores)
            
            if scores[0] >= scores[1] and scores[0] >= scores[2]:
                sentimentVal = "Negative"
            elif scores[1] >= scores[0] and scores[1] >= scores[2]:
                sentimentVal = "Neutral"
            elif scores[2] >= scores[0] and scores[2] >= scores[1]:
                sentimentVal = "Positive"
            

            data.append([tweet.user.screen_name, tweet.full_text, sentimentVal])
            # for i in range(len(scores)):
            #     l = labels[i]
            #     s = scores[i]
            #     print(l,s)

        df = pd.DataFrame(data, columns = columns)
        df.to_csv('/Users/roquereblando/PersonalProjects/data.csv')
        print(df)

    if searchMethod == "2":
        tweet_words = []
        keyword = input("Ticker: ")
        keyword = '$' + keyword
        limit = 100
        tweets = tweepy.Cursor(api.search_tweets, q = keyword, count = 150, tweet_mode = 'extended').items(limit)
        columns = ['User', 'Data', 'SentimentVal']
        data = []
        sentimentVal = "Nothing"
        roberta = "cardiffnlp/twitter-roberta-base-sentiment"
        model = AutoModelForSequenceClassification.from_pretrained(roberta)
        tokenizer = AutoTokenizer.from_pretrained(roberta)
        labels = ["Negative", "Neutral", "Positive"]
        for tweet in tweets:

            tweet_words = []
            for word in tweet.full_text.split(' '):
                if word.startswith('@') and len(word) > 1:
                    word = '@user'
                elif word.startswith('http'):
                    word = "http"
                tweet_words.append(word)
            tweet_proc = " ".join(tweet_words)
            encoded_tweet = tokenizer(tweet_proc, return_tensors = 'pt')
            output = model(**encoded_tweet)
            scores = output[0][0].detach().numpy()
            scores = softmax(scores)
            print(scores)
            
            if scores[0] >= scores[1] and scores[0] >= scores[2]:
                sentimentVal = "Negative"
            elif scores[1] >= scores[0] and scores[1] >= scores[2]:
                sentimentVal = "Neutral"
            elif scores[2] >= scores[0] and scores[2] >= scores[1]:
                sentimentVal = "Positive"
            
            data.append([tweet.user.screen_name, tweet.full_text, sentimentVal])
            # for i in range(len(scores)):
            #     l = labels[i]
            #     s = scores[i]
            #     print(l,s)

        df = pd.DataFrame(data, columns = columns)
        df.to_csv('/Users/roquereblando/PersonalProjects/data.csv')
        print(df)
    else:
        print("Bye")




# find tickers from use searches

