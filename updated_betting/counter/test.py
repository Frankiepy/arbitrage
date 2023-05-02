# Arbitrage betting calculator for soccer games

# Define the odds for each potential outcome of the game
home_odds = 2.88
away_odds = 2.8
draw_odds = 3.4

# Calculate the inverse of each odds to get the implied probabilities
home_prob = 1/home_odds
away_prob = 1/away_odds
draw_prob = 1/draw_odds

# Calculate the total implied probability of all outcomes
total_prob = home_prob + away_prob + draw_prob

# Calculate the percentage of the total implied probability for each outcome
home_percent = home_prob / total_prob
away_percent = away_prob / total_prob
draw_percent = draw_prob / total_prob

# Calculate the amount to bet on each outcome to ensure a profit
total_bet = 100 # total amount available to bet
home_bet = total_bet * (1/home_odds) / total_prob
away_bet = total_bet * (1/away_odds) / total_prob
draw_bet = total_bet * (1/draw_odds) / total_prob

# Print the results
print("Home team bet:", round(home_bet, 2))
print("Away team bet:", round(away_bet, 2))
print("Draw bet:", round(draw_bet, 2))
print("Total bet:", round(home_bet + away_bet + draw_bet, 2))



test = [['','',.8,''],['','',.2,''],['','',.6,'']]
test = sorted(test)
print(test)