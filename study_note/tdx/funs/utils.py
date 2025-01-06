'''
Author: frank 13121950875@163.com
Date: 2025-01-06 21:40:16
LastEditors: frank 13121950875@163.com
LastEditTime: 2025-01-06 21:40:43
FilePath: /study-note/study_note/tdx/funs/utils.py
Description: 

Copyright (c) 2025 by Frank, All Rights Reserved. 
'''


def clean_data(text):
    if isinstance(text, str):
        return text.replace('\x00', '').replace('\\', '')
    return text

