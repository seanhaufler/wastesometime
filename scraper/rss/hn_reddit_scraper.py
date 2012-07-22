import feedparser
import webarticle2text
import md5
import time
import sys
import reddit
from pymongo import Connection

mongo = Connection('localhost:27017')
coll = mongo.content.articles

hn_url = 'http://www.reddit.com/r/programming/.json'

def scrape_hn(hn_url):
	parser = feedparser.parse(hn_url)
	for entry in parser.entries:
		url = entry.link
		_id = md5.md5(url).hexdigest()
		title = entry.title
		try:
			body = webarticle2text.extractFromURL(url)
			wordcount = len(body.split(" "))
		except:
			wordcount = -1
		
		coll.update(
		{"_id": _id},
		{"$set": {"title": title,
				  "wordcount": wordcount}},
		upsert = True)
		
		print 'Added url %s' % url

def scrape_reddit():
	docs = reddit.Reddit(user_agent='app').get_front_page(limit=250)
	for item in docs:
		url = item.url
		_id = md5.md5(url).hexdigest()
		title = item.title
		try:
			body = webarticle2text.extractFromURL(url)
			wordcount = len(body.split(" "))
		except:
			wordcount = -1
			
		coll.update(
				{"_id": _id},
				{"$set": {"title": title,
						  "wordcount": wordcount,
						  "url": url}},
				upsert = True)
				
		print 'Added url %s' % url		

if __name__ == '__main__':	

	try:
		while True: 	
		#	scrape_hn(hn_url)
			scrape_reddit()
			time.sleep(600)
		
	except KeyboardInterrupt:
		print("Received keyboard interrupt. Exiting...")
		sys.exit(0)
	except Exception:
		print ("There was an error.")
		raise
		sys.exit(1)
