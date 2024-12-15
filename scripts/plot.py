import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot(dataframe,date,news):
    
    return plt.plot(dataframe.groupby(dataframe[date].dt.date)[news].count()),plt.ylabel('news')

def sentiment(dataframe,column):
   if column in dataframe.columns:
        sns.histplot(data=dataframe, x=column, kde=True)
        plt.title('Sentiment Distribution')
        plt.xlabel('Sentiment')
        plt.ylabel('Count')
        plt.show()
    
   else: 
     print(f"Column '{column}' does not exist in the DataFrame.")

