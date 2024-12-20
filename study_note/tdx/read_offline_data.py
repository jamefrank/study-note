'''
Author: frank 13121950875@163.com
Date: 2024-12-20 23:56:52
LastEditors: frank 13121950875@163.com
LastEditTime: 2024-12-21 00:18:27
FilePath: /study-note/study_note/tdx/read_offline_data.py
Description: 

读取通达信软件数据目录的离线数据

Copyright (c) 2024 by Frank, All Rights Reserved. 
'''

from mootdx.reader import Reader

reader = Reader.factory(market='std', tdxdir='/mnt/c/new_tdx')

# 读取日线数据
data = reader.daily(symbol='600036')
print(data)

# 读取分钟数据
data = reader.minute(symbol='600036')
print("minute")
print(data)
reader.minute(symbol='000001', suffix='1')  # suffix = 1 一分钟，5 五分钟

# 读取时间线数据
data = reader.fzline(symbol='600036')
print("fzline")
print(data)