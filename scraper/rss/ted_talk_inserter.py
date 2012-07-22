from pymongo import Connection
from BeautifulSoup import BeautifulSoup
import urllib
import md5

mongo_conn = Connection('localhost:27017')
video_content_coll = mongo_conn['content']['videos']
# Read the whole page.
data = urllib.urlopen('http://www.ted.com/talks/quick-list').read()
# Parse it
soup = BeautifulSoup(data)

# Find the table with the data
table = soup.findAll('table', attrs= {"class": "downloads notranslate"})[0]
# Get the rows, skip the first one
rows = table.findAll('tr')[1:]

# For each row, get the data
# And store it somewhere
for row in rows:
    
    try:
        cells = row.findAll('td')
        item = {}
        item['links'] =  cells[4].findAll('a')[0]['href']  # [a['href'] for a in cells[4].findAll('a')]	
        _id = md5.md5(item['links']).hexdigest() 
        item['_id'] = _id
        item['source'] = 'TED'
        item['date'] = cells[0].text
        item['title'] = cells[2].text
        item['duration'] = cells[3].text
        video_content_coll.update({'_id': _id}, item, upsert=True)
    except:
        continue
#    video_sources_coll.upsert(item)

