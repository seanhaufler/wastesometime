from __future__ import print_function

import lxml.html
import feedparser
from pymongo import Connection
import sys
import time
import md5

# using old style objects, don't see any reason to use new style objects
# as they are a bit slower and I don't need those features
class RssScraper:
    def __init__(self, feeds, limit, coll):
        """Feeds is a list of RSS or Atom feeds, limit is the max articles to
        scrape per feed, and coll is the collection to store the data in."""
        self.feeds = feeds
        self.limit = limit
        self.coll = coll
    def scrape(self):
        for feed in self.feeds:
            parser = feedparser.parse(feed)
            for entry in parser.entries:
                url = entry.link
                _id = md5.md5(url).hexdigest()
                title = entry.title
                wordcount = 0
                # this block filters out all the html tags and counts
                # the words
                for content_part in entry.content:
                    part = lxml.html.fromstring(content_part.value)
                    part_text = part.text_content()
                    part_word_list = part_text.split(" ")
                    wordcount += len(part_word_list)
                print(_id, url, title, wordcount)
                self.coll.update(
                    {"_id": _id},
                    {"$set": {"title": title,
                              "wordcount": wordcount}},
                    upsert = True)

    
def get_feeds(coll):
    return [doc['feed_url'] for doc in coll.find()]

def main():
    try:
        # setup mongo
        conn = Connection()
        source_db = conn.sources
        rss_source_coll = source_db.rss_feeds
        content_db = conn.content
        article_data_coll = content_db.articles

        # setup feed lists
        feeds = get_feeds(rss_source_coll)

        # setup scraper
        scraper = RssScraper(
            feeds,
            50,
            article_data_coll # 50 articles from each for now
        ) 
        
        while True:
            scraper.scrape()
            time.sleep(60 * 10) # sleep for 10 mins
    except KeyboardInterrupt:
        print("Received keyboard interrupt. Exiting...")
        sys.exit(0)
    except Exception:
        print ("There was an error.")
        raise
        sys.exit(1)

if __name__ == '__main__':
    main()
        
    
    
        
    

        
    




