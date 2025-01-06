'''
Author: frank 13121950875@163.com
Date: 2024-12-21 00:01:50
LastEditors: frank 13121950875@163.com
LastEditTime: 2024-12-21 00:08:49
FilePath: /study-note/study_note/tdx/read_online_data.py
Description: 

读取线上数据

Copyright (c) 2024 by Frank, All Rights Reserved. 
'''

# TODO 非开市实践测试没有成功，还需要在开市时间进行测试

from mootdx.quotes import Quotes

# 标准市场
client = Quotes.factory(market='std', multithread=True, heartbeat=True, bestip=True, timeout=15)

# k 线数据
client.bars(symbol='600036', frequency=9, offset=10)

# 指数
client.index(symbol='000001', frequency=9)

# 分钟
client.minute(symbol='000001')