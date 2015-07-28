from django.db import models

# Create your models here.

#class USER(models.Model):
#	name = models.CharField(max_length=20)
#	age = models.IntegerField()

class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Title(models.Model):
	name = models.CharField(max_length=20)
	notes = models.IntegerField(default=0)

