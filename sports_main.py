from player_class import Player
from match_class import Match
import stats_utils as su
import pandas as pd

p1 = Player("Rohit", "India", "Batsman")
p2 = Player("Virat", "India", "Batsman")

p1.update_stats(2, 1, 0, 90)
p2.update_stats(1, 2, 1, 90)

players = [p1, p2]
su.save_players(players)

match = Match(1, "India", "Australia", 250, 240)
print(match.get_summary())

df = pd.read_csv("players.csv")
print(df)

su.show_player_comparison(df)

match = Match(1, "India", "Australia", 250, 240)

matches = [{
    "Match ID": 1,
    "Team 1": "India",
    "Team 2": "Australia",
    "Score 1": 250,
    "Score 2": 240
}]

su.save_matches(matches)

summary = df[["Name", "Team", "Performance Index"]]
summary.to_csv("player_summary.csv", index=False)
su.show_player_comparison(df)
