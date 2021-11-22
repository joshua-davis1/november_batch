import numpy as np
import log
import phonenumbers
from validate_email import validate_email
import matplotlib.pyplot as plt

states = ['AL','MO','AK','MT','AZ','NE','AR','NV','CA','NH','CO','NJ','CT','NM','DE','NY','DC','NC','FL','ND','GA','OH','HI','OK','ID','OR','IL','PA','IN','RI','IA','SC','KS','SD','KY','TN','LA','TX','ME','UT','MD','VT','MA','VA','MI','WA','MN','WV','MS','WI','WY']

def compareDf(df1,df2):
    offset = np.absolute(len(df1.index) - len(df2.index))
    log.offset(offset)
    if offset > 500: return False
    return True

def processDf(df):
    df = renameHeaders(df)
    valPhoneNums(df)
    valStates(df)
    valEmails(df)

def renameHeaders(df):
    df.rename(columns={"Agent Writing Contract Start Date (Carrier appointment start date)": "Agent Writing Contract Start Date", "Agent Writing Contract Status (actually active and cancelled\'s should come in two different files)": "Agent Writing Contract Status"}, inplace=True)
    return df

def valStates(df):
    stateCols = ['Agency State','Agent State']
    for col in stateCols:
        i = 1
        for el in df[col].values:
            if el not in states: log.invalidSts(i,col)
            i+=1
    col = 'Agent License State (active)'
    i = 1
    for stList in df[col].values:
        if type(stList) != str: continue
        stList = stList.strip(",").split(',')
        for state in stList:
            if state.upper() not in states:
                log.invalidSts(i+1,col)
        i+=1

def valPhoneNums(df):
    phoneCols = ['Agency Phone Number','Agent Phone Number']
    for col in phoneCols:
        i = 1 
        for num in df[col].values:
            try:
                p_num = phonenumbers.parse(num, "US")
            except phonenumbers.phonenumberutil.NumberParseException:
                log.invalidPhNum(i,col)
            finally: i+=1


def valEmails(df):
    cols = ["Agent Email Address"]
    for col in cols:
        i=1
        for row in df[col].values:
            is_valid = validate_email(email_address=row,check_blacklist=False,check_dns=False,check_smtp=False)
            if not is_valid:
                log.invalidEmail(i,col)
            i+=1

def displayOne(df):
    print(df)

def displayTwo(df):
    df = df.groupby(['Agency State']).sum()
    df.plot()

def displayThree(df):
    cols = ['Agent Last Name','Agent First Name','Agent Writing Contract Start Date','Date when an agent became A2O']
    df = df[cols].copy()
    print(df)
