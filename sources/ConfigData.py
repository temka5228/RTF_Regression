import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder, LabelBinarizer

class ConfigData:
    def __init__(self, fname:str, delimeter=','):
        try:
            self.__csvfile = pd.read_csv(fname, sep=delimeter)
        except FileNotFoundError as e:
            raise FileNotFoundError("FILE NOT EXISTS IN CURRENT DIRECTORY; TRY \"./datasets/\"")
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
            self.__df[colName] = self.__df[colName].fillna(value)
        except Exception as e: 
            print(f"Exception on column \"{colName}\"")

    def labelEncodingPriority(self, col:str, d:dict):
        self.__df.replace({col: d}, inplace=True)

    def labelEncoding(self, col:str):
        self.__df[col] = LabelEncoder().fit_transform(self.__df[col])

    def labelBinazer(self, col:str):
        lb = LabelBinarizer()
        self.__df = self.__df.join(pd.DataFrame(lb.fit_transform(self.__df[col]),
                          columns=lb.classes_, 
                          index=self.__df.index))
        self.__df.drop(labels=col, axis=1, inplace=True)

    def printDf(self):
        print(self.__df)
    
    def printColumns(self):
        print(self.__df.columns)

    def printCountNan(self) -> pd.Series:
        nullColumns = self.__df.isnull().sum()
        print(nullColumns.sum())
        return nullColumns

    def plotHist(self):
        hist = self.__df.hist(bins = 10)