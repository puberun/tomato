from mongoengine import *
from tomato.settings import DBNAME
from django.db import models


connect(DBNAME)


class User(Document):
    isloggedin = StringField(max_length=5,default='false', required=True)
    firstname = StringField(max_length=500, required=True)
    lastname = StringField(max_length=500, required=True)
    emailid = EmailField(max_length=70, required=True, unique = True)
    username = StringField(max_length=120, required=True)
    password = StringField(max_length=500, required=True)
    

class Review(Document):
    username = StringField(max_length=120, required=True)
    res_id = StringField(max_length=500, required=True)
    review_text = StringField(max_length=5000, required=True)
    rating = StringField(max_length=3)
    rating_text = StringField(max_length=20, required=True)
    rating_color = StringField(max_length=10, required=True)
