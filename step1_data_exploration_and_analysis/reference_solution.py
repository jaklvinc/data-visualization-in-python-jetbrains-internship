import pandas as pd

#import the data
df = pd.read_csv('../data/dataset.csv')

#print the info
df.info()

#save the 5th entry
fifth_entry = df.iloc[4]

#show and save unique genres and consoles
unique_genres = df['genre'].unique()
print(unique_genres)

unique_consoles = df['platform'].unique()
print(unique_consoles)

#create a new df with counts of games for each platform
new_df = df[['name','platform']].groupby('platform').count()
new_df = new_df.rename(columns={'name':'count'})
print(new_df)





