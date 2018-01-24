'''
Created on 24 Jan 2018

@author: Arnolds
API Key: na

'''
import cassiopeia as cass
from cassiopeia import Summoner
from builtins import str
from cassiopeia import League

cass.apply_settings('settings.json')

def MySummoner(summoner_name: str, region: str):
    summoner = Summoner(name=summoner_name, region=region)
    print("Name:", summoner.name)
    print("ID:", summoner.id)

def print_summoner(name: str, region: str):
    summoner = Summoner(name=name, region=region)
    print("Name:", summoner.name)
    print("ID:", summoner.id)
    print("Account ID:", summoner.account.id)
    print("Level:", summoner.level)
    print("Revision date:", summoner.revision_date)
    print("Profile icon ID:", summoner.profile_icon.id)
    print("Profile icon name:", summoner.profile_icon.name)
    print("Profile icon URL:", summoner.profile_icon.url)
    print("Profile icon image:", summoner.profile_icon.image)

def print_leagues(summoner_name: str, region: str):
    summoner = Summoner(name=summoner_name, region=region)
    print("Name:", summoner.name)
    print("ID:", summoner.id)

    # positions = cass.get_league_positions(summoner, region=region)
    positions = summoner.league_positions
    if positions.fives.promos is not None:
        # If the summoner is in their promos, print some info
        print("Promos progress:", positions.fives.promos.progress)
        print("Promos wins", positions.fives.promos.wins)
        print("Promos losses:", positions.fives.promos.losses)
        print("Games not yet played in promos:", positions.fives.promos.not_played)
        print("Number of wins required to win promos:", positions.fives.promos.wins_required)
    else:
        print("The summoner is not in their promos.")

    print("Name of leagues this summoner is in:")
    for league in positions:
        print(league.name)
    print()

    # leagues = cass.get_leagues(summoner)
    leagues = summoner.leagues
    print("Name of leagues this summoner is in (called from a different endpoint):")
    for league in leagues:
        print(league.name)
    print()

def print_rank(summoner_name: str, region: str):
    summoner = Summoner(name=summoner_name, region=region)
    print("Summ id is ", summoner.id)
    leagues = summoner.leagues
    

    
    
if __name__ == "__main__":
    #print_summoner("Dragoon112", "EUNE")
    #print_leagues("Dragoon112", "EUNE")
    print_rank('Dragoon112', 'EUNE')