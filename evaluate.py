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


#  function that plot_residuals(y, yhat): creates a residual plot
def plot_residual(y, yhat):
    '''
    "creates a residual plot from y and yhat"
    '''
    # compute residuals
    residual = (yhat - y)
    sns.scatterplot(x=y, y=residual,color='blue', label='residual of regression')
    plt.axhline(y=0)
    plt.legend()
    plt.title("Residual scatter plot")
    plt.show()

#  function that plot_residuals(y, yhat): creates a residual plot
def plot_residuals(y, yhat):
    residuals = y - yhat
    
    plt.scatter(x=y, y=residuals)
    plt.xlabel('Home Value')
    plt.ylabel('Residuals')
    plt.title('Residual vs Home value plot')
    plt.show()


#function with regression_errors(y, yhat): returns SSE, ESS, TSS, MSE, RMSE

def regression_errors(y, yhat):
    MSE = mean_squared_error(y, yhat)
    SSE = MSE * len(y)
    RMSE = MSE**.5
    
    ESS = ((yhat - y.mean())**2).sum()
    TSS = ESS + SSE
    
    return SSE, ESS, TSS, MSE, RMSE


#function with baseline_mean_errors(y): computes the SSE, MSE, and RMSE for the baseline model
def baseline_mean_errors(y):
    baseline = np.repeat(y.mean(), len(y))
    
    MSE = mean_squared_error(y, baseline)
    SSE = MSE * len(y)
    RMSE = MSE**.5
    
    return SSE, MSE, RMSE


#  function better_than_baseline(y, yhat): returns true if your model performs better than the baseline, otherwise false
def better_than_baseline(y, yhat):
    SSE, ESS, TSS, MSE, RMSE = regression_errors(y, yhat)
    
    SSE_baseline, MSE_baseline, RMSE_baseline = baseline_mean_errors(y)
    
    if SSE < SSE_baseline:
        print('My OSL model performs better than baseline')
    else:
        print('My OSL model performs worse than baseline. :( )')
        