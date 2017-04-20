# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 11:10:42 2017

@author: Andres
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import datetime

#Create datelist
date = datetime.datetime.today()
n = 2600
datelist = []
for x in range (0, n):
    d = (date - datetime.timedelta(days = x))
    datelist.append(d.strftime('%Y-%m-%d'))

# Load dataset
stocks = ["AAPL", "TSLA", "QCOM", "INTU"]
alldata = pd.DataFrame(columns = ['Date'])
alldata['Date'] = datelist

#Extract data to set
for stock in stocks:
    url = "http://chart.finance.yahoo.com/table.csv?s="+stock+"&a=3&b=20&c=2010&d=3&e=20&f=2017&g=d&ignore=.csv"
    dataset = pd.read_csv(url, index_col=None)     
    dataset = dataset.set_index('Date')
    alldata[stock] = alldata['Date'].map(dataset['Close']).values
    
    

    
    
