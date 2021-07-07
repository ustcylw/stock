#! /usr/bin/env python
# coding: utf-8
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import pandas as pd
import stock_data.tusharepro_data as TSData


class CSVIO(object):

    @staticmethod
    def writer(df, csv_file, append=False):
        if os.path.exists(csv_file):
            if append:
                df.to_csv(csv_file, mode='a', header=None)
            else:
                os.system(f'rm -rf {csv_file}')
                df.to_csv(csv_file)
        else:
            df.to_csv(csv_file)

    @staticmethod
    def reader(csv_file):
        df = pd.read_csv(csv_file)
        return df


class TUShareDownload(object):
    def __init__(self, data_dir):
        self.data_dir = data_dir
        self.ts_data = TSData.TUShareProData()

    def dump_gupiaoliebiao(self, file_name='gupiaoliebiao.csv'):
        df = self.ts_data.get_stock_gupiaoliebiao()
        csv_file = os.path.join(self.data_dir, 'stocks/all', file_name)
        CSVIO.writer(df, csv_file, append=True)
        return df

    def load_gupiaoliebiao(self, file_name):
        csv_file = os.path.join(self.data_dir, 'stocks/all', file_name)
        df = CSVIO.reader(csv_file)
        return df

    def dump_jiaoyirili(self, file_name='jiaoyirili.csv'):
        df = self.ts_data.get_stock_jiaoyirili()
        csv_file = os.path.join(self.data_dir, 'stocks/all', file_name)
        CSVIO.writer(df, csv_file, append=True)
        return df

    def load_jiaoyirili(self, file_name):
        csv_file = os.path.join(self.data_dir, 'stocks/all', file_name)
        df = CSVIO.reader(csv_file)
        return df

    def dump_riK_start_end(self, ts_code='', start_date='20200101', end_date='20201231', cover=False):
        ts_code_dir = os.path.join(self.data_dir, ts_code)
        ts_code_year_dir = os.path.join(ts_code_dir, str(start_date)[0:4])
        if not os.path.exists(ts_code_year_dir):
            os.makedirs(ts_code_year_dir)
        csv_file = os.path.join(ts_code_year_dir, f'{start_date}--{end_date}.csv')
        if os.path.exists(csv_file) and (not cover):
            print(f'load from exist file.')
            return self.load_riK_start_end(ts_code=ts_code, start_date=start_date, end_date=end_date)
        print(f'loading {csv_file} ......')
        os.system(f'rm -rf {csv_file}')
        df = self.ts_data.get_stock_riK_start_end(ts_code=ts_code, start_date=start_date, end_date=end_date)
        CSVIO.writer(df, csv_file, append=False)
        print(f'load {csv_file} complete.')
        return df

    def load_riK_start_end(self, ts_code='', start_date='20200101', end_date='20201231'):
        csv_file = os.path.join(self.data_dir, ts_code, str(start_date)[0:4], f'{start_date}--{end_date}.csv')
        df = CSVIO.reader(csv_file)
        return df

    def dump_riK_start(self, ts_code='', trade_date='20200101', cover=False):
        ts_code_dir = os.path.join(self.data_dir, ts_code)
        ts_code_year_dir = os.path.join(ts_code_dir, str(trade_date)[0:4])
        if not os.path.exists(ts_code_year_dir):
            os.makedirs(ts_code_year_dir)
        csv_file = os.path.join(ts_code_year_dir, f'{trade_date}--{trade_date}.csv')
        if os.path.exists(csv_file) and (not cover):
            print(f'load from exist file.')
            return self.load_riK(ts_code=ts_code, trade_date=trade_date)
        print(f'loading {csv_file} ......')
        os.system(f'rm -rf {csv_file}')
        df = self.ts_data.get_stock_riK_start(ts_code=ts_code, trade_date=trade_date)
        CSVIO.writer(df, csv_file, append=False)
        print(f'load {csv_file} complete.')
        return df

    def load_riK_start(self, ts_code='', trade_date='20200102'):
        csv_file = os.path.join(self.data_dir, ts_code, str(trade_date)[0:4], f'{trade_date}--{trade_date}.csv')
        df = CSVIO.reader(csv_file)
        return df

    def dump_K_start_end_tongyonghangqing(self, ts_code='', start_date='', end_date='', freq='D', asset='E', adj=None, retry_count=3, cover=False):
        ts_code_dir = os.path.join(self.data_dir, ts_code)
        ts_code_year_dir = os.path.join(ts_code_dir, str(start_date)[0:4])
        if not os.path.exists(ts_code_year_dir):
            os.makedirs(ts_code_year_dir)
        csv_file = os.path.join(ts_code_year_dir, f'{start_date}--{end_date}--{freq}--{adj}.csv')
        if os.path.exists(csv_file) and (not cover):
            print(f'load from exist file.')
            return self.load_riK_start_end(ts_code=ts_code, start_date=start_date, end_date=end_date)
        print(f'loading {csv_file} ......')
        os.system(f'rm -rf {csv_file}')
        data = self.ts_data.get_stock_K_start_end_tongyonghangqing(ts_code=ts_code, start_date=start_date, end_date=end_date, freq=freq, asset=asset, adj=adj, retry_count=retry_count)
        CSVIO.writer(data, csv_file, append=False)
        print(f'load {csv_file} complete.')
        return data

    def load_K_start_end_tongyonghangqing(self, ts_code='', start_date='20200101', end_date='20201231', freq='D', adj=None):
        csv_file = os.path.join(self.data_dir, ts_code, str(start_date)[0:4], f'{start_date}--{end_date}--{freq}--{adj}.csv')
        data = CSVIO.reader(csv_file)
        return data

    def dump_fund_jijinliebiao_changnei(self):
        df = self.ts_data.get_fund_jijinliebiao_changnei()
        csv_file = os.path.join(self.data_dir, 'funds/all', 'jijinliebiao_changnei.csv')
        CSVIO.writer(df, csv_file, append=True)
        return df

    def load_fund_jijinliebiao_changnei(self):
        csv_file = os.path.join(self.data_dir, 'funds/all', 'jijinliebiao_changnei.csv')
        df = CSVIO.reader(csv_file)
        return df

    def dump_zijinliuxiang(self, api_name='moneyflow_hsgt', trade_date=None, start_date='20200101', end_date='20201231', cover=False):
        ts_code_dir = os.path.join(self.data_dir, 'stocks/all')
        if not os.path.exists(ts_code_dir):
            os.makedirs(ts_code_dir)
        if trade_date is None:
            csv_file = os.path.join(ts_code_dir, f'zijinliuxiang--{start_date}--{end_date}.csv')
        else:
            csv_file = os.path.join(ts_code_dir, f'zijinliuxiang--{trade_date}--00000000.csv')
        if os.path.exists(csv_file) and (not cover):
            print(f'load from exist file.')
            return self.load_zijinliuxiang(start_date=start_date, end_date=end_date)
        print(f'loading {csv_file} ......')
        os.system(f'rm -rf {csv_file}')
        data = self.ts_data.get_stock_zijinliuxiang(api_name=api_name, trade_date=trade_date, start_date=start_date, end_date=end_date)
        CSVIO.writer(data, csv_file, append=False)
        print(f'load {csv_file} complete.')
        return data

    def load_zijinliuxiang(self, trade_date=None, start_date='20200101', end_date='20201231'):
        ts_code_dir = os.path.join(self.data_dir, 'stocks/all')
        if trade_date is None:
            csv_file = os.path.join(ts_code_dir, f'zijinliuxiang--{start_date}--{end_date}.csv')
        else:
            csv_file = os.path.join(ts_code_dir, f'zijinliuxiang--{trade_date}--00000000.csv')
        data = CSVIO.reader(csv_file)
        return data

    def dump_hushenshidachengjiaogu(self, ts_code='', start_date='20200101', end_date='20201231', cover=False):
        ts_code_dir = os.path.join(self.data_dir, f'stocks/{ts_code}/hushenshidachengjiaogu')
        if not os.path.exists(ts_code_dir):
            os.makedirs(ts_code_dir)
        csv_file = os.path.join(ts_code_dir, f'hushenshidachengjiaogu--{start_date}--{end_date}.csv')
        if os.path.exists(csv_file) and (not cover):
            print(f'load from exist file.')
            return self.load_hushenshidachengjiaogu(ts_code=ts_code, start_date=start_date, end_date=end_date)
        print(f'loading {csv_file} ......')
        os.system(f'rm -rf {csv_file}')
        data = self.ts_data.get_stock_hushenshidachengjiaogu(ts_code=ts_code, start_date=start_date, end_date=end_date)
        CSVIO.writer(data, csv_file, append=False)
        print(f'load {csv_file} complete.')
        return data

    def load_hushenshidachengjiaogu(self, ts_code='', start_date='20200101', end_date='20201231'):
        ts_code_dir = os.path.join(self.data_dir, f'stocks/{ts_code}/hushenshidachengjiaogu')
        csv_file = os.path.join(ts_code_dir, f'hushenshidachengjiaogu--{start_date}--{end_date}.csv')
        data = CSVIO.reader(csv_file)
        return data


if __name__ == '__main__':

    import time

    data_dir = r'/data2/store/code/001/database/dbdata'

    tushare_downloader = TUShareDownload(data_dir=data_dir)

    # tushare_downloader.dump_gupiaoliebiao()
    df = tushare_downloader.load_gupiaoliebiao(file_name='gupiaoliebiao.csv')
    gupiaoliebiao = df.values
    print(f'gupiaoliebiao: \n{gupiaoliebiao.shape}\n{gupiaoliebiao}')
    print(f'='*80)

    # tushare_downloader.dump_jiaoyirili()
    df = tushare_downloader.load_jiaoyirili(file_name='jiaoyirili.csv')
    jiaoyirili = df.values
    print(f'jiaoyirili: \n{jiaoyirili.shape}\n{jiaoyirili}')
    print(f'='*80)

    # 获取19990101-20201231所有股票日K数据，放入同一个csv文件中
    # start_dates = ['19990101', '20000101', '20010101', '20020101', '20030101', '20040101', '20050101', '20060101', '20070101', '20080101', '20090101', '20100101', '20110101', '20120101', '20130101', '20140101', '20150101', '20160101', '20170101', '20180101', '20190101', '20200101']
    # end_dates = ['19991231', '20001231', '20011231', '20021231', '20031231', '20041231', '20051231', '20061231', '20071231', '20081231', '20091231', '20101231', '20111231', '20121231', '20131231', '20141231', '20151231', '20161231', '20171231', '20181231', '20191231', '20201231']
    # freqs = ['D', 'W', 'M']  # ['1', '5', '15', '30', '60', 'D', 'W', 'M']
    # adjs = [None, 'qfq', 'hfq']
    # for i in range(len(gupiaoliebiao)):
    #     for start_date, end_date in zip(start_dates, end_dates):
    #         for freq in freqs:
    #             for adj in adjs:
    #                 ts_code = gupiaoliebiao[i][1]
    #                 cover = True
    #                 print(f'{ts_code}\t{start_date} / {end_date}\t{cover}\t{freq}\t{adj}')
    #                 tushare_downloader.dump_K_start_end_tongyonghangqing(ts_code=ts_code, start_date=start_date, end_date=end_date, freq=freq, asset='E', adj=adj)
    #                 df = tushare_downloader.load_K_start_end_tongyonghangqing(ts_code=ts_code, start_date=start_date, end_date=end_date, freq=freq, adj=adj)
    #                 # tushare_downloader.dump_riK_start_end(ts_code=ts_code, start_date=start_date, end_date=end_date, cover=cover)
    #                 # df = tushare_downloader.load_riK_start_end(ts_code=ts_code, start_date=start_date, end_date=end_date)
    #                 # print(f'{ts_code}: \n{df.values.shape}\n{df.values}')
    #                 print(f'{ts_code}: \n{df.values.shape}')
    #                 print(f'='*80)
    #                 time.sleep(5)


    # 获取20210101-至今所有股票数据，每天放入一个csv文件中
    # 还不能用
    # trade_date = '19990101'
    # for i in range(2):
    #     # for j in range(10):
    #         ts_code = gupiaoliebiao[i][1]
    #         trade_date = jiaoyirili[j][2]
    #         start_date = '19990101'
    #         end_date = '20201231'
    #         cover = True
    #         print(f'{ts_code}\t{trade_date}\t{cover}')
    #         tushare_downloader.dump_riK_start(ts_code=ts_code, trade_date=trade_date, cover=cover)
    #         df = tushare_downloader.load_riK_start(ts_code=ts_code, trade_date=trade_date)
    #         tushare_downloader.dump_riK_start_end(ts_code=ts_code, start_date=trade_date, end_date=trade_date, cover=cover)
    #         df = tushare_downloader.load_riK_start_end(ts_code=ts_code, start_date=trade_date, end_date=trade_date)
    #         print(f'{ts_code}: \n{df.values.shape}\n{df.values}')
    #         print(f'='*80)


    # 资金流向
    # start_dates = ['19990101', '20000101', '20010101', '20020101', '20030101', '20040101', '20050101', '20060101', '20070101', '20080101', '20090101', '20100101', '20110101', '20120101', '20130101', '20140101', '20150101', '20160101', '20170101', '20180101', '20190101', '20200101']
    # end_dates = ['19991231', '20001231', '20011231', '20021231', '20031231', '20041231', '20051231', '20061231', '20071231', '20081231', '20091231', '20101231', '20111231', '20121231', '20131231', '20141231', '20151231', '20161231', '20171231', '20181231', '20191231', '20201231']
    # for start_date, end_date in zip(start_dates, end_dates):
    #     tushare_downloader.dump_zijinliuxiang(start_date=start_date, end_date=end_date)
    #     df = tushare_downloader.load_zijinliuxiang(start_date=start_date, end_date=end_date)
    #     print(f'zijinliuxiang: {df.values.shape}')
    #     print(f'='*80)

    # 沪深十大成交股
    start_dates = ['19990101', '20000101', '20010101', '20020101', '20030101', '20040101', '20050101', '20060101', '20070101', '20080101', '20090101', '20100101', '20110101', '20120101', '20130101', '20140101', '20150101', '20160101', '20170101', '20180101', '20190101', '20200101']
    end_dates = ['19991231', '20001231', '20011231', '20021231', '20031231', '20041231', '20051231', '20061231', '20071231', '20081231', '20091231', '20101231', '20111231', '20121231', '20131231', '20141231', '20151231', '20161231', '20171231', '20181231', '20191231', '20201231']
    for i in range(len(gupiaoliebiao)):
        for start_date, end_date in zip(start_dates, end_dates):
            ts_code = gupiaoliebiao[i][1]
            print(f'===  {ts_code}\t{start_date} / {end_date} ===')
            tushare_downloader.dump_hushenshidachengjiaogu(ts_code=ts_code, start_date=start_date, end_date=end_date)
            df = tushare_downloader.load_hushenshidachengjiaogu(ts_code=ts_code, start_date=start_date, end_date=end_date)
            print(f'{ts_code}: \n{df.values}')
            print(f'='*80)
            time.sleep(2)



    # =============================================================================
    # 基金
    # tushare_downloader.dump_fund_jijinliebiao_changnei()
    # df = tushare_downloader.load_fund_jijinliebiao_changnei()
    # jijinliebiao_changnei = df.values
    # print(f'jijinliebiao_changnei: \n{jijinliebiao_changnei.shape}\n{jijinliebiao_changnei}')
    # print(f'='*80)
