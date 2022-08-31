#imports
import warnings
warnings.filterwarnings("ignore")
# tabular data stuff: numpy and pandas
import numpy as np
import pandas as pd
# data viz:
import matplotlib.pyplot as plt
import seaborn as sns

import env
import os

#sql query
sql='''
SELECT bedroomcnt, bathroomcnt, calculatedfinishedsquarefeet, taxvaluedollarcnt, yearbuilt, taxamount, fips
FROM properties_2017
WHERE propertylandusetypeid=261

'''

#connection set ip
def conn(db, user=env.username, host=env.host, password=env.password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'



#connection set ip
#def conn():
    #db = 'zillow'
    #database_url_base = f'mysql+pymysql://{env.username}:{env.password}@{env.host}/zillow'
    #return database_url_base 

#make function to acquire from sql
def new_zillow_data():
    df = pd.read_sql(sql,conn("zillow"))
    return df


def get_zillow_data():
    if os.path.isfile("zillow.csv"):
        #pull data from there
        df = pd.read_csv("zillow.csv", index_col = 0)
    else:
        #if not, run sql querry
        df = new_zillow_data()
        df.to_csv("zillow.csv")
    return df

def clean_zillow_data(df):
    #drop nulls
    df=df.dropna()
    #convert bedroom to int
    df.bedroomcnt = df.bedroomcnt.astype("int64")
    #convert calculatedfinishedsquarefeet to int
    df.calculatedfinishedsquarefeet = df.calculatedfinishedsquarefeet.astype("int64")
    #convert to int
    df.taxvaluedollarcnt = df.taxvaluedollarcnt.astype("int64")
    #convert to int
    df.yearbuilt = df.yearbuilt.astype("int64")
    #convert to int
    df.fips = df.fips.astype("int64")
    #rename columns
    df = df.rename(columns = {'bedroomcnt':'bedrooms', 
                          'bathroomcnt':'bathrooms', 
                          'calculatedfinishedsquarefeet':'area',
                          'taxvaluedollarcnt':'tax_value', 
                          'yearbuilt':'year_built',
                          'taxamount':'tax_amount'})
    return df


    
   #functions to remove outliers
def remove_outliers(df, k, col_list):
    ''' remove outliers from a list of columns in a dataframe 
        and return that dataframe
    '''
    
    for col in col_list:

        q1, q3 = df[col].quantile([.25, .75])  # get quartiles
        
        iqr = q3 - q1   # calculate interquartile range
        
        upper_bound = q3 + k * iqr   # get upper bound
        lower_bound = q1 - k * iqr   # get lower bound

        # return dataframe without outliers
        
        df = df[(df[col] > lower_bound) & (df[col] < upper_bound)]
        
    return df
 

def wrangle_zillow():
    #pull data funtion
    df = get_zillow_data()
    #clean data function
    df = clean_zillow_data(df)
    df = remove_outliers(df,1.5, ["bedrooms","bathrooms","area","year_built","tax_amount"])
    return df