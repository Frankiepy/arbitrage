import requests

from moneybets import two_sites_basic

# IT GOES FIRST TEAM, SECOND TEAM, DRAW





# An api key is emailed to you when you sign up to a plan
# Get a free API key at https://api.the-odds-api.com/
API_KEY = '8d725450b28fb2467bdb7fafa3b0a4fe'

BOOKMAKER = 'superbook'

SPORT = 'soccer' # use the sport_key from the /sports endpoint below, or use 'upcoming' to see the next 8 games across all sports

REGIONS = 'eu,us,uk' # uk | us | eu | au. Multiple can be specified if comma delimited

MARKETS = 'h2h,spreads' # h2h | spreads | totals. Multiple can be specified if comma delimited

ODDS_FORMAT = 'decimal' # decimal | american

DATE_FORMAT = 'iso' # iso | unix

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#
# First get a list of in-season sports
#   The sport 'key' from the response can be used to get odds in the next request
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

#sports_response = requests.get(
#    'https://api.the-odds-api.com/v4/sports', 
#    params={
#        'api_key': API_KEY
#    }
#)


#if sports_response.status_code != 200:
#    print(f'Failed to get sports: status_code {sports_response.status_code}, response body {sports_response.text}')

#else:
#    print('List of in season sports:', sports_response.json())



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#
# Now get a list of live & upcoming games for the sport you want, along with odds for different bookmakers
# This will deduct from the usage quota
# The usage quota cost = [number of markets specified] x [number of regions specified]
# For examples of usage quota costs, see https://the-odds-api.com/liveapi/guides/v4/#usage-quota-costs
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

odds_response = requests.get(
    f'https://api.the-odds-api.com/v4/sports/{SPORT}/odds',
    params={
        'api_key': API_KEY,
        'regions': REGIONS,
        'markets': MARKETS,
        'bookmaker' : BOOKMAKER,
        'oddsFormat': ODDS_FORMAT,
        'dateFormat': DATE_FORMAT,
    }
)

if odds_response.status_code != 200:
    print(f'Failed to get odds: status_code {odds_response.status_code}, response body {odds_response.text}')

else:
    odds_json = odds_response.json()
    print('Number of events:', len(odds_json))
    print(odds_json)
    superbook = odds_json
    with open("/Users/frankie/Downloads/FeedSDK-Python-master/betting_automation/collect_info.txt", "w") as o:
        for game in superbook:
            for site1 in game['bookmakers']:
                s1 = []
                for p1 in site1['markets'][0]['outcomes']:
                    print(p1)
                    s1.append(p1['price'])

                temp_list = game['bookmakers']
                temp_list.remove(site1)
                for site2 in game['bookmakers']:
            
                    s2 = []
                    for p2 in site2['markets'][0]['outcomes']:
                        s2.append(p2['price'])
                    #print(s1,s2)
                    outcome, instructions = 2, ''
                    try:
                        outcome ,instructions = two_sites_basic(s1, s2)
                    except Exception:
                        pass
                    if outcome < 1:
                        o.write('\n')
                        o.write(f"{game['sport_title']}\n")
                        o.write(f"{game['home_team']} vs {game['away_team']}\n")
                        o.write(f'{outcome}\n')
                        o.write(f'{s1} {s2}\n')
                        o.write(f"{site1['title']}\n")
                        o.write(f"{site2['title']}\n")
                        o.write(f'{instructions[0]}\n')
                        o.write(f'{instructions[1]}\n')
                        o.write(f'{instructions[2]}\n')

    # Check the usage quota
    print('Remaining requests', odds_response.headers['x-requests-remaining'])
    print('Used requests', odds_response.headers['x-requests-used'])



#print(webscraper('https://nj.pointsbet.com/sports/soccer','p','class', ""))

#print(webscraper('https://nypost.com/2023/03/02/ny-country-club-a-bacchanal-of-money-squash-and-sexual-abuse-suit/','span', '', ''))

'https://nj.pointsbet.com/sports/soccer/Portuguese-Primeira-Liga'
'https://sportsbook.draftkings.com/leagues/soccer/portugal---primeira-liga'
'https://sportsbook.fanduel.com/soccer?tab=epl'


matches_site1 = {'Bayern v Dortumund' : ['+125', '+204', '+281']}
mathces_site2 = {}