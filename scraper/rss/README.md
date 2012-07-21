This is the RSS feed scraper. It collects to a local mongod instance,
and looks for the 'sources database'. In that database it opens
a collection called 'rss_feeds', where it expects documents of the form
{"feed_url": *feed url*}, where feed url is a link to an atom or RSS feed.

It then parses those feeds and stores the first 50 items in the content directory.
The objectID will be a md5hex of the link url to ensure
uniqueness. The content database is called "articles". 

Format for article documents
{_id: md5 hex, url: article url, wordcount: number of words in the article, title: title of article"}

Dependencies:
sudo pip install pymongo
sudo pip install feedparser
sudo pip install lxml
