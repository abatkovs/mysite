from riotwatcher import RiotWatcher
from requests import HTTPError

watcher = RiotWatcher('RGAPI-6bf6d0a9-8cba-49d3-a4da-7b4e6396580e')

my_region = 'eun1'

#me = watcher.summoner.by_name(my_region, 'Dragoon112')
#print(me)

# all objects are returned (by default) as a dict
# lets see if i got diamond yet (i probably didnt)
#my_ranked_stats = watcher.league.by_summoner(my_region, me['id'])
#print(my_ranked_stats)

#print("{p[name]} rank is {r[0][tier]} {r[0][rank]} from {r[0][leagueName]} league".format(p=me, r=my_ranked_stats))

class lol_summoner:
    
    name = ""
    def __init__(self, my_region = "eun1"):
        self.my_region = my_region
    
    def summoner(self, name):
        #1 call
        self.name = name
        summoner = watcher.summoner.by_name(self.my_region, self.name)
        return summoner
        
    def rank(self, name):
        # 2 calls
        summoner = self.summoner(name)
        #summoner = watcher.summoner.by_name(self.my_region, self.name)
        my_ranked_stats = watcher.league.by_summoner(self.my_region, summoner['id'])
        return my_ranked_stats
#
# data = my_ranked_stats
#for list in data:
#    print(list)
#    for key, value in list.items():
#        print('{} - {}'.format(key, value))


    
# Lets see some champions
#static_champ_list = watcher.static_data.champions(my_region)
#print(static_champ_list)

# Error checking requires importing HTTPError from requests



# For Riot's API, the 404 status code indicates that the requested data wasn't found and
# should be expected to occur in normal operation, as in the case of a an
# invalid summoner name, match ID, etc.
#
# The 429 status code indicates that the user has sent too many requests
# in a given amount of time ("rate limiting").

"""
try:
    response = watcher.summoner.by_name(my_region, "some ranom names")
except HTTPError as err:
    if err.response.status_code == 429:
        print('We should retry in {} seconds.'.format(err.headers['Retry-After']))
        print('this retry-after is handled by default by the RiotWatcher library')
        print('future requests wait until the retry-after time passes')
    elif err.response.status_code == 404:
        print('Summoner with that ridiculous name not found.')
    else:
        raise
"""