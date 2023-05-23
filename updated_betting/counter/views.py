from django.shortcuts import render
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
import requests
from datetime import datetime
import pytz

def win_p_1(t_ML):
    win = 0
    if t_ML[0] == '-':
        win = 100/float(t_ML[1:])
    else:
        win = float(t_ML[1:])/100
    return win
    
 
def bet(amount, t1_ML, tie_ML, t2_ML):
    won_amount1 = amount*win_p_1(t1_ML)
    won_amount2 = amount*win_p_1(tie_ML)
    won_amount3 = amount*win_p_1(t2_ML)
    total1 = won_amount1 + amount
    total2 = won_amount2  + amount
    total3 = won_amount3 + amount
    #print(1/total1 + 1/total2 + 1/total3)
    return {total1:[t1_ML, 1/total1], total2:[tie_ML, 1/total2], total3:[t2_ML, 1/total3]}#, [total1, total2, total3]

def two_sites(pot1, pot2):
    keys1 = list(pot1)
    keys2 = list(pot2)
    t1,tie,t2 = 0,0,0
    
    if keys1[0] > keys2[0]:
        t1 = pot1[keys1[0]]
        mult1 = keys1[0]
    else:
        t1 = pot2[keys2[0]]
        mult1 = keys2[0]
    
    if keys1[1] > keys2[1]:
        tie = pot1[keys1[1]]
        multtie = keys1[1]
    else:
        tie = pot2[keys2[1]]
        multtie = keys2[1]
    
    if keys1[2] > keys2[2]:
        t2 = pot1[keys1[2]]
        mult2 = keys1[2]
    else:
        t2 = pot2[keys2[2]]
        mult2 = keys2[2]

    #print(t1,tie,t2)
    print(mult1,multtie,mult2)
    #print(print(t1[1] + tie[1] + t2[1]))
    #if t1[1] + tie[1] + t2[1] < 1:
        #add_to_probability = (1-(t1[1] + tie[1] + t2[1]))/3
        #t1[1] += add_to_probability
        #tie[1] += add_to_probability
        #t2[1] += add_to_probability
        #print(t1,tie,t2) # put this percent of money into this one
        #print(t1[1] * mult1, tie[1] * multtie, t2[1] * mult2)# winnings
        
    #else:
    #    print(0)

    
def two_sites_basic(s1, s2):
    #order is different team1, team2, tie
    t1,t2,tie = 0,0,0
    
    if s1[0] > s2[0]:
        t1 = s1[0]
    else:
        t1 = s2[0]
    
    if s1[2] > s2[2]:
        tie = s1[2]
    else:
        tie = s2[2]
    
    if s1[1] > s2[1]:
        t2 = s1[1]
    else:
        t2 = s2[1]

    team1 = ''
    tied_game = ''
    team2 = ''

    #print(t1,tie,t2)
    if 1/t1 + 1/tie + 1/t2 < 1:
        add_to_probability = (1-(1/t1 + 1/tie + 1/t2))/3
        #return 1/t1 + 1/tie + 1/t2
        perct1 = 1/t1 + add_to_probability
        perct2 = 1/tie + add_to_probability
        perct3 = 1/t2 + add_to_probability
        team1 = 'TEAM 1: buy this percent: ' + str(perct1)
        tied_game = 'TIE: buy this percent: ' + str(perct2)
        team2 = 'TEAM 2: buy this percent: ' + str(perct3)
        #print(t1,tie,t2) # put this percent of money into this one
        #print(perct1 * t1, perct2* tie, perct3 * t2)# winnings
        
    #else:
    #    return(1)
    return [1/t1 + 1/tie + 1/t2, [team1,tied_game,team2], [perct1*t1,perct2*tie,perct3*t2]]


l1 = bet(1, '+125','+204','+281')
l2 = bet(1, '+125','+270','+195')

two_sites_basic(list(l1),list(l2))

two_sites(l1,l2)

#bet(1, '+170', '+143', '+260')

"https://the-odds-api.com/sports-odds-data/bookmaker-apis.html#us-bookmakers"

def get_info(key):
    scope = ['https://ww.googleapis.com/auth/spreadsheeets', 'https://www.googleapis.com/auth/drive.file', 'https://www.googleapis.com/auth/drive']

    #gc = gspread.service_account(filename='/Users/frankie/Downloads/gspread-5.9.0/sheetsconnection-386902-8d39a29cfb3c.json')
    #spreadsheets2-387422-722bacd99d06.json
    gc = gspread.service_account(filename='/Users/frankie/opt/anaconda3/envs/myenv/updated_betting2/counter/sheetsconnection-386902-8d39a29cfb3c.json')
    sh = gc.open_by_key('1fblZM76XYfcG82Qel4xKiFnrVwyE_2D7UkV5XbdETFE')
    worksheet = sh.sheet1
    worksheet.batch_clear(['A2:K350'])

    #04c597bac5375d93135a36cdf66c9e4e - full, brand new
    #a00d8a728f54650ef7793a6f5974ed0c - full, brand new
    #8ed6d5217b0e9d7f46b9c22e456e3966 - full, brand new
    #3c71816014ad3e323eca95b3fe2e1263 - new
    #8d725450b28fb2467bdb7fafa3b0a4fe - old
    API_KEY = key#'8d725450b28fb2467bdb7fafa3b0a4fe'

    BOOKMAKER = 'superbook'

    SPORT = 'soccer' # use the sport_key from the /sports endpoint below, or use 'upcoming' to see the next 8 games across all sports

    REGIONS = 'eu,us,uk' # uk | us | eu | au. Multiple can be specified if comma delimited

    MARKETS = 'h2h,spreads' # h2h | spreads | totals. Multiple can be specified if comma delimited

    ODDS_FORMAT = 'decimal' # decimal | american

    DATE_FORMAT = 'iso' # iso | unix

    info = []
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
                        outcome, instructions, results = two_sites_basic(s1, s2)
                    except Exception:
                        pass
                    if outcome < 0.99:
                        temp = []
                        temp.append('\n')
                        temp.append(f"League: {game['sport_title']}")
                        temp.append(f"Game: {game['home_team']} vs {game['away_team']}")
                        number = 100-(float(outcome)*100)
                        temp.append(f'return percentage: {number/100}% (>0.1 is pretty good)')

                        team1 = site1['title']
                        tie = site1['title']
                        team2 = site1['title']

                        if s1[0] < s2[0]:
                            team1 = site2['title']
                        if s1[1] < s2[1]:
                            tie = site2['title']
                        if s1[2] < s2[2]:
                            team2 = site2['title']
                        print(s1[0])
                            
                        temp.append(f'{s1} {s2}')
                        temp.append(f"{site1['title']}")
                        temp.append(f"{site2['title']}")
                        temp.append(f'{team1}: {instructions[0]}')
                        temp.append(f'{tie}: {instructions[1]}')
                        temp.append(f'{team2}: {instructions[2]}')
                        info.append(temp)

                        league = game['sport_title']
                        game1 = f"{game['home_team']} vs {game['away_team']}"
                        return_percent = 1-outcome
                        #o.write(f'{s1} {s2}')
                        site11 = site1['title']
                        site22 = site2['title']
                        team1_win = instructions[0]
                        tie = instructions[1]
                        team2_win = instructions[2]
                        t1_result = results[0]
                        tie_result = results[1]
                        t2_result = results[2]
                        info1 = [game1, league, return_percent, site11, site22, team1_win, tie, team2_win, t1_result, tie_result, t2_result]

                        tz_NY = pytz.timezone('America/New_York') 

                        # Get the current time in New York
                        datetime_NY = datetime.now(tz_NY)
                        current_time = datetime_NY.strftime("%H:%M:%S")
                        try:
                            worksheet.append_row(info1)
                            worksheet.update_acell('L2',current_time)
                        except Exception:
                            gc = gspread.service_account(filename='/Users/frankie/opt/anaconda3/envs/myenv/updated_betting2/counter/spreadsheets2-387422-722bacd99d06.json')
                            sh = gc.open_by_key('1fblZM76XYfcG82Qel4xKiFnrVwyE_2D7UkV5XbdETFE')
                            worksheet = sh.sheet1
                            try:
                                worksheet.append_row(info1)
                            except Exception:
                                pass

        # Check the usage quota
        start = []
        start.append(f"Remaining requests for current API key: {int(odds_response.headers['x-requests-remaining'])}")
        start.append(f"Used requests for current API key: {int(odds_response.headers['x-requests-used'])}")
        print('good')
        #info.append(start)
    return [start] + info


count = 0
count = ['']
testing = 0

def index(request):
    global count
    global info
    global testing
    if request.method == 'POST':
        info = 'okay'
        if True:
            #request.POST.get('key')
            #count += 3
            count = get_info(request.POST.get('key'))
            print(count)
            #count = sorted(count)# fix the sorting shitttttttttttt
            #info = get_info()
            #print(info)
    return render(request, '/Users/frankie/opt/anaconda3/envs/myenv/updated_betting2/counter/templates/index.html', {'count': count})#, {'testing' : testing})
