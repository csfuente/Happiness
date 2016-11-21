from django.db import models

class Tweet(models.Model):
    text = models.CharField(max_length=255)
    city = models.CharField(max_length=100)

    def save(self,*args,**kwargs):
        temp = Tweet.objects.filter(city=self.city)
        if len(temp)>10000:
            temp[0].delete()
        super(Tweet, self).save(*args,**kwargs)

class City(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=65)

class Measur(models.Model):
    city = models.ForeignKey(City,default=0)
    amor = models.PositiveIntegerField(default=0)
    ira = models.PositiveIntegerField(default=0)
    alegria = models.PositiveIntegerField(default=0)
    sorpresa = models.PositiveIntegerField(default=0)
    envidia = models.PositiveIntegerField(default=0)
    tristeza = models.PositiveIntegerField(default=0)
    miedo = models.PositiveIntegerField(default=0)
