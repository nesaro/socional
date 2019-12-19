import sys
import datetime
import PyRSS2Gen
import os
import os.path

PATH = '/home/nesaro/wiki/'

def file_to_rssitem(x):
    full_path = os.path.join(PATH,x)
    with open(full_path) as f:
        content = f.read()

    created_timestamp = os.path.getctime(full_path)
    created = datetime.datetime.fromtimestamp(created_timestamp)

    return PyRSS2Gen.RSSItem(title=x,
                             link=x,
                             description=content[:10],
                             guid=PyRSS2Gen.Guid(x),
                             pubDate=created)

rss = PyRSS2Gen.RSS2(
    title = "Andrew's PyRSS2Gen feed",
    link = "http://www.dalkescientific.com/Python/PyRSS2Gen.html",
    description = "The latest news about PyRSS2Gen, a "
                  "Python library for generating RSS2 feeds",
    lastBuildDate = datetime.datetime.now(),
    items = [file_to_rssitem(x) for x in os.listdir(PATH) if any(x.endswith(y) for y in ('md', 'txt'))]
    )

rss.write_xml(sys.stdout)
