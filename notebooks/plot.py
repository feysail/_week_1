import pandas as pd
import matplotlib.pyplot as plt

def plot(dataframe,date,news):
    
    return plt.plot(dataframe.groupby(dataframe[date].dt.date)[news].count()),plt.ylabel('news')