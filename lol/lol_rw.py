from riotwatcher import RiotWatcher
from requests import HTTPError

watcher = RiotWatcher('na')

my_region = 'eun1'

#me = watcher.summoner.by_name(my_region, 'Dragoon112')
#print(me)

# all objects are returned (by default) as a dict
# lets see if i got diamond yet (i probably didnt)
#my_ranked_stats = watcher.league.by_summoner(my_region, me['id'])
#print(my_ranked_stats)

#print("{p[name]} rank is {r[0][tier]} {r[0][rank]} from {r[0][leagueName]} league".format(p=me, r=my_ranked_stats))

class lol_summoner():
    name = ""
    my_region = "eun1"
    def rank(self):
        me = watcher.summoner.by_name(self.my_region, self.name)
        my_ranked_stats = watcher.league.by_summoner(self.my_region, me['id'])
        #print(my_ranked_stats)
        out = "{p[name]} rank is {r[0][tier]} {r[0][rank]} - {r[0][leaguePoints]} from {r[0][leagueName]} league".format(p=me, r=my_ranked_stats)
        #print("{p[name]} rank is {r[0][tier]} {r[0][rank]} - {r[0][leaguePoints]} from {r[0][leagueName]} league".format(p=me, r=my_ranked_stats))
        
        return my_ranked_stats

# Lets some champions
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