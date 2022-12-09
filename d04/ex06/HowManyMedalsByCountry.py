from FileLoader import FileLoader
import pandas as pd

def	how_many_medals_by_country(df, country_name):
    res = {}
    # df = (df.loc[df["Team"]==country_name]).drop_duplicates()
    df = df.loc[df["Team"]==country_name]
    # print(df)
    for year in df["Year"]:
        # print(f"year: {year}")

        G = len(df.loc[(df["Year"]==year) & (df["Medal"]=="Gold")])
        S = len(df.loc[(df["Year"]==year) & (df["Medal"]=="Silver")])
        B = len(df.loc[(df["Year"]==year) & (df["Medal"]=="Bronze")])
        # print(f"GSB: {G} {S} {B}")
        res[year] = {'G': G, 'S': S, 'B': B}
    print(res)

if	__name__ == "__main__":
    fl = FileLoader()
    df = fl.load("athlete_events.csv")
    how_many_medals_by_country(df, "Finland")



