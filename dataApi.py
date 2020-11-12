# -*- coding: utf-8 -*-
'''
Data API
    -- Data Functions would be defined here 
'''

import requests
import pandas as pd
import numpy as np

PATH = 	"http://roycheng.natapp1.cc"
nan, NaN = np.nan, np.nan

def getFuturesData(futures, start, end, freq, datatype, token, adjustS=False):
    '''Get Futures Data'''
    print("Getting Data...")
    payload = {'futures': futures, 'start' : start, 'end' : end, 'freq' : freq, 'datatype' : datatype, 'adjustS':adjustS, 'token' : token}
    res = requests.get(PATH+"/futures", params=payload)
    if("ERROR" in res.text):
        return pd.DataFrame({"ERROR:" : res.text})
    df = pd.DataFrame(eval(res.text))
    try:
        df.index = pd.to_datetime(df.index)
    except:
        pass
    return df
