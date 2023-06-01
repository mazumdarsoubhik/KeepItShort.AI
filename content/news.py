from newsapi import NewsApiClient
import pandas as pd
import configparser

def initiate_api(path=""):
    # read configs
    config = configparser.ConfigParser()
    config.read(f'{path}config.ini')

    api_key = config['newsapi']['news_api_key']

    newsapi = NewsApiClient(api_key)

    return newsapi

# all_sources = newsapi.get_sources()

# all_sources_df = pd.DataFrame.from_dict(all_sources['sources'])

# print(all_sources_df[all_sources_df["country"] == "in"])

def get_news_article(limit=10):
    '''
    Return top headlines in list of dictionary format

    '''
    newsapi = initiate_api("../" if __name__ == '__main__' else "")

    top_headlines = newsapi.get_top_headlines(country='in')

    return top_headlines['articles'][:limit]

def get_news_links(limit=10):
    '''
    Returns list of links of top news headlines
    '''
    newsapi = initiate_api("../" if __name__ == '__main__' else "")
    
    top_headlines = newsapi.get_top_headlines(country='in')

    top_headlines_df = pd.DataFrame.from_dict(top_headlines['articles'][:limit])

    news_links = top_headlines_df["url"].to_list()

    return news_links

if __name__ == '__main__':
    # config.read('../config.ini')

    # api_key = config['newsapi']['news_api_key']

    # newsapi = NewsApiClient(api_key)

    # print(get_news_links(5))
    print(get_news_article(1))