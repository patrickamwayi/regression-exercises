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



