import tweepy
import configparser
import json
from content import news
from model import LLM

# read configs
config = configparser.ConfigParser()
config.read('config.ini')


news_links = news.get_news_links()

news_card = LLM.get_news_card(news_links[0])

print(news_card)
