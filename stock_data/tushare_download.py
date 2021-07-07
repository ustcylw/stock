#! /usr/bin/env python
# coding: utf-8
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import pandas as pd
import stock_data.tushare_data as TSData


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
        self.ts_data = TSData.TUShareData()

    def dump_gupiaoliebiao(self, file_name='gupiaoliebiao.csv', date='2021-01-01', append=False):
        df = self.ts_data.get_stock_gupiaoliebiao(date)
        csv_file = os.path.join(self.data_dir, file_name)
        CSVIO.writer(df, csv_file, append)
        return df

    def load_gupiaoliebiao(self, file_name):
        csv_file = os.path.join(self.data_dir, file_name)
        df = CSVIO.reader(csv_file)
        return df


if __name__ == '__main__':

    data_dir = r'/data2/store/code/001/database/dbdata/stocks/all'

    tushare_downloader = TUShareDownload(data_dir=data_dir)

    tushare_downloader.dump_gupiaoliebiao()
    df = tushare_downloader.load_gupiaoliebiao(file_name='gupiaoliebiao.csv')
    print(f'df: {df}')
