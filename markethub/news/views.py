# django imports

from django.shortcuts import render
import feedparser
from news.models import NewsArticle
from django.core.paginator import Paginator
from django.core.cache import cache
from bs4 import BeautifulSoup



def clean_html(raw_html):
    
    # Parse the raw HTML with BeautifulSoup
    soup = BeautifulSoup(raw_html, 'html.parser')

    # Remove all <img> tags (if present)
    for img in soup.find_all('img'):
        img.decompose()  # Remove the img tag completely

    # Return the cleaned text (without any HTML tags)
    return soup.get_text()



def home(request):

    # rss feeds
    
    rss_urls = [

    	# Indian Markets
    	'https://economictimes.indiatimes.com/rssfeedsdefault.cms',
        'https://www.moneycontrol.com/rss/latestnews.xml',
        'https://www.business-standard.com/rss/home_page_top_stories.rss',
        'https://www.livemint.com/rss/markets',
        'https://www.livemint.com/rss/money',
        'https://www.thehindubusinessline.com/news/feeder/default.rss',
        'https://economictimes.indiatimes.com/markets/rssfeeds/1977021501.cms',
        'https://www.business-standard.com/rss/markets-106.rss',
        'https://feeds.feedburner.com/ndtvprofit-latest',

        # Asian Markets
        'https://www.reuters.com/markets/asia/?format=xml',
        'https://www.scmp.com/rss/2/feed',

        # US Markets
        'https://www.reuters.com/markets/us?format=xml',
        'https://www.cnbc.com/id/10001147/device/rss/rss.html',
        'https://feeds.a.dj.com/rss/RSSMarketsMain.xml',
        'https://feeds.finance.yahoo.com/rss/2.0/headline?s=^DJI&region=US&lang=en-US',

     ] 


    # News Logic
    all_entries = []
    seen_titles = set()  # Set to track unique titles or links

    for rss_url in rss_urls:
        try:
            feed = feedparser.parse(rss_url)
            for entry in feed.entries:
                # Use title or link to filter duplicates
                if entry.title not in seen_titles:
                    # Clean the title and description using BeautifulSoup
                    entry.title = clean_html(entry.title)
                    entry.description = clean_html(entry.description)
                    
                    all_entries.append(entry)
                    seen_titles.add(entry.title)  # Mark this title as seen
        except Exception as e:
            print(f"Error fetching {rss_url}: {e}")

    all_entries.sort(key=lambda entry: entry.published_parsed, reverse=True)

    # Cache the combined and filtered entries for 1 hour (3600 seconds)
    cache.set('rss_news', all_entries, timeout=3600)

    # Pagination Logic
    # Show 50 news items per page and next in next and prev
    paginator = Paginator(all_entries, 50)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        # context for news with pagination
        'feed': page_obj
        # context for market prices

    }
    

    return render(request , 'home.html' , context)





