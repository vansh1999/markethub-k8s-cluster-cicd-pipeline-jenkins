from django.shortcuts import render
import feedparser

# Create your views here.

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

# def home(request):
# 	# make var news_list and get NewsArticle Model and limit number to 50
# 	news_list = NewsArticle.objects.order_by('-published_at')[:50]
# 	# render to home page and pass news_list context
# 	return render(request , 'home.html' , {'news_list' : news_list})




def home(request):
    
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

     ]  # Your list of RSS feeds


    ### working logic for entries with pagination ###
    # all_entries = []
    # for rss_url in rss_urls:
    #     try:
    #         feed = feedparser.parse(rss_url)
    #         all_entries.extend(feed.entries)
    #     except Exception as e:
    #         print(f"Failed to fetch or parse RSS feed from {rss_url}: {e}")
    #         continue

    # all_entries.sort(key=lambda entry: entry.published_parsed, reverse=True)

    ######


    # news logic
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
    paginator = Paginator(all_entries, 50)  # Show 50 news items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'feed': page_obj
    }
    

    return render(request , 'home.html' , context)





