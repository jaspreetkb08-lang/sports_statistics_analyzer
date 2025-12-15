import pandas as pd
import matplotlib.pyplot as plt


performance = lambda g, a, f: (g * 4) + (a * 3) - f

def save_players(players):
    data = [p.get_summary() for p in players]
    df = pd.DataFrame(data)
    df.to_csv("players.csv", index=False)

def show_player_comparison(df):
    plt.figure()
    plt.bar(df["Name"], df["Performance Index"])
    plt.title("Player Performance Comparison")
    plt.xlabel("Player")
    plt.ylabel("Performance Index")
    plt.show()

def save_matches(matches):
    import pandas as pd
    df = pd.DataFrame(matches)
    df.to_csv("matches.csv", index=False)

