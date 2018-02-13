from riotwatcher import RiotWatcher
from requests import HTTPError



#me = watcher.summoner.by_name(my_region, 'Dragoon112')
#print(me)

# all objects are returned (by default) as a dict
# lets see if i got diamond yet (i probably didnt)
#my_ranked_stats = watcher.league.by_summoner(my_region, me['id'])
#print(my_ranked_stats)

#print("{p[name]} rank is {r[0][tier]} {r[0][rank]} from {r[0][leagueName]} league".format(p=me, r=my_ranked_stats))


class lol_summoner:
    
    
    my_region = 'eun1'

    name = ""
    def __init__(self, my_region = "eun1", path = ''):
        print('Reading API key.')

        f = open('{}api_key'.format(path), 'r')
        data = f.read()
        print('API Key: {}'.format(data))
        
        self.my_region = my_region
        self.watcher = RiotWatcher(data)
    
    def summoner(self, name):
        #1 call
        self.name = name
        summoner = self.watcher.summoner.by_name(self.my_region, self.name)
        return summoner
        
    def rank(self, name):
        # 2 calls
        try:
            summoner = self.summoner(name)
        except HTTPError as err:
            if err.response.status_code == 429:
                return '429'
            elif err.response.status_code == 404:
                return '404'
            else:
                raise
            
        #summoner = watcher.summoner.by_name(self.my_region, self.name)
        my_ranked_stats = self.watcher.league.by_summoner(self.my_region, summoner['id'])
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



#+++++++++++++++++Testing


















