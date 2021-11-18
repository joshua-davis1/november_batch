import pandas as pd

df = pd.read_csv("2_pandas_Salaries.csv")

def one():
    print(df.head())

def two():
    print(df.info())

def three():
    print(df['BasePay'].head(10000).mean())

def four():
    print(df['TotalPayBenefits'].max())

def five():
    print(df[df['EmployeeName'].str.contains('JOSEPH DRISCOLL')]['JobTitle'])

def six():
    print(df[df['EmployeeName'].str.contains('JOSEPH DRISCOLL')]['TotalPay'])

def seven():
    print(df['EmployeeName'][df['TotalPayBenefits'].idxmax()])

def eight():
    # Joe is paid - negative. Did joe receive a loan from employer?
    print(df['EmployeeName'][df['TotalPayBenefits'].idxmin()])

def nine():
    print(df.groupby(['Year'])['TotalPay'].mean())

def ten():
    print(df['JobTitle'].nunique())

def eleven():
    print(df['JobTitle'].value_counts().head(7))

def twelve():
    print(df['JobTitle'].value_counts().loc[lambda x : x == 1])

def thirteen():
    print(df['JobTitle'].str.contains('Chief').sum())

def forteen():
    print("?")

thirteen()
