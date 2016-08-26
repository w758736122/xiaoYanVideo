from django.db import models
from mongoengine import *
from mongoengine import connect
connect('spider',host='127.0.0.1',port=27017)

class ArtiInfo(Document):
    data_years = StringField()
    data_title = StringField()
    data_region = StringField()
    data_actors = StringField()
    data_rate = StringField()
    data_director = StringField()
    data_video_long = StringField()
    titles = StringField()
    img = StringField()
    links=StringField()
    ticket = StringField()
    meta={
        'collection':'video_spider'
    }

#for i  in ArtiInfo.objects[:1]:
  #  print(i.titles)
