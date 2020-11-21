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
    '''
    Get Futures Data
    
    Args*:
        futures: str, futures ticker, active contract X000
        start: str, can be turned to pd.datetime
        end: str, can be turned to pd.datetime
        freq: str, requesting frequency
        datatype: str, data type, see more in github page
        token: str, the token you have
        adjustS: boolean, whether to adjust the data, work for active contract
    
    '''
    print("Getting Futures Data...")
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


def getFuturesIndiData(futures, start, end, freq, datatype, token, adjustS=False, field='close_price', indicator='MA', indi_dict={'timeperiod': 14, 'matype': 1}):
    '''
    Get Futures Indicator Data
    
    Args*:
        futures: str, futures ticker, active contract X000
        start: str, can be turned to pd.datetime
        end: str, can be turned to pd.datetime
        freq: str, requesting frequency
        datatype: str, data type, see more in github page
        token: str, the token you have
        adjustS: boolean, whether to adjust the data, work for active contract
        field: str, field to use in priceshot
        indicator: str, indicator name, ask author for more indicators and paraDict
        indi_dict: dict, used to calculate indicator, ask author for more indicators and paraDict
    '''
    print("Getting Futures Indicator Data...")
    indi_dict = str(indi_dict)
    payload = locals()
    res = requests.get(PATH+"/futures_indi", params=payload)
    if("ERROR" in res.text):
        return pd.DataFrame({"ERROR:" : res.text})
    seri = pd.Series(eval(res.text))
    try:
        seri.index = pd.to_datetime(seri.index)
    except:
        pass
    return seri


def getFuturesIndiData1(string, start, end, token):
    '''
    Get Futures Indicator Data, faster version
    String format: "M000 MA @timeperiod:20|matype:1"
    
    Args*:
        string: str, request string, see above format, "ticker indicatorName @parameter1:value1|parameter2:value2"
        start: str, can be turned to pd.datetime
        end: str, can be turned to pd.datetime
        token: str, the token you have
    '''
    print("Getting Futures Indicator Data Fast...")
    payload = locals()
    res = requests.get(PATH+"/futures_indi1", params=payload)
    if("ERROR" in res.text):
        return pd.DataFrame({"ERROR:" : res.text})
    seri = pd.Series(eval(res.text))
    try:
        seri.index = pd.to_datetime(seri.index)
    except:
        pass
    return seri

    
    
    
    
    
    
    
    