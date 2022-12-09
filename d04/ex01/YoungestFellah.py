from FileLoader import FileLoader as fl
import pandas as pd

def	youngest_fellah(df, year):
    df_m = df.loc[(df["Year"]== year) & (df["Sex"] == "M")]
    df_f = df.loc[(df["Year"]== year) & (df["Sex"] == "F")]
    return {'f':min(df_f["Age"]),'m':min(df_m["Age"])}


if __name__=="__main__":
    fl()
    print(youngest_fellah(fl.load(fl,"athlete_events.csv"), 2004))

