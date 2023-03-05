import pandas as pd
import matplotlib.pyplot as plt



# Crude Oil Production by Country dataset
# Crude Oil Production data for different countries from 1992 to 2018.

df = pd.read_csv('Crude Oil Production by Country.csv')
df.head()

# These are the dataframe's columns
df.columns


# Drop columns and let's use data from 2008 to 2018

# Let's Drop columns 'Flag' and all years before 2008
df = df.drop(columns=['Flag', '1992', '1993', '1994', '1995', '1996', \
                      '1997', '1998', '1999', '2000', '2001', '2002',\
                          '2003', '2004', '2005', '2006', '2007'])
df.head()

# Let's filter out rows with values less than 500 in the '2018' column
df_clean = df[df['2018'] >= 500]


# Let's Sort the dataframe by the '2018' column in descending order
df_clean = df_clean.sort_values('2018', ascending=False)

# and the fix columns datatypes
df_clean['2008'] = pd.to_numeric(df_clean['2008'], errors='coerce')
df_clean['2009'] = pd.to_numeric(df_clean['2009'], errors='coerce')
df_clean['2010'] = pd.to_numeric(df_clean['2010'], errors='coerce')
df_clean['2011'] = pd.to_numeric(df_clean['2011'], errors='coerce')

# Visualization Plot functions
# Define a function that plots a multiline for the top 5 countries.


def linePlot(data):
    
    
    # we start by selecting the top 5 countries
    top_5_countries = df_clean.head()['Country'].tolist()
    # Let's create a new dataframe with only the top 5 countries
    df_top_5 = df_clean[df_clean['Country'].isin(top_5_countries)]
    # then set the 'Country' column as the index of the dataframe
    df_top_5 = df_top_5.set_index('Country')
    df_top_5.T.plot()
    plt.xlabel('Year')
    plt.ylabel('Value')
    plt.title('Top 5 countries Oil Production between 2008-2018')
    plt.show()


# Define a function that plots a pie chart for mean oil production by country.


def pieChart(data):
    
    
    """
       We start by selecting the top 5 countries
       then create a new dataframe with only the top 5 countries
       Calculate the mean of the year columns for each row
       finally plot a pie chart of the means by country
    """
    top_5 = data.head()['Country'].tolist()
    
    df_top5 = data[data['Country'].isin(top_5)]
    
    df_top5['mean'] = df_top5.loc[:, '2008':'2018'].mean(axis=1)
    plt.pie(x=df_top5['mean'].values, labels=df_top5['Country'].values, \
            autopct='%1.1f%%')
    plt.title("Distribution of Yearly Means by country")
    plt.show()



# Define a function that's plot a bar chart


def barChart(data):
    
    
    top_10 = data.head(10)['Country'].tolist()
    df_top_10 = data[data['Country'].isin(top_10)]
    df_top_10['Mean'] = df_top_10.loc[:, '2008':'2018'].mean(axis=1)
    df_top_10 = df_top_10.sort_values(by='Mean', ascending=False)
    plt.bar(df_top_10['Country'], df_top_10['Mean'])
    plt.xlabel('Country')
    plt.ylabel('Mean Oil Production')
    plt.xticks(rotation=45)
    plt.title("The Average top 10 Oil Production by Country (2008-2018)")
    plt.show()
    
    """
       We start by selecting the top 10 countries
       then create a new dataframe with only the top 10 countries.
       Calculate the mean oil production across years for each country
       then sort the dataframe by the mean oil production
       and finally plot a bar chart
    """
    


# 1. Line plot

linePlot(df_clean)

# 2. Pie Chart
pieChart(df_clean)

# 3. Bar Chart

barChart(df_clean)
