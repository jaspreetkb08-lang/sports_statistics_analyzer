from datetime import datetime

def timestamp(func):
    def wrapper(*args, **kwargs):
        print("Match logged at:", datetime.now())
        return func(*args, **kwargs)
    return wrapper

class Match:
    def __init__(self, match_id, team1, team2, score1, score2):
        self.match_id = match_id
        self.team1 = team1
        self.team2 = team2
        self.score1 = score1
        self.score2 = score2

    @timestamp
    def get_summary(self):
        return {
            "Match ID": self.match_id,
            "Team 1": self.team1,
            "Team 2": self.team2,
            "Score": f"{self.score1}-{self.score2}"
        }
