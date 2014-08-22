# HW 5: How to implement a web crawler
# Jeong

from bs4 import BeautifulSoup
import csv 
from nltk.util import clean_html
import urllib2 
import re

# a blog to scrape?
blog_to_scrape = "http://www.washingtonpost.com/blog/monkey-cage/Archive/201408"

# What info do we want? 
headers = ["publish_date", "author", "url", "post_title", "comment_count", "is_post"]

# Where do we save info?
filename = "monkeycage.csv"
readFile = open(filename, "wb")
csvwriter = csv.writer(readFile)
csvwriter.writerow(headers)

# Open webpage
webpage = urllib2.urlopen(blog_to_scrape)

# Parse it
soup = BeautifulSoup(webpage.read()) # parse with BeautifulSoup
soup.prettify()


# Extract publish_date
post_dates = soup.findAll("span", attrs={'class': 'updated'})
# for date in post_dates:
#  d = clean_html(str(date))

# Extract author
authors = soup.findAll("span", attrs={'class':'author vcard'})
 
# Extract url
urls = soup.findAll("h2")
 
# Extract post_title
post_titles = soup.findAll("h2", attrs={'class': 'entry-title'})

# Extract comment count
comments_count = soup.findAll("a", href=re.compile('comments$'))


for i in range(48)[::-1]: # by adding [::-1], I sort the posts in a chronological way.
 author = authors[i]
 a = clean_html(str(author))
 date = post_dates[i]
 d = clean_html(str(date))
 url = urls[i]
 u = clean_html(str(url.find("a")["href"]))
 title = post_titles[i]
 t = clean_html(str(title.find("a")))
 count = comments_count[i]
 c = clean_html(str(count))
 # is_post: a boolean value that is 1 if your crawler thinks the page is a post
 if authors[i] != "" and post_titles[i] != "" and urls[i] !="":
  p = 1
 else: p = 0
 csvwriter.writerow([d, a, u, t, c, p])

readFile.close()

