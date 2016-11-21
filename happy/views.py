# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from models import Tweet, City, Measur
import os, json

def _removeNonAscii(s): return "".join(i for i in s if ord(i)<128)

def results(request):
    cities = City.objects.all()

    for meas in Measur.objects.all():
        meas.delete()

    for city in cities:
        tweets = Tweet.objects.filter(city=str(city.name))
        calculo = Measur(city=city)
        text = u''
        for tweet in tweets:
            text += "{'text': '%s'}," % _removeNonAscii(tweet.text.replace('\n','').replace('"','').replace("'",''))
        pop = """curl -d "{'data': [%s]}" http://www.sentiment140.com/api/bulkClassifyJson""" % unicode(text)
        print pop
        response = os.popen(pop)
        response = json.load(response)

        for result in response['data']:
            if result['polarity']==0:
                calculo.negative += 1
            elif result['polarity']==2:
                calculo.neutral +=1
            elif result['polarity']==4:
                calculo.positive += 1
            
        calculo.save()

    measures = Measur.objects.all()

    return render_to_response('index.html',{'measures':measures})
