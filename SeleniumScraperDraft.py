import csv
from getpass import getpass
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import pandas as pd
import openpyxl
df = pd.DataFrame([[11, 21, 31], [12, 22, 32], [31, 32, 33]],
                  index=['one', 'two', 'three'], columns=['a', 'b', 'c'])

print(df)

def get_tweet_data(card):
    #Extractin data from card
    username = card.find_element(By.XPATH, './/span').text
    handle = card.find_element(By.XPATH, './/span[contains(text(), "@")]').text
    try:
        postdate = card.find_element(By.XPATH, './/time').get_attribute('datetime')
    except NoSuchElementException:
        return
    text = card.find_element(By.XPATH, './/div[2]/div[2]/div[2]').text
    reply_cnt = card.find_element(By.XPATH, './/div[@data-testid="reply"]').text
    retweet_cnt = card.find_element(By.XPATH, './/div[@data-testid="retweet"]').text
    like_cnt = card.find_element(By.XPATH, './/div[@data-testid="like"]').text

    tweet = (username, handle, postdate, text, reply_cnt, retweet_cnt, like_cnt)
    return tweet

def printAndSetCard(card):
    username = card.find_element(By.XPATH, './/span').text
    handle = card.find_element(By.XPATH, './/span[contains(text(), "@")]').text
    try:
        postdate = card.find_element(By.XPATH, './/time').get_attribute('datetime')
    except NoSuchElementException:
        return
    text = card.find_element(By.XPATH, './/div[2]/div[2]/div[2]').text
    reply_cnt = card.find_element(By.XPATH, './/div[@data-testid="reply"]').text
    retweet_cnt = card.find_element(By.XPATH, './/div[@data-testid="retweet"]').text
    like_cnt = card.find_element(By.XPATH, './/div[@data-testid="like"]').text

    tweet = (username, handle, postdate, text, reply_cnt, retweet_cnt, like_cnt)
    print(username)
    print(handle)
    print(postdate) 
    print(text) 
    print(reply_cnt)
    print(retweet_cnt)
    print(like_cnt)
    return

PATH = '/Users/roquereblando/Downloads/chromedriver'
#chrome
driver = Chrome(PATH)
driver.get('https://www.twitter.com/login')
driver.maximize_window()

sleep(4)

username = driver.find_element(By.XPATH,'//input[@autocomplete="username"]')
username.click()
username.send_keys('Harry_Reblando')
username.send_keys(Keys.RETURN)
sleep(1)
password = driver.find_element(By.XPATH,'//input[@autocomplete="current-password"]')
password.click()
password.send_keys("Roqueoctober911$")
password.send_keys(Keys.RETURN)
sleep(1)
search = driver.find_element(By.XPATH, '//input[@enterkeyhint = "search"]')
search.click()
search.send_keys("APPL")
search.send_keys(Keys.RETURN)
sleep(1)
driver.find_element(By.LINK_TEXT, 'Latest').click()
sleep(1)

sleep(1)

# data = []
# tweet_ids = set()
# page_cards = driver.find_elements(By.XPATH, '//div[@data-testid="cellInnerDiv"]')
# for card in page_cards:
#         tweet = get_tweet_data(card)
#         tweet_id = ''.join(tweet)
#         if tweet_id not in tweet_ids:
#             data.append(tweet)


data = []
tweet_ids = set()
last_position = driver.execute_script("return window.pageYOffset;")
scrolling = True
count = 0
sleep(1)
while count < 3:
    page_cards = driver.find_elements(By.XPATH, '//div[@data-testid="cellInnerDiv"]')
    for card in page_cards:
        tweet = get_tweet_data(card)
        tweet_id = ''.join(tweet)
        if tweet_id not in tweet_ids:
            printAndSetCard(card)
            data.append(tweet)
    driver.execute_script('window.scrollBy(0, 2000);')
    count += 1
    







# getting tweet data test



# cards = driver.find_elements(By.XPATH, '//div[@data-testid="cellInnerDiv"]')
# sleep(1)
# card = cards[0]
# #username
# print(card.find_element(By.XPATH, './/span').text)
# #usertage
# print(card.find_element(By.XPATH, './/span[contains(text(), "@")]').text)
# #Time stamp
# print(card.find_element(By.XPATH, './/time').get_attribute('datetime'))
# # print(card.find_element(By.XPATH, './/div[2]/div[2]/div[2]').text)  #Another way of retreiving the tweet text
# #The tweet text
# print(card.find_element(By.XPATH, './/div[@data-testid="tweetText"]').text)
# #replycount
# print(card.find_element(By.XPATH, './/div[@data-testid="reply"]').text)
# #retweet count
# print(card.find_element(By.XPATH, './/div[@data-testid="retweet"]').text)
# #like count
# print(card.find_element(By.XPATH, './/div[@data-testid="like"]').text)



# ***************** Project Notes *********************
