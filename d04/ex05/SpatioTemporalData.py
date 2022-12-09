from FileLoader import FileLoader


class	SpatioTemporalData:
    def	__init__(self, data):
        self.data = data

    def	when(self, location):
        data_location = self.data.loc[self.data["City"]==location]
        return(list(set(data_location["Year"])))

    def	where(self, date):
        data_d = self.data.loc[self.data["Year"]==date]
        return(list(data_d["City"])[0])

if	__name__=="__main__":
    fl = FileLoader()
    df = fl.load("athlete_events.csv")
    std = SpatioTemporalData(df)
    # print(std.when("Athina"))
    print(std.where(2016))


