#a. import the necessary libraries and read csv file
#im trying to make an accurate count of how many walmarts are in each city specfied in texas
#trying to make some sort of bar chart or pie to represent the years in which walmarts were opened in houston.
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.metrics import confusion_matrix
from pandas import Series, DataFrame
import seaborn as sns
import matplotlib.pyplot as plt

# To import the data from csv to pandas package
df = pd.read_csv('TexasWalmartOpenings.csv')
# To display the list of variables in the dataframe from the imported data
print(list(df.columns))

# To display the first five rows of the data
print("\nThe first five rows of the data ")
print(df.head())

#display how many cities have a walmart
df.sort_values(by = ['open_dateyear', 'City'])
print("\nTotal Walmarts for Houston: ", df.loc[df['City'] == 'Houston', 'City'].count() )
print("\nTotal Walmarts for Dallas: ", df.loc[df['City'] == 'Dallas', 'City'].count() )
#lewisville and waco are accurate, dallas and houston are not I dont know why
print("\nTotal Walmarts for Lewisville: ", df.loc[df['City'] == 'Lewisville', 'City'].count() )
print("\nTotal Walmarts for Waco: ", df.loc[df['City'] == 'Waco', 'City'].count() )


df['open_dateyear'].hist(color = 'skyblue')
plt.title("Distributions for Walmart Opening Dates")
plt.show()

houston = df[df.City == 'Houston']
dallas = df[df.City == 'Dallas']
#print(houston)
df2 = pd.DataFrame(houston)
print('-------Houston----')
print(df2)
df3 = pd.DataFrame(dallas)
print('-------Dallas----')
print(df3)
print("Houston Superstore Opening Dates")
print(df2[['storenum','date_super2']])

houston_date = df2['date_super2']
houston_name = df2['City']

plt.pie(houston_date, labels=houston_date, autopct='%1.1f%%', shadow=True, startangle=140)

df2.plot(kind = 'pie', y = 'date_super2', labels= df2['date_super2'])
plt.title("Population")
plt.show

sns.barplot(x = 'date_super2', y = 'City', data = df2, orient = 'v')
plt.show

#in excel the highlighted ones are not showing I dont know why(never mind fixed it)
#i want to do a pie chart or bar chart with a specific city and the opening dates