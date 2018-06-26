import tushare as ts

data = ts.get_tick_data('300027', date='2014-01-09') #一次性获取全部数据
print(data)