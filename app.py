import configparser
import json
from content import news
from model import LLM
from media import instagram
from PIL import Image
import requests
from io import BytesIO
import os
# from flask import Flask, render_template, request

# read configs
config = configparser.ConfigParser()
config.read('config.ini')

news_articles = news.get_news_article(5)

i=0
for the_article in news_articles:
    print(f"\n\nWorking on {i} news article: {the_article['title']}")

    news_card = LLM.get_news_card(the_article['url'])

    print(f"Got the news card")

    caption = f"{news_card['Headline']}\n\n{news_card['Summary']}\n\nSource: {the_article['source']['name']}"

    response = requests.get(news_card['image_url'])
    image = Image.open(BytesIO(response.content))
    image = image.convert('RGB')
    image.save('output.jpg', 'JPEG')

    post_response = instagram.post_image(url='output.jpg', caption=caption)
    
    print(f"POST RESPONSE:{post_response}")
    print(f"Posted the news")

    os.remove('output.jpg')

    content_log = {**the_article, **news_card}
    with open('post_logs.txt', 'a') as file:
        dict_str = str(content_log)
        file.write(dict_str + '\n')

    print("Finished the news!!!")
    i += 1