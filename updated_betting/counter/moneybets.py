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
        team1 = 'TEAM 1: buy this percent: ' + str(perct1) + ' win this: ' + str(perct1*t1)
        tied_game = 'TIE: buy this percent: ' + str(perct2) + ' win this: ' + str(perct2*tie)
        team2 = 'TEAM 2: buy this percent: ' + str(perct3) + ' win this: ' + str(perct3*t2)
        #print(t1,tie,t2) # put this percent of money into this one
        #print(perct1 * t1, perct2* tie, perct3 * t2)# winnings
        
    #else:
    #    return(1)
    return [1/t1 + 1/tie + 1/t2, [team1,tied_game,team2]]


l1 = bet(1, '+125','+204','+281')
l2 = bet(1, '+125','+270','+195')

two_sites_basic(list(l1),list(l2))

two_sites(l1,l2)

#bet(1, '+170', '+143', '+260')

"https://the-odds-api.com/sports-odds-data/bookmaker-apis.html#us-bookmakers"