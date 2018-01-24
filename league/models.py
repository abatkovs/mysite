from django.db import models

# Create your models here.

class Summoners(models.Model):
    summoner_name = models.CharField(max_length=200, unique = True)
    summoner_id = models.IntegerField(default = 0)
    losses = models.IntegerField(default = 0)
    wins = models.IntegerField(default = 0)
    leagueName = models.CharField(max_length = 100)
    rank = models.CharField(max_length = 50)
    modify_date = models.DateTimeField('date published')
    def __str__(self):
        return self.summoner_name
    
    
"""
s.name = 'Dragoon112'
data = s.rank()
lol_s = Summoners(summoner_name = data[0]['playerOrTeamName'], summoner_id = data[0]['playerOrTeamId'], losses = data[0]['losses'], wins = data[0]['wins'], leagueName = data[0]['leagueName'], rank = data[0]['tier'] + " " + data[0]['rank'] + " - " + str(data[0]['leaguePoints']), pub_date = timezone.now())
lol_s.save()


"""    