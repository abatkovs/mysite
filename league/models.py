from django.db import models

# Create your models here.

class Summoners(models.Model):
    name = models.CharField(max_length=200, unique = True)
    summoner_id = models.IntegerField(default = 0, unique = True)
    accountId = models.IntegerField(default = 0)
    summonerLevel = models.IntegerField(default = 0)
    profileIconId = models.IntegerField(default = 0)
    revisionDate = models.IntegerField(default = 0)
    modify_date = models.DateTimeField('date published')
    def __str__(self):
        return 'SummonerName: {}'.format(self.name)
    
    
"""
revisionDate: 1518529366000
profileIconId: 1625
summonerLevel: 82
accountId: 31650179
id: 27260328
name: FizzCantCarry Q8


"""    