'''
Author: frank 13121950875@163.com
Date: 2024-12-24 00:12:37
LastEditors: frank 13121950875@163.com
LastEditTime: 2025-01-06 23:11:29
FilePath: /study-note/study_note/tdx/test/read_fq_data.py
Description: 

读取复权数据
"00": 不复权, "01": 前复权, "02": 后复权

Copyright (c) 2024 by Frank, All Rights Reserved. 
'''


from mootdx.contrib.adjust import get_adjust_year


NFQ = "00"
QFQ = "01"
HFQ = "02"

# data = get_adjust_year(symbol='000001', year='2021', factor='01')
# print(data)


from mootdx.quotes import Quotes

client = Quotes.factory(market='std')
client.bars(symbol='600036', frequency=9, offset=10)

# 前复权
data = client.bars(symbol='600036', adjust='qfq', offset=10, start=0)
print(data)
# # 后复权
# data  = client.bars(symbol='600036', adjust='hfq')
# print(data)