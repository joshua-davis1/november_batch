from os import listdir
from os.path import isfile, join
import logging
import numpy as np
import pandas as pd
import log
import helpers

read_files = []

log.logStart()
mypath = "."
fileList = [f for f in listdir(mypath) if isfile(join(mypath, f)) and f.endswith(".csv")]
fileList.sort(reverse=True)


for i in range(0,len(fileList)):
    if i < len(fileList) - 1:
        df1 = pd.read_csv(fileList[i])
        df2 = pd.read_csv(fileList[i+1])
        isValid = helpers.compareDf(df1,df2)
        if isValid:
            if fileList[i] in read_files:
                log.alreadyPrc(fileList[i])
                continue
            log.openFile(fileList[i])
            helpers.processDf(df1)
            helpers.displayOne(df1)
            helpers.displayTwo(df1)
            helpers.displayThree(df1)
            read_files.append(fileList[i])
            log.closeFile()
        else:
            data = {"file": [fileList[i],fileList[i+1]],"dataframe":[len(df1.index),len(df2.index)]}
            log.dfLenErr(data)
            continue
    else:  
        df1 = pd.read_csv(fileList[i])
    print(len(df1.index))
    #if (len(df.index) > 500):
    #    pass
