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
dt = datetime.datetime.today()
n = 2800
dp = dt - datetime.timedelta(days = n)
datelist = []
for x in range (0, n):
    d = (dt - datetime.timedelta(days = x))
    datelist.append(d.strftime('%Y-%m-%d'))


# Load dataset
stocks = ["AAPL", "TSLA", "QCOM", "INTU"]
alldata = pd.DataFrame(columns = ['Date'])
alldata['Date'] = datelist

#Extract data to set
for stock in stocks:
    url = "http://chart.finance.yahoo.com/table.csv?s="+stock+"&a="+str(int(dp.month - 1))+"&b="+str(dp.day)+"&c="+str(dp.year)+"&d="+str(int(dt.month - 1))+"&e="+str(dt.day)+"&f="+str(dt.year)+"&g=d&ignore=.csv"
    dataset = pd.read_csv(url, index_col=None)     
    dataset = dataset.set_index('Date')
    alldata[stock] = alldata['Date'].map(dataset['Close']).values
    

    
    
