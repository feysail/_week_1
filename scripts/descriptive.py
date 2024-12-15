import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
def length(dataframe,column):
    return len(dataframe[column])

def groupby(data_frame,group_column,count_column):
    return data_frame.groupby(group_column)[[count_column]].count().sort_values(ascending=False)


def change(data_frame,date):
    return data_frame[date]==pd.to_datetime(data_frame[date],format='mixed', utc=True)


    

