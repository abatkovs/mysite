#Importing django environment and then running the tests
import sys; print('%s %s' % (sys.executable or sys.platform, sys.version))
import os; os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'; import django


from django.core.wsgi import get_wsgi_application
from pip._vendor.distlib.compat import raw_input
application = get_wsgi_application()

#demo testi apaksha
from django.utils import timezone


from league.models import Summoners
from lol.lol_rw import lol_summoner
s = lol_summoner(path = '../lol/')

def test():
    #TLP Levi
    f = input('Name: ')

    print(f)
    summoner = s.summoner(f)
    for k, v in summoner.items():
        print('{}: {}'.format(k,v))
    #if summoner id == Summoners.objects.filter(summoner_id = summoner id) tad nepievinoe summoner velreiz
    
   
    while True:
        try:
            print('Trying summoner: {} - {}'.format(summoner['name'], summoner['id']))
            Summoners.objects.get(summoner_id = summoner['id'])
            break
        except:
            print('adding summoner: '.format(summoner['name']))
            data = Summoners(name = summoner['name'], modify_date = timezone.now(), accountId = summoner['accountId'], profileIconId = summoner['profileIconId'], revisionDate = summoner['revisionDate'], summonerLevel = summoner['summonerLevel'], summoner_id = summoner['id'])
            data.save()
    
    #if summoner['id'] == Summoners.objects.filter(summoner_id = summoner['id']):
    #    print('New Summoner: {} Already exists in database {}'.format(summoner['id'], Summoners.objects.filter(summoner_id = summoner['id'])))

    print('Got ID = {}'.format(summoner['id']))
    summoner_id = Summoners.objects.get(summoner_id = summoner['id']).summoner_id
    print('DB ID = {}'.format(summoner_id))
    print(type(summoner_id))
    print(Summoners.objects.all())
    #return Summoners.objects.all()


while True:
    test()




