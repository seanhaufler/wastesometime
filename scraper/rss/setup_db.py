from __future__ import print_function
from pymongo import Connection

import sys

"""adds a few rss feeds into the correct collection for testing. This only needs to be run once.
after running this script, start the scraper. """

test_feeds = [
    "http://feeds.feedburner.com/TechCrunch/", # techcrunch
    "http://feeds.feedburner.com/ommalik", # feedburner
    "http://feeds.feedburner.com/avc", # fred wilson
    "http://feeds.arstechnica.com/arstechnica/index", # ars
    "http://feeds.huffingtonpost.com/huffingtonpost/raw_feed", #huffpo
    "http://500hats.com/feed", # dave mcclure
    "http://feeds.feedburner.com/stevecorona", # steve corona,
    "http://feeds.feedburner.com/massivegreatness", # MG Siegler
    "http://feeds.feedburner.com/dcurtis" #Dcurtis
    ]
              



if __name__ == '__main__':
    try: 
        # this is localhost for now
        conn = Connection()
        source_db = conn.sources
        rss_coll = source_db.rss_feeds

        print("Setting up feed source collection...")
    
        for feed_url in test_feeds:
            rss_coll.insert({"feed_url": feed_url})

        print("...Done")
        sys.exit(0)
    except Exception:
        print("There was an error!")
        raise
        sys.exit(0)
