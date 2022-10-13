import pandas as pd

if __name__ == "__main__":
    data = pd.read_json("players_reshape.json")

    teams = list(data['club'].drop_duplicates(keep="first"))
    for team in teams:
        print(f'"{team}", ')
