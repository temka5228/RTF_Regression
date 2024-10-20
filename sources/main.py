from ConfigData import ConfigData


if __name__ == "__main__":
    cd = ConfigData("./datasets/german_credit_data.csv")
    cd.printColumns()
    nullColumns = cd.printCountNan()
    for ax, col in nullColumns.to_dict().items():
        if col > 0:
            cd.fillNan(ax, 'empty')
    #cd.printDf()
    di = {'empty' : 0, 'little': 1, 'moderate': 2, 'rich': 3}
    cd.labelEncodingPriority('Checking account', di)
    di = {'empty' : 0, 'little': 1, 'moderate': 2,  'quite rich': 3,  'rich': 4}
    cd.labelEncodingPriority('Saving accounts', di)
    cd.labelEncoding('Sex')
    cd.labelBinazer('Housing')
    cd.labelBinazer('Purpose')
    cd.printDf()
