from FileLoader import FileLoader
import matplotlib.pyplot as plt
import pandas  as pd

def how_many_medals(df, name):
    df_name = df.loc[df["Name"]==name]
    res = {}
    for year in df_name["Year"]:
        G = 0
        S = 0
        B = 0
        new_df = df_name.loc[(df["Year"]==year)]
        for medal in new_df["Medal"]:
            # print(medal)
            if medal=="Gold":
                G += 1
            elif medal=="Silver":
                S += 1
            elif medal=="Bronze":
                B += 1
        # print(f"GSB in year {year}: {G} {S} {B}")
        res.update({year:{'G': G, 'S': S, 'B': B}})
    return(res)




    # return(len(df_year))

if __name__=="__main__":
    fl = FileLoader()
    df = FileLoader.load(fl, "athlete_events.csv")
    new_df = how_many_medals(df,"Kjetil Andr Aamodt")
    for key, value in new_df.items():
        print(key, ' : ', value)
