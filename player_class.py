class Player:
    def __init__(self, name, team, role):
        self.name = name
        self.team = team
        self.role = role
        self.goals = 0
        self.assists = 0
        self.fouls = 0
        self.minutes = 0

    def update_stats(self, goals, assists, fouls, minutes):
        self.goals += goals
        self.assists += assists
        self.fouls += fouls
        self.minutes += minutes

    def get_performance_index(self):
        return (self.goals * 4) + (self.assists * 3) - self.fouls

    def get_summary(self):
        return {
            "Name": self.name,
            "Team": self.team,
            "Role": self.role,
            "Goals": self.goals,
            "Assists": self.assists,
            "Fouls": self.fouls,
            "Minutes": self.minutes,
            "Performance Index": self.get_performance_index()
        }
