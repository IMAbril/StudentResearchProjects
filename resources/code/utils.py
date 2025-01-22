#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Useful functions for my projects
"""
import datetime
import pandas as pd
import random
import radar
from faker import Faker
fake = Faker()
def generateTimeSeriesData(n):
    """
    Parameters
    ----------
    n : int. number of observations.

    Returns
    -------
    df: pandas dataframe. Columns of df : Date, Price

    """
    listdata = []
    start = datetime.datetime(2019,8,1)
    end = datetime.datetime(2019,8,30)
    
    for _ in range(n):
        date = radar.random_datetime(start = '2019-08-1', stop = '2019-08-30').strftime("%Y-%m-%d")
        price = round(random.uniform(900,1000), 4)
        
        listdata.append([date,price])
    
    df = pd.DataFrame(listdata, columns=['Data','Price'])
    df['Date'] = pd.to_datetime(df['Date'], format = '%Y-%m-%d')
    df = df.groupby(by='Date').mean()
    
    return df