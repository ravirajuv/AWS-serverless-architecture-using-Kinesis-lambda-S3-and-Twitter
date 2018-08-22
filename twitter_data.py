import boto3
import json
import logging
import urllib
import time
import codecs
import tweepy
from tweepy import OAuthHandler


auth = OAuthHandler('YOUR_CONSUMER_API_KEY', 'YOUR_CONSUMER_API_KEY_SECRET')
auth.set_access_token('YOUR_ACCESS_TOKEN', 'YOUR_ACCESS_TOKEN_SECRET')

api = tweepy.API(auth)
hashtag = 'photography' # Try with different hashtag

# Creating firehose client
firehose_client = boto3.client('firehose', region_name="us-east-1")

# To push the twitter data to firehose delivery stream
def tweet_processor(tweet):
    try:
        response = firehose_client.put_record(
        DeliveryStreamName='NAME_OF_YOUR_FIREHOSE_DELIVERY_STREAM',
        Record={ 'Data': json.dumps(tweet, ensure_ascii=True)+'\n' } )
        logging.info(response)
    except Exception:
        logging.exception("Couldn't push twitter data to firehose")

# Main function in aws lambda
def lambda_handler(event, context):
    for tweet in tweepy.Cursor(api.search, q=hashtag).items(100):
        print(tweet, tweet._json)
        tweet_processor(tweet._json)
    return 'Twitter data sent to firehose delivery stream!'
