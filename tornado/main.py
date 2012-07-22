    # Python
import os
import json
import random

# Tornado
import tornado.httpserver
import tornado.ioloop
import tornado.web

# Mongo
import pymongo
from bson import json_util

class Application(tornado.web.Application):
	
    def __init__(self):
        handlers = [
            (r"/", HomeHandler),
            (r"/articles/", ArticleHandler),
            (r"/videos/", VideoHandler),
            (r"/frame/", FrameHandler)
            (r"/search/", DocSearchHandler)

        conn = pymongo.Connection()
        
        self.content = conn.content
        self.articles = self.content.articles
        self.videos = self.content.videos

        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            debug=True,
        )
        tornado.web.Application.__init__(self, handlers, **settings)

class BaseHandler(tornado.web.RequestHandler):
    pass

class HomeHandler(BaseHandler):
	
    def get(self):
        self.render("home.html")

class FrameHandler(BaseHandler):

    def get(self):
        self.render("frametest.html")

class ArticleHandler(BaseHandler):
	
    def get(self):
       	minLenInt = 200
       	maxLenInt = 400

        try:
            minLenInt = int(self.get_argument("minLen"))
            maxLenInt = int(self.get_argument("maxLen"))
        except:
            pass
        coll = self.application.articles
        query = {"$and": [{"wordcount": {"$gte": minLenInt}},
                          {"wordcount": {"$lte": maxLenInt}}]}
        docs = coll.find(query)
        result_arr = []
        for doc in docs:
            result_arr.append(doc)
        self.write(json.dumps(result_arr, default=json_util.default))

class VideoHandler(BaseHandler):
	
    def get(self):
        minTime = 200
        maxTime = 400
		
	try:
            minTime = int(self.get_argument("minTime"))
	    maxTime = int(self.get_argument("maxTime"))
	except:
	    pass
			
	coll = self.application.videos
	query = {"$and": [{"duration": {"$gte": minTime}},
                          {"duration": {"$lte": maxTime}}]}
        docs = coll.find(query)
        result_arr = []
        for doc in docs:
            result_arr.append(doc)

        self.write(json.dumps(result_arr, default=json_util.default))
        
class DocSearchHandler(BaseHandler):
    
    def get(self):
        maxTime = 300
        
        try:
            maxTime = int(self.get_argument('maxTime'))
        except:
            pass
        
        coll = self.application.videos
        query = {"$and": [{"duration": {"$gt": 0}},
                {"duration": {"$lte": maxTime}}]}
        docs = coll.find(query)
        video_result_arr = []
        for doc in docs:
            video_result_arr.append(doc)
            
        maxTime *= 200/60                #200 wpm
        coll = self.application.articles
        query = {"$and": [{"wordcount": {"$gt": 50}},
                {"wordcount": {"$lte": maxTime}}]}
        docs = coll.find(query)
        article_result_arr = []
        for doc in docs:
            article_result_arr.append(doc)
    
        video_len = len(video_result_arr) -1
        vid_one = random.randint(0, video_len)
        vid_two = random.randint(0, video_len)
        
        results = []
        results.append(video_result_arr[vid_one])
        results.append(video_result_arr[vid_two])
        
        article_len = len(article_result_arr) -1
        art_one = random.randint(0, article_len)
        art_two = random.randint(0, article_len)
        art_three = random.randint(0, article_len)
        
        results.append(article_result_arr[art_one])
        results.append(article_result_arr[art_two])
        results.append(article_result_arr[art_three])
        
        self.write(json.dumps(results, default=json_util.default))
        	

def main(port='8080', address='127.0.0.1'):
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(port, address)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
