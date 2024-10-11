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

![Screenshot 2024-09-29 at 9 01 15 AM](https://github.com/user-attachments/assets/5bab1844-e594-4216-8fc0-2d71f630d4aa)

# Installation and Setup

## Option 1: Default Installation

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

5. Install Dependencies : This command will install all the packages listed in the requirements.txt file, ensuring that the correct versions of each package are used.

    ``` $ pip install -r requirements.txt ```
    
7. Run Migrations

    ``` $ python manage.py migrate ```     

8. Run the Development Server

    ``` $ python manage.py runserver ```

When running - Access the App

8. Open a web browser and go to: http://127.0.0.1:8000


## Option 2: Installation Using Docker

### Prerequisites

Docker installed on your machine

### Steps to install Docker

1. Get docker engine using docker.io

    ``` $ sudo apt install docker.io ```

2. Add a group docker and add current user ubuntu

    ``` $ sudo usermod -a -G docker $USER ```

3. Reboot

   ``` $ sudo reboot  ```

### Run Docker

1. Clone the repository and cd

    ``` $ git clone https://github.com/vansh1999/markethub.git ```
   
    ``` $ cd markethub ```

2. Build Dockerfile

   We already have a Dockerfile in our repo, you just need to build and run it

    ``` $ docker build . -t markethub:latest ```

4. Run the container

    ``` $ docker run -d -p 8000:8000 markethub:latest ```


Access the app: Open your browser at http://localhost:8000

Or if using AWS ec2 instance goto <public_ip>:8000

Note -> Add port 8000 at the inbound security group


## Option 3: Installation Using Docker Compose

Installation steps to get docker will be same as above in option 2

1. Install docker compose
   
    ``` $ sudo apt install docker-compose ```
   
We already have a docker-compose.yaml file in our repo, just need run docker compose

3. Run docker compose

    ``` $ docker-compose up -d ```

## Option 4: Pull Prebuilt Docker Image from Docker Hub

If you want to skip building the Docker image yourself, you can pull the prebuilt image directly from Docker Hub, which I had pushed to Docker Hub.

1. Install Docker as mentioned in option 2

2. pull image from docker hub

    ``` $ docker pull vansh1999/markethub ```

   Docker Hub -> https://hub.docker.com/repository/docker/vansh1999/markethub/general

4.  Run the image and start container on port 8000

    ``` $ docker run -d -p 8000:8000 vansh1999/markethub ```


Access the app: Open your browser at http://localhost:8000

Or if using AWS ec2 instance goto <public_ip>:8000


## Project Structure

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
|─── Dockerfile            # Dockerfile to build image
|─── docker-compose.yaml   # YAML file to run with docker-compose
|─── volume                # Volume for our app, Persistent data storage

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


## Jenkins Distributed CICD Pipeline


