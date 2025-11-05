import pandas as pd

def csv_reader(filename):
    df = pd.read_csv(filename)
    return df

def columns_no(df):
    return df.shape[1]

def rows_no(df):
    return df.shape[0]

def fill_missing(df):
    return df.fillna(0)







