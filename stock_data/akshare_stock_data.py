#! /usr/bin/env python
# coding: utf-8
import os, sys
import numpy as np
import akshare as ak


class AKShareStock(object):
    def __init__(self):
        pass

    def stock_ak_agu_shichangzongmao_sh(self):
        '''
        上海证券交易所
        接口: stock_sse_summary
        目标地址: http://www.sse.com.cn/market/stockdata/statistic/
        描述: 上海证券交易所-股票数据总貌
        限量: 单次返回最近交易日的股票数据总貌数据(当前交易日的数据需要交易所收盘后统计)
        输入参数
            名称	类型	必选	描述
            -	-	-	-
        输出参数-实时行情数据
            名称	类型	默认显示	描述
            type	str	Y	-
            item	str	Y	-
            number	float	Y	-
        '''
        stock_sse_summary_df = ak.stock_sse_summary()
        return stock_sse_summary_df

    def stock_ahgu_gupiaozidian(self):
        '''
        A+H股票字典
        接口: stock_zh_ah_name
        目标地址: http://stockapp.finance.qq.com/mstats/#mod=list&id=hk_ah&module=HK&type=AH
        描述: A+H 股数据是从腾讯财经获取的数据, 历史数据按日频率更新
        限量: 单次返回所有 A+H 上市公司的代码和名称字典
        输入参数
            名称	类型	必选	描述
            -	-	-	-
        输出参数-历史行情数据
            名称	    类型	    默认显示	    描述
            字典	    str	    Y	        股票代码和股票名称的映射
        '''
        stock_zh_ah_name_dict = ak.stock_zh_ah_name()
        return stock_zh_ah_name_dict

    def stock_ak_agu_shishihangqing(self):
        '''
        接口: stock_zh_a_spot
        目标地址: http://vip.stock.finance.sina.com.cn/mkt/#hs_a
        描述: A 股数据是从新浪财经获取的数据, 重复运行本函数会被新浪暂时封 IP, 建议增加时间间隔
        限量: 单次返回所有 A 股上市公司的实时行情数据
        输入参数
            名称	类型	必选	描述
            -	-	-	-
        输出参数-实时行情数据
            名称	类型	默认显示	描述
            代码	str	Y	-
            名称	str	Y	-
            最新价	float	Y	-
            涨跌幅	float	Y	-
            涨跌额	float	Y	-
            买入	float	Y	-
            卖出	float	Y	-
            成交量	float	Y	-
            成交额	float	Y	-
            今开	float	Y	-
            昨收	float	Y	-
            最高	float	Y	-
            最低	float	Y	-
        '''
        return ak.stock_zh_a_spot()

    def stock_ak_agu_lishihangqing_riK_xl(self, code="sh601939", start="19900101", end="22001220", adjust=''):
        '''
        接口: stock_zh_a_daily
        目标地址: https://finance.sina.com.cn/realstock/company/sh600006/nc.shtml(示例)
        描述: A 股数据是从新浪财经获取的数据, 历史数据按日频率更新
        限量: 单次返回指定 A 股上市公司指定日期间的历史行情日频率数据
        输入参数
            名称	        类型	    必选	描述
            symbol	    str	    Y	symbol='sh600000'; 股票代码可以在 ak.stock_zh_a_spot() 中获取
            start_date	str	    Y	start_date='20201103'; 开始查询的日期
            end_date	str	    Y	end_date='20201116'; 结束查询的日期
            adjust	    str	    Y	默认返回不复权的数据; qfq: 返回前复权后的数据; hfq: 返回后复权后的数据; hfq-factor: 返回后复权因子; qfq-factor: 返回前复权因子
        股票数据复权
            1.为何要复权：由于股票存在配股、分拆、合并和发放股息等事件，会导致股价出现较大的缺口。 若使用不复权的价格处理数据、计算各种指标，将会导致它们失去连续性，且使用不复权价格计算收益也会出现错误。 为了保证数据连贯性，常通过前复权和后复权对价格序列进行调整。
            2.前复权：保持当前价格不变，将历史价格进行增减，从而使股价连续。 前复权用来看盘非常方便，能一眼看出股价的历史走势，叠加各种技术指标也比较顺畅，是各种行情软件默认的复权方式。 这种方法虽然很常见，但也有两个缺陷需要注意。
            2.1 为了保证当前价格不变，每次股票除权除息，均需要重新调整历史价格，因此其历史价格是时变的。 这会导致在不同时点看到的历史前复权价可能出现差异。
            2.2 对于有持续分红的公司来说，前复权价可能出现负值。
            3.后复权：保证历史价格不变，在每次股票权益事件发生后，调整当前的股票价格。 后复权价格和真实股票价格可能差别较大，不适合用来看盘。 其优点在于，可以被看作投资者的长期财富增长曲线，反映投资者的真实收益率情况。
            4.在量化投资研究中普遍采用后复权数据。
        输出参数-历史行情数据
            名称	类型	默认显示	描述
            date	datetime	Y	交易日
            close	float	Y	收盘价
            high	float	Y	最高价
            low	float	Y	最低价
            open	float	Y	开盘价
            volume	float	Y	成交量(股)
            outstanding_share	float	Y	流动股本(股)
            turnover	float	Y	换手率=成交量(股)/流动股本(股)
        例子：
        前复权: stock_zh_a_daily_qfq_df = ak.stock_zh_a_daily(symbol="sz000002", start_date="20101103", end_date="20201116", adjust="qfq")
        后复权: stock_zh_a_daily_hfq_df = ak.stock_zh_a_daily(symbol="sz000002", start_date='20201103', end_date='20201116', adjust="hfq")
        前复权因子: qfq_factor_df = ak.stock_zh_a_daily(symbol="sz000002", adjust="qfq-factor")
        后复权因子: hfq_factor_df = ak.stock_zh_a_daily(symbol="sz000002", adjust="hfq-factor")
        '''
        stock_zh_a_daily_qfq_df = ak.stock_zh_a_daily(
            symbol=code,
            start_date=start,
            end_date=end,
            adjust=adjust
        )
        return stock_zh_a_daily_qfq_df

    def stock_ak_agu_lishihangqing_fenshiK_xl(self, code, period, adjust):
        '''
        接口: stock_zh_a_minute
        目标地址: http://finance.sina.com.cn/realstock/company/sh600519/nc.shtml
        描述: 新浪财经获取股票或者指数的分时数据，目前可以获取 1, 5, 15, 30, 60 分钟的数据频率, 可以指定是否复权
        限量: 单次返回指定股票或指数的指定频率的所有历史分时行情数据
        输入参数
            名称	类型	必选	描述
            symbol	str	Y	symbol='sh000300'; 同日频率数据接口
            period	str	Y	period='1'; 获取 1, 5, 15, 30, 60 分钟的数据频率
            adjust	str	Y	adjust=""; 默认为空: 返回不复权的数据; qfq: 返回前复权后的数据; hfq: 返回后复权后的数据;
        输出参数
            名称	类型	默认显示	描述
            day	datetime	Y	-
            open	float	Y	-
            high	float	Y	-
            low	float	Y	-
            close	float	Y	-
            volume	float	Y	-
        '''
        stock_zh_a_minute_df = ak.stock_zh_a_minute(
            symbol=code,
            period=period,
            adjust=adjust
        )
        return stock_zh_a_minute_df

    def stock_ak_agu_lishihangqing_fenshiK_txcj(self, code, trade_date):
        '''
        腾讯财经
        接口: stock_zh_a_tick_tx
        目标地址: http://gu.qq.com/sz300494/gp/detail(示例)
        描述: A 股数据是从腾讯财经获取的数据, 历史数据按日频率更新
        限量: 单次返回具体某个 A 上市公司的近 2 年历史分笔行情数据
        P.S. 每个交易日 16:00 提供当日数据, 如遇到数据缺失，请使用 stock_zh_a_tick_163 接口，注意数据会有一定差异, 或者使用 stock_zh_a_tick_tx_js(code=”sz000001”) 来获取当日腾讯分笔数据
        输入参数-历史行情数据
            名称	类型	必选	描述
            symbol	str	Y	symbol="sh600000"
            trade_date	datetime	Y	trade_date="20191011"
        输出参数-历史行情数据
            名称	类型	默认显示	描述
            成交时间	time	Y	-
            成交价格	float	Y	-
            价格变动	float	Y	-
            成交量	float	Y	注意单位: 手
            成交额	float	Y	注意单位: 元
            性质	str	Y	买卖盘标记
        '''
        stock_zh_a_tick_tx_df = ak.stock_zh_a_tick_tx(code=code, trade_date=trade_date)
        return stock_zh_a_tick_tx_df

    def stock_ak_agu_lishihangqing_fenshiK_wycj(self, code, trade_date):
        '''
        网易财经
        接口: stock_zh_a_tick_163
        目标地址: http://quotes.money.163.com/trade/cjmx_000001.html#01b05(示例)
        描述: A 股数据是从网易财经获取的数据, 历史数据按日频率更新
        限量: 单次返回具体某个 A 上市公司的近 5 个交易日的历史分笔行情数据
        输入参数
            名称	类型	必选	描述
            symbol	str	Y	symbol="sh600000"
            trade_date	datetime	Y	trade_date="20200408"
        输出参数-历史行情数据
            名称	类型	默认显示	描述
            成交时间	time	Y	-
            成交价	float	Y	-
            价格变动	float	Y	-
            成交量(手)	float	Y	-
            成交额(元)	float	Y	-
            性质	str	Y	买卖盘标记
        '''
        stock_zh_a_tick_163_df = ak.stock_zh_a_tick_163(code=code, trade_date=trade_date)
        return stock_zh_a_tick_163_df


akshare_stock = AKShareStock()