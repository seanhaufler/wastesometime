This is the RSS feed scraper. It collects to a local mongod instance,
and looks for the 'sources database'. In that database it opens
a collection called 'rss_feeds', where it expects documents of the form
{"feed_url": *feed url*}, where feed url is a link to an atom or RSS feed.

It then parses those feeds and stores the first 50 items in the content directory.
The objectID will be a md5hex of the blog url, date, and article name, to ensure
uniqueness.

The content database is called "articles". Each document will be aggregated in a collection
by wordcount, in increments of 50 words. e.g an article with 40 words would be in the length50
collection, an article with 5004 words would be in the length5050 collection.

Format for article documents
{_id: md5 hex, url: article url, wordcount: number of words in the article, title: title of article"}
