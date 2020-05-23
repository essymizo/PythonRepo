#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The script will delete all tweets from the account that is specified.
Get consumer key and consumer secret token by registering a twitter application at https://dev.twitter.com/apps
@author: EssyMizo
"""

import tweepy

 """Initialize"""
CONSUMER_KEY = 'XXX' 
CONSUMER_SECRET = 'XXX'


 """Delete tweets"""
def batch_delete(api):
    print "Want to delete all tweets from account @%s." % api.verify_credentials().screen_name
    print "y to confirm"
    do_delete = raw_input("> ")
    if do_delete.lower() == 'y':
        for status in tweepy.Cursor(api.user_timeline).items():
            try:
                api.destroy_status(status.id)
               # print "Deleted:", status.id
            except:
                print " Cannot delete:", status.id

if __name__ == "__main__":
   
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    print "Successfully login as: %s" % api.me().screen_name
    
   
    batch_delete(api)

