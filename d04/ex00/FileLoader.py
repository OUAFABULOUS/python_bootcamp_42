import pandas as pd

class	FileLoader:
    def	load(self, path):
        df = pd .read_csv(path)
        # print(type(df))
        # print(df.shape)
        return df

    def	display(self, df, n):
        print(df.head(n)) if n > 0 else print(df.tail(-1 * n))

    # def	display(self, df, n):

if __name__=="__main__":
    fl  = FileLoader()
    FileLoader.display(fl, FileLoader.load(fl, "athlete_events.csv"), -5)

