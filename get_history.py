"""
# 获取指数的历史数据，主要是PE信息；后续利用这个信息确定估值
"""

import os
import sys
import akshare as ak
import numpy as np
import pandas as pd



index_name_li = ['沪深300', '中证500', '创业板50']

def get_one_index_history(index_name='中证500', indicator="市盈率", save_dirs='./data_dir/'):
    index_value_hist_funddb_df = ak.index_value_hist_funddb(symbol=index_name, indicator=indicator)
    
    # print(index_value_hist_funddb_df)
    # print(type(index_value_hist_funddb_df))

    index_value_hist_funddb_df = pd.DataFrame(index_value_hist_funddb_df, columns = ['日期', indicator])
    #return index_value_hist_funddb_df
    # 保存
    index_value_hist_funddb_df.to_csv(os.path.join(save_dirs, '{}_{}.csv'.format(index_name, indicator)), index=None)
    #cur_date = datetime.datetime.now().date()  # 当前日期
    
    

if __name__ == '__main__':
    indicator="市净率"
    get_one_index_history(index_name_li[0], indicator=indicator)
    





