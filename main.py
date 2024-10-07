import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

class ConfigData:
    def __init__(self, fname:str, delimeter=','):
        self.__csvfile = pd.read_csv(fname, sep=delimeter)
        self.__main()

    def __main(self):
        self.__df = self.__toDataFrame()
        self.__df = self.__setIndex(self.__df)

        #self.printDf()


    def __toDataFrame(self):
        return pd.DataFrame(self.__csvfile)

    def __setIndex(self, df:pd.DataFrame, labelIndex=None):
        try: 
            if labelIndex != None:
                return df.set_index(labelIndex)
            else: 
                raise Exception("Something went wrong\n Created new indecies with name \"ID\"")
        except Exception as e: 
            return df.set_index(pd.Series(np.arange(df.shape[0]), name="ID"))
        
    def fillNan(self, colName:str, value=0):
        try: 
            self.__df[colName].fillna(value, inplace=True)
        except Exception as e: 
            print(f"Exception on column \"{colName}\"")

    def printDf(self):
        print(self.__df)
    
    def printColumns(self):
        print(self.__df.columns)

    def printCountNan(self) -> pd.Series:
        nullColumns = self.__df.isnull().sum()
        print(nullColumns.sum())
        return nullColumns

    def plotHist(self):
        self.__df.hist()



if __name__ == "__main__":
    childrenAmnesia = ConfigData("./children anemia.csv")
    childrenAmnesia.printColumns()
    nullColumns = childrenAmnesia.printCountNan()
    for ax, col in nullColumns.to_dict().items():
        if col > 0:
            childrenAmnesia.fillNan(ax, 0)
    childrenAmnesia.printDf()