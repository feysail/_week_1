import pandas as pd
def load_data(path):
    return pd.read_csv(path)

def change(dataframe,column):
   return dataframe[column]==pd.to_datetime(dataframe[column])