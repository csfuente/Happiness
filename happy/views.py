# -*- coding: latin-1 -*-
from django.shortcuts import render_to_response
from models import Tweet, City, Measur

AMOR_QUERY = [u"te quiero mucho",u"te quiero más",u"amo tanto",u"amo tanto",u"todo mi amor",u"muy enamorado",u"tan enamorada"]
IRA_QUERY = [u"te odio",u"siento rabia",u"le odio",u"estoy furioso",u"estoy furiosa",u"crispado",u"estoy cabreado"]
ALEGRIA_QUERY= [u"mas feliz",u"bastante feliz",u"tan feliz",u"muy feliz",u'gozo',u'júbilo',u'deleite',u'alborozo',u'juerga']
SORPRESA_QUERY=[u"no me lo puedo creer",u"increible",u"asombro",u"me ha sorprendido",u"te ha sorprendido",u"cogido por sorpresa"]
ENVIDIA_QUERY= [u"ambiciono",u"codicio",u"mucha envidia",u"yo quiero ser",u"por que no puedo",u"envidio",u"celoso"]
TRISTEZA_QUERY=[u"muy triste",u"tan deprimido",u"estoy llorando",u"tengo el corazón roto",u"estoy triste",u"me quiero morir"]
MIEDO_QUERY=[u"muy asustado",u"tan asustada",u"realmente asustado",u"terrorifico",u"tanto temor",u"que horror",u"aterrozizado"]


def results(request):
    cities = City.objects.all()

    for meas in Measur.objects.all():
        meas.delete()

    for city in cities:
        tweets = Tweet.objects.filter(city=str(city.name))
        calculo = Measur(city=city)
        for tweet in tweets:
            for amor in AMOR_QUERY:
                if amor in tweet.text:
                    calculo.amor += 1
            for ira in IRA_QUERY:
                if ira in tweet.text:
                    calculo.ira += 1
            for alegria in ALEGRIA_QUERY:
                if alegria in tweet.text:
                    calculo.alegria += 1
            for sorpresa in SORPRESA_QUERY:
                if sorpresa in tweet.text:
                    calculo.sorpresa += 1
            for envidia in ENVIDIA_QUERY:
                if envidia in tweet.text:
                    calculo.envidia += 1
            for tristeza in TRISTEZA_QUERY:
                if tristeza in tweet.text:
                    calculo.tristeza += 1
            for miedo in MIEDO_QUERY:
                if miedo in tweet.text:
                    calculo.miedo += 1
        calculo.save()

    measures = Measur.objects.all()

    return render_to_response('index.html',{'measures':measures})
