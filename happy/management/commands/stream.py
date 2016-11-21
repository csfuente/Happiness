from optparse import make_option
from django.core.management.base import BaseCommand, CommandError
from happy.models import Tweet, City
import tweepy
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from tweepy import Stream
import json
import ast

city = ''

class Command(BaseCommand):
    help = "Streaming de tweets por ciudad"


    def add_arguments(self, parser):
        parser.add_argument('city')

    def handle(self, *args, **options):

        city = City.objects.get(id=int(options['city']))
    
        class listener(StreamListener):
            def on_data(self, data):
                try:
                    tweet = json.loads(data)
                    Tweet(city=city.name,text=tweet['text']).save()
                    print tweet['text']
                except Exception as e:
                    print e
                finally:
                    return True
            def on_error(self, status):
                print status

        consumer_key = 'nfuviCx9LnZdSavy6wzece3mh'
        consumer_secret = 'pqBZoz2I9pvfOvYSl0nHZSvpKSCio8cTU5Cr48J4nSYIhZXkfj'
        access_token = '75291095-lcobPsNLU65GHyVyZZFOZfiMjOrwFmdCIk3CvINXy'
        access_secret = 'qZbD1qiUJMLfltjYk6PinfAWG6SpQ2DKs2SS09w5CSGZf'

        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_secret)

        api = tweepy.API(auth)

        twitterStream = Stream(auth, listener())
        twitterStream.filter(locations=ast.literal_eval(city.position))    #Cambiar para por ciudad
