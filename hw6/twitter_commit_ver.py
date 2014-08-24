# HW 6: twitter

import tweepy
import time
import csv # to handle csv files

#First parameter is Consumer Key, second is Consumer Secret 

auth = tweepy.OAuthHandler('BjTweq5EYaXCgPmILfN0jxPaS', '8fmlBO5QUY9sP2NCLHVaszEXgHSq8moarQ60K7wCK2Z1zOWqQA')
auth.set_access_token('2745459493-1zu9IBaYrfjZacrZCGhIQuPFGskoctyS9TTjv6N', 'LtqVcUdPrvXyTcaNYNPuotph0IpNMjEjp8YLn53Cx1Duq')    
api = tweepy.API(auth)


# Create a csv file to store the data
headers = ["id", "followers_count"]

# Where do we save info?
filename = "twitter.csv"
readFile = open(filename, 'a')
csvwriter = csv.writer(readFile)
csvwriter.writerow(headers)

# Get the target
betsy = api.get_user('BetsySinclair1')

# Get the followers of the target
betsy_followers = api.followers_ids(id=betsy.screen_name)

# Get the followers of the followers
followers_count= {}
for f in range(100):
 time.sleep(10) #Suspend execution for 100 seconds
 followers_count[betsy_followers[f]] = api.get_user(id=betsy_followers[f]).followers_count

csvwriter.writerows(followers_count.items())

import operator
sorted_count  = sorted(followers_count.iteritems(), key = operator.itemgetter(1), reverse=True)
print sorted_count[0]  # This will return the most followed follower of the target.

# Find The most active user that your target follows.
betsy_friends = api.friends_ids(id='BetsySinclair1')
followers = {}
for f in range(len(betsy_friends)):
 time.sleep(10)
 followers[betsy_friends[f]] = api.get_user(id=betsy_friends[f]).followers_count

csvwriter.writerows(followers.items())  

sorted_count = sorted(followers.iteritems(), key = operator.itemgetter(1), reverse=True)
print sorted_count[0] # This returns the most followed friend of the target