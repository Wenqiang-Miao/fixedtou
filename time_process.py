#  时间相关的处理 
#  如果是定投日 返回 'investment_day'
#  如果是其它交易日 返回 'trade_day'  
#  如果是非交易日 返回 'non_trade_day'

import time
import datetime
from chinese_calendar import is_workday
from dateutil.relativedelta import relativedelta



def given_date_type_judge(given_date='2022-08-19', trade_day=4, day_type_li=['non_trade_day', 'trade_day', 'investment_day'] ):
    """
    判断给定日期是否为交易日,定投日
    Args:
        day_type (list, optional): _description_. Defaults to ['investment_day', 'trade_day', 'non_trade_day'].
    """
    #
    if isinstance(given_date, str):
        given_date = datetime.datetime.strptime(given_date, '%Y-%m-%d').date()
    
    day_type = 0  # 默认为非交易日
    if given_date.isoweekday() < 6 and is_workday(given_date): # 周一到周五 且 是交易日
        if given_date.isoweekday() == trade_day: # 是定投交易日
            day_type = 2
        else:
            day_type = 1
            
    print(day_type_li[day_type])
    return day_type_li[day_type]
            
    
      
def today_type_judge(trade_day=4, day_type_li=['non_trade_day', 'trade_day', 'investment_day']):
    """
    判断今天是否为交易日，定投日
    Args:
        trade_day (int, optional): _description_. Defaults to 4.
        day_type_li (list, optional): _description_. Defaults to ['non_trade_day', 'trade_day', 'investment_day'].

    Returns:
        _type_: _description_
    """
    cur_date = datetime.datetime.now().date()  # 当前日期
    return given_date_type_judge(cur_date, trade_day, day_type_li)
           
            
            
def comp_margin_date_from_given_date(given_date='2022-08-19', margin_type='week', margin_value=-15):
    """
    给定时间间隔，计算给定日期间隔后的日期
    Args:
        given_date (str, optional): _description_. Defaults to '2022-08-19'.
        margin_type (str, optional): _description_. Defaults to 'week'.
        margin_value (int, optional): 值为负，表示是之前的日期. Defaults to -15.

    Returns:
        _type_: _description_
    """
    if isinstance(given_date, str):
        given_date = datetime.datetime.strptime(given_date, '%Y-%m-%d').date()
    
    # given_date = datetime.datetime.now().date()  # 当前日期
    print(str(given_date), given_date.year)
    res_date = None

    if margin_type == 'day':
        res_date = given_date + relativedelta(days=margin_value)
        print(str(res_date), res_date.year)
        return res_date
    elif margin_type == 'week':
        res_date = given_date + relativedelta(weeks=margin_value)
        print(str(res_date), res_date.year)
        return res_date
    elif margin_type == 'month':
        res_date = given_date + relativedelta(months=margin_value)
        print(str(res_date), res_date.year)
        return res_date
    elif margin_type == 'year':
        res_date = given_date + relativedelta(years=margin_value)
        print(str(res_date), res_date.year)
        return res_date
    else:
        print('margin_type only support day, week, month, year')
        return res_date
            

 
def get_next_day(given_date='2022-08-19'):
    """
    返回给定日期的下一天
    Args:
        given_date (str, optional): _description_. Defaults to '2022-08-19'.

    Returns:
        _type_: _description_
    """
    if isinstance(given_date, str):
        given_date = datetime.datetime.strptime(given_date, '%Y-%m-%d').date()
    
    # given_date = datetime.datetime.now().date()  # 当前日期

    res_date = given_date + relativedelta(days=1)
    
    return res_date
    

 
def get_former_trade_day(given_date='2022-08-29'):
    """
    返回给定日期的前一个交易日
    Args:
        given_date (str, optional): _description_. Defaults to '2022-08-19'.

    Returns:
        _type_: _description_
    """
    if isinstance(given_date, str):
        given_date = datetime.datetime.strptime(given_date, '%Y-%m-%d').date()
    
    res_date = given_date + relativedelta(days=-1)
    while not is_workday(res_date):  # 不是交易日一直循环减少日期
        res_date = res_date + relativedelta(days=-1)
        
    #print(res_date)
    return res_date


def get_next_trade_day(given_date='2022-08-26'):
    """
    返回给定日期的下一个交易日
    Args:
        given_date (str, optional): _description_. Defaults to '2022-08-19'.

    Returns:
        _type_: _description_
    """
    if isinstance(given_date, str):
        given_date = datetime.datetime.strptime(given_date, '%Y-%m-%d').date()
    
    res_date = given_date + relativedelta(days=1)
    while not is_workday(res_date):  # 不是交易日一直循环增加日期
        res_date = res_date + relativedelta(days=1)
        
    #print(res_date)
    return res_date
 
    
       
if __name__ == '__main__':
    get_next_trade_day()
    
    cur_date = '2022-08-18'
    # cur_date = datetime.datetime.now().date()
    #given_date_type_judge(cur_date)
    
    


