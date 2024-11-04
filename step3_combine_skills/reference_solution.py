import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

#set the theme of the plot
sns.set_theme()
fig, ax = plt.subplots()

#load in the dataset
df = pd.read_csv('../data/dataset.csv')

# only select platforms that we want
df = df[df['platform'].isin(['PS4','XOne','PC','WiiU'])]

#group by both platforms and genres
df = df.groupby(['platform','genre']).count()
df = df.reset_index() #reset index so we can sort on genres

#print barplot properly
sns.barplot(df,x='platform',y='name',hue='genre',order=['PS4','XOne','PC','WiiU'],hue_order=sorted(df['genre'].unique()))

#setup proper label
ax.set_ylabel('count')

if __name__ == '__main__':
    plt.show()

