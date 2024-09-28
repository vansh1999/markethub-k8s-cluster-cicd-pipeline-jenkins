# MarketHub : Financial News and Live Stock Price Application

A Django-based web application that fetches real-time financial news from various RSS feeds (20+) and provides live updates on NIFTY, SENSEX and other international market prices with auto-refresh functionality. The app also features pagination for news and real-time index tracking with dynamic price color highlighting.

## Features
Live Nifty and Sensex Prices: Real-time updates for Nifty and Sensex every 2 seconds using AJAX.
Color-coded Price Movements: Green for price increase, red for decrease, and black for no change.
Financial News Aggregation: Fetches the latest financial news from various RSS feeds, including Indian, Asian, and US markets.
Pagination for News: Displays news with pagination to enhance readability.
AJAX-based Auto-refresh: Real-time updates without refreshing the entire page.
Responsive Design: Built with Bootstrap for responsive and mobile-friendly UI.

## Technologies Used
Python: Backend logic
Django: Web framework
JavaScript (AJAX/jQuery): For dynamic and real-time content updates
Bootstrap: Frontend for responsive design
RSS Feeds: To pull in real-time financial news
JSON: To serve real-time stock data via APIs

## Screenshots
![Screenshot 2024-09-26 at 9 50 04 PM](https://github.com/user-attachments/assets/98f07027-c6b7-4d58-bc8d-bd53b8fa8469)

## Installation and Setup
To get a copy of the project up and running on your local machine, follow these steps.

### Prerequisites

Python 3.x

Django 4.x

pip (Python package installer)

### Steps to Install

1. Clone the Repository

``` $ git clone https://github.com/vansh1999/markethub.git ```

2. Navigate to the Project Directory:

``` $ cd markethub ```

3. Create a Virtual Environment

``` $ python3 -m venv env ```

4. Activate the Virtual Environment

``` $ source env/bin/activate  # For Linux/MacOS ```

``` $ env\Scripts\activate      # For Windows ```

5. Install Dependencies

This command will install all the packages listed in the requirements.txt file, ensuring that the correct versions of each package are used.

``` $ pip install -r requirements.txt ``` 

6. Run Migrations

``` $ python manage.py migrate ```

7. Run the Development Server

``` $ python manage.py runserver ```

When running - Access the App

8. Open a web browser and go to: http://127.0.0.1:8000

### Project Structure

```
markethub/
│
├── news/                  # Django app for financial news
│   ├── migrations/        # Database migrations
│   ├── templates/         # HTML templates
                └── base.html
                └── home.html
│   ├── views.py           # View logic including fetching news and pagination
│   └── urls.py            # URL routes
│
├── markethub/             # project
│   └── urls.py/
    └── settings.py/
├── manage.py              # Django management script
|─── requirements.txt      # List of dependencies
|─── README.md             # Project README file
```

### RSS Feeds Used

This project aggregates financial news from the following RSS feeds:

         Indian Markets
        'https://economictimes.indiatimes.com/markets/rssfeeds/1977021501.cms',
        'https://economictimes.indiatimes.com/rssfeedsdefault.cms',
        'https://economictimes.indiatimes.com/prime/money-and-markets/rssfeeds/62511286.cms',
        'https://www.moneycontrol.com/rss/latestnews.xml',
        'https://www.business-standard.com/rss/home_page_top_stories.rss',
        'https://www.livemint.com/rss/markets',
        'https://www.livemint.com/rss/money',
        'https://www.thehindubusinessline.com/news/feeder/default.rss',
        'https://economictimes.indiatimes.com/markets/rssfeeds/1977021501.cms',
        'https://www.business-standard.com/rss/markets-106.rss',
        'https://feeds.feedburner.com/ndtvprofit-latest',
        'https://economictimes.indiatimes.com/markets/stocks/rssfeeds/2146842.cms',
        'https://www.ndtvprofit.com/stories.rss',
        'https://www.thehindu.com/business/Economy/feeder/default.rss',
        'https://www.thehindu.com/business/markets/feeder/default.rss',
        'https://economictimes.indiatimes.com/wealth/mutual-funds/rssfeeds/49995327.cms',
        'https://economictimes.indiatimes.com/tech/funding/rssfeeds/78570550.cms',
        'https://economictimes.indiatimes.com/wealth/personal-finance-news/rssfeeds/49674901.cms',
        'https://economictimes.indiatimes.com/wealth/rssfeeds/837555174.cms',
        

         Asian Markets
        'https://www.reuters.com/markets/asia/?format=xml',
        'https://www.scmp.com/rss/2/feed',

         US Markets
        'https://www.reuters.com/markets/us?format=xml',
        'https://www.cnbc.com/id/10001147/device/rss/rss.html',
        'https://feeds.a.dj.com/rss/RSSMarketsMain.xml',
        'https://feeds.finance.yahoo.com/rss/2.0/headline?s=^DJI&region=US&lang=en-US',

         not working 
        'https://www.business-standard.com/rss/markets-106.rss',
        'https://www.business-standard.com/rss/economy-102.rss',
        'https://www.business-standard.com/rss/finance-103.rss',
        'https://www.business-standard.com/rss/finance/personal-finance-10313.rss',
        'https://www.business-standard.com/rss/finance/investment-10315.rss',
        'https://www.business-standard.com/rss/markets-106.rss',
        'https://www.business-standard.com/rss/markets/commodities-10608.rss',
        'https://www.business-standard.com/rss/markets/stock-market-news-10618.rss',

### Contributing

If you'd like to contribute to this project:

1. Fork the repository.
2. Create a new feature branch (git checkout -b <feature-branch>).
3. Make your changes and commit them (git commit -m 'Add some feature / changes').
4. Push to the branch (git push origin feature-branch).
5. Open a pull request.


### Contact

For any queries or feedback, feel free to contact me at:

Email: vansh.bhardwaj1999@gmail.com

Twitter: [@heyyvanshh] (https://x.com/heyyvanshh)



