import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# creating dataframe
df = pd.read_csv('content/Zomato-data.csv')


## data cleaning
# converting rate column to float by removing denominator
def handle_rate(value):
    value = str(value).split('/')
    value = value[0]
    return float(value)

df['rate'] = df['rate'].apply(handle_rate)


#checking restaurant types
sns.countplot(x=df['listed_in(type)'])

grouped_data = df.groupby('listed_in(type)')['votes'].sum()
result = pd.DataFrame({'votes': grouped_data})
plt.plot(result, c='red', marker='o')
plt.xlabel('Type of Restaurant')
plt.ylabel('Number of Votes')

max_votes = df['votes'].max()
max_votes_restaurant = df.loc[df['votes'] == max_votes, 'name']
print("The restaurant with the highest votes is: ", max_votes_restaurant)

#online order availability
sns.countplot(x=df['online_order'])
plt.xlabel('Online Order Availability')

# analyzing ratings
plt.hist(df['rate'], bins=5)
plt.title('Distribution of Restaurant Ratings')

#approx cost for couple

sns.countplot(x=df['approx_cost(for two people)'])

# online order vs offline order
sns.boxplot(x='online_order', y='rate', data=df)

# order mode preference by restaurant type
pivot_table = df.pivot_table(index='listed_in(type)', columns='online_order', aggfunc='size', fill_value=0)
sns.heatmap(pivot_table, annot=True, fmt='d', cmap='YlGnBu')
plt.xlabel('Online Order')
plt.ylabel('Type of Restaurant')
plt.title('Order Mode Preference by Restaurant Type')
plt.show()