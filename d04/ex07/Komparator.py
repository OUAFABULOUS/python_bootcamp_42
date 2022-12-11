from FileLoader import FileLoader
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random

class Komparator:
    def	__init__(self, df):
        self.df = df

    def	get_random_rgb(self):
        for i in range(3):
            r = random.randint(0, 1)
            g = random.randint(0, 1)
            b = random.randint(0, 1)
            rgb = (r, g, b)
        return rgb


    def	get_to_plot(self, categorical_var, numerical_var):
        to_plot = pd.DataFrame()
        for i, x in enumerate(set(self.df[categorical_var])):
            name = numerical_var + " in " + x
            additional= pd.DataFrame({name: list((self.df.loc[df[categorical_var]==x])[numerical_var])})
            to_plot = pd.concat([to_plot, additional], axis=1)
        return(to_plot)


    def	compare_box_plots(self, categorical_var, numerical_var):
        plt.figure()
        to_plot = self.get_to_plot(categorical_var, numerical_var)
        to_plot.boxplot(list(to_plot.columns.values))
        plt.show()

    def	density(self, categorical_var, numerical_var):
        plt.figure()
        to_plot = self.get_to_plot(categorical_var, numerical_var)
        to_plot.plot.density()
        plt.show()

    def	compare_histograms(self, categorical_var, numerical_var):
        plt.figure()
        to_plot = self.get_to_plot(categorical_var, numerical_var)
        for column_name in list(to_plot.columns.values):
            rgb = self.get_random_rgb()
            plt.hist(to_plot[column_name], bins=25, alpha=0.45, color=rgb)
        plt.legend(to_plot.columns.values)
        plt.show()



if	__name__=="__main__":
    fl = FileLoader()
    df = fl.load("athlete_events.csv")
    k = Komparator(df)
    # k.compare_box_plots("Sex", "Age")
    # k.density("Sex", "Height")
    k.compare_histograms("Sex", "Height")
    exit()
    field_type_dict = (df.dtypes).astype(str).to_dict()
    categorical_columns = [x for x in list(field_type_dict.keys()) if field_type_dict[x] is "object"]
    numerical_columns = [x for x in list(field_type_dict.keys()) if field_type_dict[x]is not "object"]
    # for numerical in numerical_columns:
        # for categorical in categorical_columns:
            # compare_box_plots(categorical, numerical) I commented this line because it will take an eternity
