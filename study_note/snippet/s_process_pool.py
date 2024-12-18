'''
Author: frank 13121950875@163.com
Date: 2024-12-12 23:16:22
LastEditors: frank 13121950875@163.com
LastEditTime: 2024-12-12 23:16:26
FilePath: /mootdx/stock-policy/study_test/s_process_pool.py
Description: 

进程池使用示例

Copyright (c) 2024 by Frank, All Rights Reserved. 
'''


import concurrent.futures
import time
import random

# 定义一个模拟的任务函数
def task_function(task_name, duration):
    print(f"Task '{task_name}' is starting and will take {duration:.2f} seconds.")
    # 模拟任务执行时间
    time.sleep(duration)
    print(f"Task '{task_name}' has finished.")
    return f"Result of Task '{task_name}'"

if __name__ == "__main__":
    # 创建一个包含4个工作进程的进程池
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        # 准备一些任务，每个任务有不同的参数
        tasks = [
            ("Task-1", random.uniform(0.5, 2.0)),
            ("Task-2", random.uniform(0.5, 2.0)),
            ("Task-3", random.uniform(0.5, 2.0)),
            ("Task-4", random.uniform(0.5, 2.0)),
            ("Task-5", random.uniform(0.5, 2.0))
        ]
        
        # 使用列表推导式来提交所有任务，并获取future对象
        futures = [executor.submit(task_function, name, dur) for name, dur in tasks]
        
        # 遍历完成的future对象并获取结果
        for future in concurrent.futures.as_completed(futures):
            try:
                result = future.result()
                print(result)
            except Exception as exc:
                print(f"The task generated an exception: {exc}")

    print("All tasks have been processed.")
