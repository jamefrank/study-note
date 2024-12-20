'''
Author: frank 13121950875@163.com
Date: 2024-12-21 00:19:11
LastEditors: frank 13121950875@163.com
LastEditTime: 2024-12-21 00:27:44
FilePath: /study-note/study_note/tdx/read_block_data.py
Description: 

读取离线数据中的板块信息

Copyright (c) 2024 by Frank, All Rights Reserved. 
'''


from mootdx.reader import Reader

# TODO 没有实践成功
reader = Reader.factory(market='std', tdxdir='/mnt/c/new_tdx')
data = reader.block(symbol='block_zs', group=False)
print(data)

# 分组格式
data = reader.block(symbol='block_zs', group=True)
print(data)


# # 写入新板块 (只能执行一次，重复执行会报错)
# reader = Reader.factory(market='std', tdxdir='/mnt/c/new_tdx')
# bsuc = reader.block_new(name='最优盈利板块', symbol=['600001', '600002', '600003', '600004', ])
# print(bsuc)

# 读取新板块信息文件夹

# 默认扁平格式
data = reader.block_new()
print(data)
# 分组格式
data = reader.block_new(group=True)
print(data)