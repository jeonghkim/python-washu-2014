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
headers = ["post", "publish_date", "author", "url", "post_title", "comment_count"]

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
for date in post_dates:
 d = clean_html(str(date))
#  print d

# Extract author
authors = soup.findAll("span", attrs={'class':'author vcard'})
for author in authors:
 a = clean_html(str(author))
#  print a

 
# Extract url
#petitions = soup.findAll("a", href=re.compile('^/petition'))

urls = soup.findAll(href = re.compile("^http://www.washingtonpost.com/blogs/monkey-cage/wp/2014/08/"))
print len(urls[0])
# for url in urls:
#  u = urls[1][0]
#  print u
 
# Extract post_title
post_titles = soup.findAll("h2", attrs={'class': 'entry-title'})
for title in post_titles:
 p = clean_html(str(title.find("a")))
#  print p
 

 