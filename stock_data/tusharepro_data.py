#! /usr/bin/env python
# coding: utf-8
import os, sys
import numpy as np
import pandas as pd
import tushare as ts


class TUShareProData(object):
    def __init__(
            self,
            token='ca7a26820a3f427c3245156563b64685c5a61cc7b080fcd4dd4b93df'
    ):
        self.token = token
        ts.set_token(self.token)
        self.pro = ts.pro_api()

    # =============================================================================
    # 股票
    def get_stock_gupiaoliebiao(self, api_name='stock_basic', exchange='', list_status='L', fields='', **kwargs):
        # data = self.pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
        data = self.pro.query(
            api_name=api_name,
            exchange=exchange,
            list_status=list_status
            # fields='ts_code,symbol,name,area,industry,list_date'
        )
        return data

    def get_stock_jiaoyirili(self, api_name='trade_cal', start_date=20200101, end_date='20201231'):
        data = self.pro.query(api_name=api_name, start_date=start_date, end_date=end_date)
        return data

    def get_stock_riK_start_end(self, api_name='daily', ts_code='', start_date='20200101', end_date='20201231'):
        data = self.pro.query(api_name=api_name, ts_code=ts_code, start_date=start_date, end_date=end_date)
        return data

    def get_stock_riK_start(self, api_name='daily', ts_code='', trade_date='20200101'):
        data = self.pro.query(api_name=api_name, ts_code=ts_code, start_date=trade_date)
        return data

    def get_stock_K_start_end_tongyonghangqing(self, ts_code='', start_date='', end_date='', freq='D', asset='E', adj=None, retry_count=3):
        '''
        BAR数据
        Parameters:
            ts_code:证券代码，支持股票,ETF/LOF,期货/期权,港股,数字货币
            start_date:开始日期  YYYYMMDD
            end_date:结束日期 YYYYMMDD
            freq:支持1/5/15/30/60分钟,周/月/季/年
            asset:证券类型 E:股票和交易所基金，I:沪深指数,C:数字货币,FT:期货 FD:基金/O期权/H港股/CB可转债
            exchange:市场代码，用户数字货币行情
            adj:复权类型,None不复权,qfq:前复权,hfq:后复权
            ma:均线,支持自定义均线频度，如：ma5/ma10/ma20/ma60/maN
            offset:开始行数（分页功能，从第几行开始取数据）
            limit: 本次提取数据行数
            factors因子数据，目前支持以下两种：
                vr:量比,默认不返回，返回需指定：factor=['vr']
                tor:换手率，默认不返回，返回需指定：factor=['tor']
                            以上两种都需要：factor=['vr', 'tor']
            retry_count:网络重试次数
        Return
        DataFrame
        code:代码
        open：开盘close/high/low/vol成交量/amount成交额/maN均价/vr量比/tor换手率

             期货(asset='FT')
        code/open/close/high/low/avg_price：均价  position：持仓量  vol：成交总量
        '''
        df = ts.pro_bar(ts_code=ts_code, adj=adj, start_date=start_date, end_date=end_date, freq=freq, asset=asset, retry_count=retry_count)
        return df

    def get_stock_zijinliuxiang(self, api_name='moneyflow_hsgt', trade_date=None, start_date='20200101', end_date='20201231'):
        if trade_date == None:
            data = self.pro.query(api_name=api_name, start_date=start_date, end_date=end_date)
        else:
            data = self.pro.query(api_name=api_name, trade_date=trade_date)
        return data

    def get_stock_hushenshidachengjiaogu(self, ts_code='', start_date='20200101', end_date='20201231'):
        data = self.pro.query(api_name='hsgt_top10', ts_code=ts_code, start_date=start_date, end_date=end_date)
        return data

    def get_stock_chigumingxi(self):
        # TODO
        data = self.pro.hk_hold(trade_date='20190625', exchange='SH')
        return data

    # 股票
    # =============================================================================

    # =============================================================================
    # 基金
    def get_fund_jijinliebiao_changnei(self):
        df = self.pro.fund_basic(market='E')
        return df

    # 基金
    # =============================================================================
