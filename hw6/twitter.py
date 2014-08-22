# HW 6: twitter

import tweepy

#First parameter is Consumer Key, second is Consumer Secret 
auth = tweepy.OAuthHandler('BjTweq5EYaXCgPmILfN0jxPaS', '8fmlBO5QUY9sP2NCLHVaszEXgHSq8moarQ60K7wCK2Z1zOWqQA')
auth.set_access_token('2745459493-1zu9IBaYrfjZacrZCGhIQuPFGskoctyS9TTjv6N', 'LtqVcUdPrvXyTcaNYNPuotph0IpNMjEjp8YLn53Cx1Duq')    
api = tweepy.API(auth)

#Get the target
nate_jensen = api.get_user('NateMJensen')
nate_friends = api.friends(id=nate_jensen.screen_name)

for f in nate_friends:
  #Note I am handling UTF encoded strings so I convert them to ASCII-compatible for my mac
  friend[f] = "{0}".format(f.screen_name.encode('ascii', 'ignore'))
