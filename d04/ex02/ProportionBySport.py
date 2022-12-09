import pandas as pd
from FileLoader import FileLoader

def	proportion_by_sport(df, year, sport, gender):
    df_gender = (df.loc[(df["Sex"]==gender) & (df["Year"]==year)]).drop_duplicates(["ID"])
    denominator = len(df_gender.index)
    if denominator == 0:
        return None
    numerator = len((df_gender.loc[(df_gender["Sport"]==sport)]).index)
    return numerator /denominator


if __name__=="__main__":
    fl = FileLoader()
    data = FileLoader.load(fl,"athlete_events.csv")
    print(proportion_by_sport(data, 2004, "Tennis", "F"))
