import pandas as pd
import numpy as np
import Extract
import Transform
import Load

def main():
    
    # extract
    filepath = "rawdata/DatasetProject_HRAnalytics.xlsx"
    df = Extract.readData(filepath)

    # transform
    transformer = Transform.dataTransformation(df)
    transformedDf = transformer.transform()

    # load
    outputFile = 'cleanedData/HRDfFinished.xlsx'
    loadResult = Load.loadData(transformedDf, outputFile)

    if loadResult:
        print('ETL process completed successfully')
    else:
        print('ETL process encountered an error')

if __name__ == '__main__':
    main()







