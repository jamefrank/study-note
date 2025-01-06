'''
Author: frank 13121950875@163.com
Date: 2025-01-06 20:52:55
LastEditors: frank 13121950875@163.com
LastEditTime: 2025-01-06 22:08:19
FilePath: /study-note/study_note/tdx/funs/stocks_update.py
Description: 

数据更新到本地

Copyright (c) 2025 by Frank, All Rights Reserved. 
'''

from study_note import TDX_DATA_DIR

from mootdx.quotes import Quotes
from mootdx import consts

from study_note.tdx.funs.utils import clean_data

client = Quotes.factory(market='std')

# update sh codes
symbol = client.stocks(market=consts.MARKET_SH)
stocks = symbol[symbol['code'].str.startswith('60')]
stocks = stocks[['code', 'name']]
stocks['name'] = stocks['name'].map(clean_data)
codes_path = TDX_DATA_DIR / "codes_sh.csv"
stocks.to_csv(codes_path, index=False)
sh_num = len(stocks)
print(f"sh nums:{sh_num}")

# update sz codes
symbol = client.stocks(market=consts.MARKET_SZ)
stocks = symbol[symbol['code'].str.startswith('00')]
stocks = stocks[['code', 'name']]
stocks['name'] = stocks['name'].map(clean_data)
codes_path = TDX_DATA_DIR / "codes_sz.csv"
stocks.to_csv(codes_path, index=False)
sz_num = len(stocks)
print(f"sz nums:{sz_num}")

print(f"total nums:{sh_num + sz_num}")

