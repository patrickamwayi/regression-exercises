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


#def wrangle_zillow2():
#    if plot_residuals(y, yhat): creates a residual plot

#        regression_errors(y, yhat): returns the following values:
#        sum of squared errors (SSE)
#        explained sum of squares (ESS)
#        total sum of squares (TSS)
#        mean squared error (MSE)
#        root mean squared error (RMSE)
#        baseline_mean_errors(y): computes the SSE, MSE, and RMSE for the baseline model
#    else:
#         better_than_baseline(y, yhat): returns true if your model performs better than the baseline, otherwise false
#    return df
#


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

#def regression_errors(y, yhat):
#    '''
#   'regression errors'
 #   '''

 #   sum of squared errors(SSE)
 #   explained sum of squares(ESS)
  #  total sum of squares(TSS)
  #  mean squared error(MSE)
 #   root mean squared error(RMSE)

