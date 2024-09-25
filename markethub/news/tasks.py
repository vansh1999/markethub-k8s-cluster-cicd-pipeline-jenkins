# from background_task import background
# from .views import fetch_rss_feeds
# from .tasks import refresh_rss_feeds


# @background(schedule=60)  # Schedule it to run after 60 seconds initially
# def refresh_rss_feeds():
#     fetch_rss_feeds()  # Call the function that fetches and caches the RSS feeds


# # Schedule the task to refresh news every hour
# refresh_rss_feeds(repeat=3600)  # 3600 seconds = 1 hour