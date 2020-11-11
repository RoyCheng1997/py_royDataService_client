# -*- coding: utf-8 -*-
"""
Data Service Run Demo
"""

import dataApi

TOKEN = 'T3ZRzqjcPVxO2P9MEhFvEZRHSJ6lXjqpu6WoknKEZsHqAU26Bv'

df = dataApi.getFuturesData('IF', '2019-07-01', '2019-08-02', '30_m', datatype='compare',adjustS=False,token=TOKEN)
print(df.head())

