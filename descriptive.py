import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
def length(dataframe,column):
    return len(dataframe[column])

def groupby(data_frame,group_column,count_column):
    return data_frame.groupby(group_column)[[count_column]].count()

def plot(data_frame,date,news):
    return plt.plot(data_frame[date],data_frame[news].count())


    

