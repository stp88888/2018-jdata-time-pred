# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 14:45:20 2018

@author: STP
"""

import pandas as pd
import numpy as np

def get_periods_data(data, start_month, end_month):
    if start_month < end_month:
        return data[(data['month'] >= start_month) & (data['month'] <= end_month)]
    else:
        return pd.concat([data[data['month'] >= start_month], data[data['month'] <= end_month]])



path = './/JDATA_A//'

item_data = pd.read_csv(path+'jdata_sku_basic_info.csv')
user_data = pd.read_csv(path+'jdata_user_basic_info.csv')
comment_data = pd.read_csv(path+'jdata_user_comment_score.csv')
action_data = pd.read_csv(path+'jdata_user_action.csv')
order_data = pd.read_csv(path+'jdata_user_order.csv')

action_data['month'] = action_data['a_date'].apply(lambda x:x.split('-')[1])
action_data['day'] = action_data['a_date'].apply(lambda x:x.split('-')[2])
del action_data['a_date']

