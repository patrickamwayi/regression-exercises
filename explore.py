#standard imports
import numpy as np
import pandas as pd

#viz and stats
import pydataset
import matplotlib.pyplot as plt
import seaborn as sns

def plot_variable_pairs(df):
    sns.pairplot(data=df.sample(10000), kind='reg', corner = True, plot_kws={'line_kws':{'color':'red'}})
plot_variable_pairs(train)


#define funtion with features and outputs 3 different plots
def plot_categorical_and_continous(cat_var,con_var):
    plt.figure(figsize= (20,10))
    plt.subplot(131)
    sns.boxplot(x = cat_var, y = con_var, data = train.sample(10000))
    plt.subplot(132)
    sns.swarmplot(x = cat_var, y = con_var, data = train.sample(10000))
    plt.subplot(133)
    sns.barplot(x = cat_var, y = con_var, data = train.sample(10000))
    plt.figure()
    plt.show()
#plot graph
plot_categorical_and_continous("bedrooms","tax_value")
plt.show()