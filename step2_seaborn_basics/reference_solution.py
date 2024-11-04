import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

#load the data
df = pd.read_csv('../data/dataset.csv')

#set the theme
sns.set_theme()

#create figure and axes
fig, ax = plt.subplots(1,2,figsize=(10,5))

#create histogram
sns.histplot(df,x='global_sales',ax=ax[0])
ax[0].set_title('Histogram')
ax[0].set_ylabel('Count')
ax[0].set_xlabel('Global Sales')

#create scatterplot
sns.scatterplot(df,x='na_sales',y='eu_sales',ax=ax[1])
ax[1].set_title('Scatter plot')
ax[1].set_ylabel('EU Sales')
ax[1].set_xlabel('NA Sales')

#set the layout so everything is shown
plt.tight_layout()

if __name__ == '__main__':
    plt.show()


