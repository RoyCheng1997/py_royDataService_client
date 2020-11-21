# -*- coding: utf-8 -*-
"""
Data Service Run Demo
"""

import dataApi

TOKEN = 'T3ZRzqjcPVxO2P9MEhFvEZRHSJ6lXjqpu6WoknKEZsHqAU26Bv'

# Ordinary request
df = dataApi.getFuturesData('M000', '2019/1/11', '2019/5/11', '1_d', datatype='tradingData',adjustS=True,token=TOKEN)
print(df.head())

# Request for futures indicators
seri = dataApi.getFuturesIndiData('M000', '2019/1/11', '2019/5/11', '1_d', datatype='tradingData',adjustS=True, token=TOKEN,
                              field='close_price', indicator='MA', indi_dict={'timeperiod': 20, 'matype': 1})

# Fast request for futures indicators
seri = dataApi.getFuturesIndiData1("M1905 MA @timeperiod:20|matype:1", '2019/1/11', '2019/5/11', token=TOKEN)
print(seri.head())


