from FileLoader import FileLoader
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class Komparator:
    def	__init__(self, df):
        self.df = df
    def	compare_box_plots(self, categorical_var, numerical_var):
        plt.figure()
        to_plot = pd.DataFrame()
        for i, x in enumerate(set(self.df[categorical_var])):
            name = numerical_var + " in " + x
            additional= pd.DataFrame({name: list((self.df.loc[df[categorical_var]==x])[numerical_var])})
            to_plot = pd.concat([to_plot, additional], axis=1)
        to_plot.boxplot(list(to_plot.columns.values))
        plt.show()

if	__name__=="__main__":
    fl = FileLoader()
    df = fl.load("athlete_events.csv")
    k = Komparator(df)
    k.compare_box_plots("Sex", "Age")
    exit()
    field_type_dict = (df.dtypes).astype(str).to_dict()
    categorical_columns = [x for x in list(field_type_dict.keys()) if field_type_dict[x] is "object"]
    numerical_columns = [x for x in list(field_type_dict.keys()) if field_type_dict[x]is not "object"]
    # for numerical in numerical_columns:
        # for categorical in categorical_columns:
            # compare_box_plots(categorical, numerical) I commented this line because it will take an eternity
