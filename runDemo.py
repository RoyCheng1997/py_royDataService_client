# -*- coding: utf-8 -*-
"""
Data Service Run Demo
"""

import dataApi

TOKEN = 'xN48CyrWiod1OyRZVRZ3J826l8KLUZFCs52WbtQszR8w8KrbLt'

df = dataApi.getFuturesData('IF', '2019-07-01', '2019-08-02', '1_m', datatype='compare',database='ChenCheng',token=TOKEN)
print(df.head())

