from sqlalchemy import create_engine
import tushare as ts
import datetime





# df = ts.get_tick_data('300027', date='2014-12-22')
#
#
#
# print(df.head(10))
#
# print(df.index)
#
# print('df.columns')
# print(df.columns)
# # 存入数据库
#
#
# #追加数据到现有表


class SaveStock2Mysql():
    m_sql_connect = create_engine('mysql+pymysql://root:YXvnaaOw16I97iDo@192.168.1.132:3306/stock?charset=utf8')

    def __init__(self):
        # 当前日期
        nowDate = datetime.datetime.now()
        self.m_nNowYear = nowDate.year
        self.m_nNowMonth = nowDate.month
        self.m_nNwoDay = nowDate.day

    def __del__(self):
        pass
        # self.stop()

    def SaveDf(self, stock_code):
        string_format = '%d-%02d-%02d'
        nYear = 2014
        nMonth = 1
        nDay = 1

        # stock_code = '300027'
        # stock_date = '2014-12-22'
        # stock_date = '1990-12-01'

        for nYear in range(1990, self.m_nNowYear):
            for nMonth in range(1, 12):
                for nDay in range(1, 31):
                    stock_date = string_format % (nYear, nMonth, nDay)
                    print(stock_date)

                    try:
                        df = ts.get_tick_data(stock_code, stock_date)
                        if len(df.head(10)) == 10:
                            # 存入数据库
                            df.to_sql('tick_data', self.m_sql_connect, if_exists='append')
                    except Exception as err:
                        print(err)

if __name__ == '__main__':
    SaveData = SaveStock2Mysql()
    stock_code = 300027
    SaveData.SaveDf(str(stock_code))