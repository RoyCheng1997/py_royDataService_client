# -*- coding: utf-8 -*-
"""
Data Service Run Demo
"""

import dataApi

TOKEN = 'T3ZRzqjcPVxO2P9MEhFvEZRHSJ6lXjqpu6WoknKEZsHqAU26Bv'

df = dataApi.getFuturesData('M000', '2019/1/11', '2019/5/11', '1_d', datatype='tradingData',adjustS=True,token=TOKEN)
print(df.head())
