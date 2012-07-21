from __future__ import print_function

import feedparser
from pymongo import Connection
import sys
import time

# using old style objects, don't see any reason to use new style objects
# as they are a bit slower and I don't need those features
class RssScraper:
    def __init__(self, feeds, limit, coll):
        """Feeds is a list of RSS or Atom feeds, limit is the max articles to
        scrape per feed, and coll is the collection to store the data in."""
        self.feeds = feeds
        self.limit = limit
        self.coll = coll

    
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
        print(feeds)
        # setup scraper
        scraper = RssScraper(
            feeds,
            50,
            article_data_coll # 50 articles from each for now
        ) 
        
        while True:
           
            time.sleep(60 * 5) # sleep for 5 mins
    except KeyboardInterrupt:
        print("Received keyboard interrupt. Exiting...")
        sys.exit(0)
    except Exception:
        print ("There was an error.")
        raise
        sys.exit(1)

if __name__ == '__main__':
    main()
        
    
    
        
    

        
    




