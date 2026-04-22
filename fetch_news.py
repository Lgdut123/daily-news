import requests
import feedparser
from datetime import datetime

# Constants
NEWS_API_KEY = 'your_api_key_here'

# Categories to filter by
CATEGORIES = ['AI', 'Robotics', 'Basic Science', 'Physics', 'Biology', 'Chemistry', 'Medical', 'Aerospace', 'Psychology', 'Sociology', 'Information Engineering']

# Function to fetch news from News API

def fetch_news_api():
    url = f'https://newsapi.org/v2/everything?q=technology&apiKey={NEWS_API_KEY}'
    response = requests.get(url)
    return response.json().get('articles', [])

# Function to fetch news from RSS feeds

def fetch_news_rss():
    feeds = [
        'https://feeds.feedburner.com/techcrunch/',
        'https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml',
        'https://www.wired.com/feed/rss' 
    ]
    articles = []
    for feed in feeds:
        rss = feedparser.parse(feed)
        articles.extend(rss.entries)
    return articles

# Consolidate news from multiple sources

def get_filtered_news():
    articles = fetch_news_api() + fetch_news_rss()
    filtered_articles = []
    for article in articles:
        # Example filtering logic
        if any(category.lower() in article.get('title', '').lower() for category in CATEGORIES):
            filtered_articles.append({
                'Category': article.get('category', 'Unknown'),
                'Title': article.get('title', 'No Title'),
                'Summary': article.get('description', 'No Summary'),
                'Source': article.get('source', {}).get('name', 'Unknown'),
                'Link': article.get('url', ''),
                'PublishedAt': article.get('publishedAt', datetime.now().isoformat()),
            })
    return filtered_articles[:20]  # Limit to 20

# Example usage
if __name__ == '__main__':
    news = get_filtered_news()
    for item in news:
        print(item)