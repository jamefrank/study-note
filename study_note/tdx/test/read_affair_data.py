'''
Author: frank 13121950875@163.com
Date: 2024-12-21 00:10:04
LastEditors: frank 13121950875@163.com
LastEditTime: 2024-12-21 00:36:14
FilePath: /study-note/study_note/tdx/read_affair_data.py
Description: 

下载财务数据

Copyright (c) 2024 by Frank, All Rights Reserved. 
'''


from mootdx.affair import Affair

# 远程文件列表
files = Affair.files()
for file in files:
    print(file)

# 下载单个
res = Affair.fetch(downdir='tmp', filename='gpcw19960630.zip')
print(res)

# 下载全部
Affair.fetch(downdir='tmp')


# 解析本地数据 + 保存成其他格式的文件
result = Affair.parse(downdir='tmp', filename='gpcw20170930.zip')

# 保存 csv 文件
result.to_csv('gpcw20170930.csv')

# TODO 没有实践成功，但是暂时也不需要
# # 保存 Excel 文件
# result.to_excel('gpcw20170930.xls')

# 命令行写入到文件
# TODO 如果当前文件夹下没有zip文件，只会下载该文件，但是不会完成转换
# mootdx affair -f gpcw20000930.zip -o gpcw20170930.csv


# 财务数据字段对照表
# https://www.mootdx.com/zh-cn/latest/api/fields/