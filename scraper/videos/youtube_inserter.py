from gdata.youtube.service import YouTubeService
from pymongo import Connection
import md5

def get_user_videos(username):
  	yt_service = YouTubeService()
  	uri = 'http://gdata.youtube.com/feeds/api/users/%s/uploads' % username
  	feed = yt_service.GetYouTubeVideoFeed(uri)
	video_obj = {}
	video_obj['source'] = username
	
	while len(feed.entry) > 0:
		for video in feed.entry:
			video_obj['date'] = video.published.text
			video_obj['title'] = video.title.text
			video_obj['duration'] = video.media.duration.seconds
			
			url = video.link[0].href
			
			url = None
			for link in video.link:
				if 'www.youtube.com/watch' in link.href:
					url = link.href
					break
					
			_id = md5.md5(url).hexdigest()
			video_obj['links'] = url
			video_obj['_id'] = _id
			video_content_coll.update({'_id': _id}, video_obj, upsert=True)
			print 'Added url %s with _id %s' % (url, _id)

		try:
			feed = yt_service.GetYouTubeVideoFeed(feed.GetNextLink().href) 
		except:
			break

def run_scrape():
	
	youtube_channels = youtube_names_coll.find()
	
	for channel in youtube_channels:
		get_user_videos(channel['name'])

if __name__ == '__main__':
	
	mongo_conn = Connection('localhost:27117')
	video_content_coll = mongo_conn['content']['videos']
	youtube_names_coll = mongo_conn['sources']['videos']

	youtube_names_coll.insert({'name':'theRSAorg'})
	youtube_names_coll.insert({'name':'TEDtalksDirector'})
	youtube_names_coll.insert({'name':'collegehumor'})
	youtube_names_coll.insert({'name':'PBSoffbook'})
	youtube_names_coll.insert({'name':'UCtelevision'})
	youtube_names_coll.insert({'name':'TheBadAstronomer'})
	youtube_names_coll.insert({'name':'KassemG'})
	
	while True:
		run_scrape()
