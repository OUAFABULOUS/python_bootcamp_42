from FileLoader import FileLoader
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class	MyPlotLib:
    def	histogram(data, features):
        # print(data[features])
        for feature in features:
            plt.figure()
            plt.hist(data[feature], color='blue', edgecolor='black', bins=int(45/1))
            # plt.hist(data[features])
            plt.show()

    def density(data, features):
        plt.figure()
        for feature in features:
            # plt(data[feature], kind='density')
            (data[feature]).plot(kind='density')
        plt.show()

    def pair_plot(data, features):
        plt.figure()
        new_df = pd.DataFrame()
        for feature in features:
            new_df[feature] = data[feature]
        pd.plotting.scatter_matrix(new_df, alpha=0.2,grid=True)
        # scatter_matrix(data[feature])
        plt.show()

    def box_plot(data, features):
        plt.figure()
        data.boxplot(column=features)
        plt.show()






if __name__=="__main__":
    fl = FileLoader()
    df = fl.load("athlete_events.csv")
    # MyPlotLib.histogram(df, "Sex")
    # MyPlotLib.density(df, ["Height", "Weight"])
    # MyPlotLib.pair_plot(df, ["Height", "Weight"])
    MyPlotLib.box_plot(df, ["Weight", "Height"])

