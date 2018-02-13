from lol.lol_rw import  lol_summoner
from league.models import Summoners


a = lol_summoner()
s = input('Summoner Name: ')
summoner = a.summoner(s)
print('Summoner Info: {}'.format(summoner))
for key,value in summoner.items():
    print('{}: {}'.format(key, value))
summoner = a.rank(s)
for i in summoner:
    if i['queueType'] == 'RANKED_SOLO_5x5':
        print('SoloQueue: {}'.format(i))
        for key, value in i.items():
            print('{}: {}'.format(key, value))
    elif i['queueType'] == 'RANKED_FLEX_SR':
        print('FlexQueue: {}'.format(i))
        for key, value in i.items():
            print('{}: {}'.format(key, value))
    
        
