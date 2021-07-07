#! /usr/bin/env python
# coding: utf-8
import os, sys
import numpy as np
import pandas as pd
import tushare as ts


class TUShareData(object):
    def __init__(self):
        pass

    def get_stock_lishi_hangqing_3years(self, code=None, start=None, end=None, ktype='D', retry_count=3, pause=0):
        '''
        获取个股历史交易数据（包括均线数据），可以通过参数设置获取日k线、周k线、月k线，以及5分钟、15分钟、30分钟和60分钟k线数据。本接口只能获取
        近3年的日线数据，适合搭配均线数据进行选股和分析，如果需要全部历史数据，请调用下一个接口get_h_data()。
        参数说明：
            code：股票代码，即6位数字代码，或者指数代码（sh=上证指数 sz=深圳成指 hs300=沪深300指数 sz50=上证50 zxb=中小板 cyb=创业板）
            start：开始日期，格式YYYY-MM-DD
            end：结束日期，格式YYYY-MM-DD
            ktype：数据类型，D=日k线 W=周 M=月 5=5分钟 15=15分钟 30=30分钟 60=60分钟，默认为D
            retry_count：当网络异常后重试次数，默认为3
            pause:重试时停顿秒数，默认为0
        返回值说明：
            date：日期
            open：开盘价
            high：最高价
            close：收盘价
            low：最低价
            volume：成交量
            price_change：价格变动
            p_change：涨跌幅
            ma5：5日均价
            ma10：10日均价
            ma20:20日均价
            v_ma5:5日均量
            v_ma10:10日均量
            v_ma20:20日均量
            turnover:换手率[注：指数无此项]
        例子:
        ts.get_hist_data('600848', ktype='W') #获取周k线数据
        ts.get_hist_data('600848', ktype='M') #获取月k线数据
        ts.get_hist_data('600848', ktype='5') #获取5分钟k线数据
        ts.get_hist_data('600848', ktype='15') #获取15分钟k线数据
        ts.get_hist_data('600848', ktype='30') #获取30分钟k线数据
        ts.get_hist_data('600848', ktype='60') #获取60分钟k线数据
        ts.get_hist_data('sh'）#获取上证指数k线数据，其它参数与个股一致，下同
        ts.get_hist_data('sz'）#获取深圳成指k线数据
        ts.get_hist_data('hs300'）#获取沪深300指数k线数据
        ts.get_hist_data('sz50'）#获取上证50指数k线数据
        ts.get_hist_data('zxb'）#获取中小板指数k线数据
        ts.get_hist_data('cyb'）#获取创业板指数k线数据
        '''
        data = ts.get_hist_data(code=code)
        return data

    def get_stock_lishi_hangqing(self, code, start=None, end=None, autype='qfq',
               index=False, retry_count=3, pause=0.001, drop_factor=True):
        '''
        获取历史复权数据
        Parameters
            code:string
                股票代码 e.g. 600848
            start:string
                开始日期 format：YYYY-MM-DD 为空时取当前日期
            end:string
                结束日期 format：YYYY-MM-DD 为空时取去年今日
            autype:string
                复权类型，qfq-前复权 hfq-后复权 None-不复权，默认为qfq
            retry_count : int, 默认 3
                如遇网络等问题重复执行的次数
            pause : int, 默认 0
                重复请求数据过程中暂停的秒数，防止请求间隔时间太短出现的问题
            drop_factor : bool, 默认 True
                是否移除复权因子，在分析过程中可能复权因子意义不大，但是如需要先储存到数据库之后再分析的话，有该项目会更加灵活
        return
            DataFrame
                date 交易日期 (index)
                open 开盘价
                high  最高价
                close 收盘价
                low 最低价
                volume 成交量
                amount 成交金额
        例子:
            ts.get_h_data('002337') #前复权
            ts.get_h_data('002337', autype='hfq') #后复权
            ts.get_h_data('002337', autype=None) #不复权
            ts.get_h_data('002337', start='2015-01-01', end='2015-03-16') #两个日期之间的前复权数据
            ts.get_h_data('399106', index=True) #深圳综合指数
        '''
        data = ts.get_h_data(
            code=code,
            start=start,
            end=end,
            autype=autype,
            index=index,
            retry_count=retry_count,
            pause=pause,
            drop_factor=drop_factor
        )
        return data

    def get_stock_lishi_fenbi(self, code=None, date=None, retry_count=3, pause=0.001, src='sn'):
        '''
        获取个股以往交易历史的分笔数据明细，通过分析分笔数据，可以大致判断资金的进出情况。在使用过程中，对于获取股票某一阶段的历史分笔数据，
        需要通过参入交易日参数并append到一个DataFrame或者直接append到本地同一个文件里。历史分笔接口只能获取当前交易日之前的数据，
        当日分笔历史数据请调用get_today_ticks()接口或者在当日18点后通过本接口获取。
        参数说明：
            code：股票代码，即6位数字代码
            date：日期，格式YYYY-MM-DD
            retry_count : int, 默认3,如遇网络等问题重复执行的次数
            pause : int, 默认 0,重复请求数据过程中暂停的秒数，防止请求间隔时间太短出现的问题
        调用方法：
            import tushare as ts
            df = ts.get_tick_data('600848',date='2018-12-12',src='tt')
            df.head(10)
        返回值说明：
            time：时间
            price：成交价格
            change：价格变动
            volume：成交手
            amount：成交金额(元)
            type：买卖类型【买盘、卖盘、中性盘】
        '''
        data = ts.get_tick_data(code=code, date=date, retry_count=retry_count, pause=pause, src=src)
        return data

    def get_stock_shishi_fenbi(self, symbols):
        '''
        获取实时分笔数据，可以实时取得股票当前报价和成交信息，其中一种场景是，写一个python定时程序来调用本接口（可两三秒执行一次，性能与行情软件基本一致），
        然后通过DataFrame的矩阵计算实现交易监控，可实时监测交易量和价格的变化。
        参数说明：
            symbols：6位数字股票代码，或者指数代码（sh=上证指数 sz=深圳成指 hs300=沪深300指数 sz50=上证50 zxb=中小板 cyb=创业板）
            可输入的类型：str、list、set或者pandas的Series对象
        调用方法：
            import tushare as ts
            df = ts.get_realtime_quotes('000581') #Single stock symbol
            df[['code','name','price','bid','ask','volume','amount','time']]
        结果显示：
               code    name     price  bid    ask    volume   amount        time
            0  000581  威孚高科  31.15  31.14  31.15  8183020  253494991.16  11:30:36
        返回值说明：
            0：name，股票名字
            1：open，今日开盘价
            2：pre_close，昨日收盘价
            3：price，当前价格
            4：high，今日最高价
            5：low，今日最低价
            6：bid，竞买价，即“买一”报价
            7：ask，竞卖价，即“卖一”报价
            8：volume，成交量 maybe you need do volume/100
            9：amount，成交金额（元 CNY）
            10：b1_v，委买一（笔数 bid volume）
            11：b1_p，委买一（价格 bid price）
            12：b2_v，“买二”
            13：b2_p，“买二”
            14：b3_v，“买三”
            15：b3_p，“买三”
            16：b4_v，“买四”
            17：b4_p，“买四”
            18：b5_v，“买五”
            19：b5_p，“买五”
            20：a1_v，委卖一（笔数 ask volume）
            21：a1_p，委卖一（价格 ask price）
            ...
            30：date，日期；
            31：time，时间；
        请求多个股票方法（一次最好不要超过30个）：
            #symbols from a list
            ts.get_realtime_quotes(['600848','000980','000981'])
            #from a Series
            ts.get_realtime_quotes(df['code'].tail(10))  #一次获取10个股票的实时分笔数据
        获取实时指数：
            #上证指数
            ts.get_realtime_quotes('sh')
            #上证指数 深圳成指 沪深300指数 上证50 中小板 创业板
            ts.get_realtime_quotes(['sh','sz','hs300','sz50','zxb','cyb'])
            #或者混搭
            ts.get_realtime_quotes(['sh','600848'])
        '''
        data = ts.get_realtime_quotes(symbols=symbols)
        return data

    def get_stock_dangri_fenbi(self, code=None, retry_count=3, pause=0.001):
        '''
        获取当前交易日（交易进行中使用）已经产生的分笔明细数据。
        参数说明：
            code：股票代码，即6位数字代码
            retry_count : int, 默认3,如遇网络等问题重复执行的次数
            pause : int, 默认 0,重复请求数据过程中暂停的秒数，防止请求间隔时间太短出现的问题
        调用方法：
            import tushare as ts
            df = ts.get_today_ticks('601333')
            df.head(10)
        返回值说明：
            time：时间
            price：当前价格
            pchange:涨跌幅
            change：价格变动
            volume：成交手
            amount：成交金额(元)
            type：买卖类型【买盘、卖盘、中性盘】
        '''
        data = ts.get_today_ticks(code=code, retry_count=retry_count, pause=pause)
        return data

    def get_stock_shishi_dapanzhishuhangqing(self):
        '''
        获取大盘指数实时行情列表，以表格的形式展示大盘指数实时行情。
        调用方法：
            import tushare as ts
            df = ts.get_index()
        返回值说明：
            code:指数代码
            name:指数名称
            change:涨跌幅
            open:开盘点位
            preclose:昨日收盘点位
            close:收盘点位
            high:最高点位
            low:最低点位
            volume:成交量(手)
            amount:成交金额（亿元）
        '''
        data = ts.get_index()
        return data

    def get_stock_dadanjiaoyi(self, code=None, date=None, vol=400, retry_count=3, pause=0.001):
        '''
        获取大单交易数据，默认为大于等于400手，数据来源于新浪财经。
        参数说明：
            code：股票代码，即6位数字代码
            date:日期，格式YYYY-MM-DD
            vol:手数，默认为400手，输入数值型参数
            retry_count : int, 默认3,如遇网络等问题重复执行的次数
            pause : int, 默认 0,重复请求数据过程中暂停的秒数，防止请求间隔时间太短出现的问题
        返回值说明：
            code：代码
            name：名称
            time：时间
            price：当前价格
            volume：成交手
            preprice ：上一笔价格
            type：买卖类型【买盘、卖盘、中性盘】
        '''
        data = ts.get_sina_dd(code=code, date=date, vol=vol, retry_count=retry_count, pause=pause)
        return data

    def get_stock_fenpeiyuan(self, year=2017, top=25, retry_count=3, pause=0.001):
        '''
        分配预案
        每到季报、年报公布的时段，就经常会有上市公司利润分配预案发布，而一些高送转高分红的股票往往会成为市场炒作的热点。
        及时获取和统计高送转预案的股票是参与热点炒作的关键，TuShare提供了简洁的接口，能返回股票的送转和分红预案情况。
        参数说明：
            year : 预案公布的年份，默认为2014
            top :取最新n条数据，默认取最近公布的25条
            retry_count：当网络异常后重试次数，默认为3
            pause:重试时停顿秒数，默认为0
        返回值说明：
            code:股票代码
            name:股票名称
            year:分配年份
            report_date:公布日期
            divi:分红金额（每10股）
            shares:转增和送股数（每10股）
        '''
        data = ts.profit_data(year=year, top=top, retry_count=retry_count, pause=pause)
        return data

    def get_stock_yejibaogao(self, year, quarter):
        '''
        业绩预告
            按年度、季度获取业绩预告数据，接口提供从1998年以后每年的业绩预告数据，需指定年度、季度两个参数。数据在获取的过程中，
            会打印进度信息(下同)。
        参数说明：
            year:int 年度 e.g:2014
            quarter:int 季度 :1、2、3、4，只能输入这4个季度
        结果返回的数据属性说明如下：
            code,代码
            name,名称
            type,业绩变动类型【预增、预亏等】
            report_date,发布日期
            pre_eps,上年同期每股收益
            range,业绩变动范围
        '''
        data = ts.forecast_data(year=year, quarter=quarter)
        return data

    def get_stock_xianshoujiejin(self, year=None, month=None, retry_count=3, pause=0.001):
        '''
        限售股解禁
            以月的形式返回限售股解禁情况，通过了解解禁股本的大小，判断股票上行的压力。可通过设定年份和月份参数获取不同时段的数据。
        参数说明：
            year:年份,默认为当前年
            month:解禁月份，默认为当前月
            retry_count：当网络异常后重试次数，默认为3
            pause:重试时停顿秒数，默认为0
        返回值说明：
            code：股票代码
            name：股票名称
            date:解禁日期
            count:解禁数量（万股）
            ratio:占总盘比率
        '''
        data = ts.xsg_data(year=year, month=month, retry_count=retry_count, pause=retry_count)
        return data

    def get_stock_jijinchigu(self, year, quarter, retry_count=3, pause=0.001):
        '''
        基金持股
            获取每个季度基金持有上市公司股票的数据。
        参数说明：
            year:年份,默认为当前年
            quarter:季度（只能输入1，2，3，4这个四个数字）
            retry_count：当网络异常后重试次数，默认为3
            pause:重试时停顿秒数，默认为0
        返回值说明：
            code：股票代码
            name：股票名称
            date:报告日期
            nums:基金家数
            nlast:与上期相比（增加或减少了）
            count:基金持股数（万股）
            clast:与上期相比
            amount:基金持股市值
            ratio:占流通盘比率
        '''
        data = ts.fund_holdings(year=year, quarter=quarter, retry_count=retry_count, pause=pause)
        return data

    def get_stock_xingushuju(self, retry_count=3, pause=0.001):
        '''
        新股数据
            获取IPO发行和上市的时间列表，包括发行数量、网上发行数量、发行价格已经中签率信息等。
        参数说明：
            retry_count：当网络异常后重试次数，默认为3
            pause:重试时停顿秒数，默认为0
        返回值说明：
            code：股票代码
            name：股票名称
            ipo_date:上网发行日期
            issue_date:上市日期
            amount:发行数量(万股)
            markets:上网发行数量(万股)
            price:发行价格(元)
            pe:发行市盈率
            limit:个人申购上限(万股)
            funds：募集资金(亿元)
            ballot:网上中签率(%)
        '''
        data = ts.new_stocks(retry_count=retry_count, pause=pause)
        return data

    def get_stock_sh_rongzirongquan(self, start=None, end=None, retry_count=3, pause=0.001):
        '''
        融资融券（沪市）请转移到Tushare Pro 融资融券新接口
            沪市的融资融券数据从上海证券交易所网站直接获取，提供了有记录以来的全部汇总和明细数据。根据上交所网站提示：数据根据券商申报的数据汇总，由券商保证数据的真实、完整、准确。
            本日融资融券余额＝本日融资余额＋本日融券余量金额
            本日融资余额＝前日融资余额＋本日融资买入额－本日融资偿还额；
            本日融资偿还额＝本日直接还款额＋本日卖券还款额＋本日融资强制平仓额＋本日融资正权益调整－本日融资负权益调整；
            本日融券余量=前日融券余量+本日融券卖出数量-本日融券偿还量；
            本日融券偿还量＝本日买券还券量＋本日直接还券量＋本日融券强制平仓量＋本日融券正权益调整－本日融券负权益调整－本日余券应划转量；
            融券单位：股（标的证券为股票）/份（标的证券为基金）/手（标的证券为债券）。
            明细信息中仅包含当前融资融券标的证券的相关数据，汇总信息中包含被调出标的证券范围的证券的余额余量相关数据。
        沪市融资融券汇总数据
        参数说明：
            start:开始日期 format：YYYY-MM-DD 为空时取去年今日
            end:结束日期 format：YYYY-MM-DD 为空时取当前日期
            retry_count：当网络异常后重试次数，默认为3
            pause:重试时停顿秒数，默认为0
        返回值说明：
            opDate:信用交易日期
            rzye:本日融资余额(元)
            rzmre: 本日融资买入额(元)
            rqyl: 本日融券余量
            rqylje: 本日融券余量金额(元)
            rqmcl: 本日融券卖出量
            rzrqjyzl:本日融资融券余额(元)
        '''
        data = ts.sh_margins(start=start, end=end, retry_count=retry_count, pause=pause)
        return data

    def get_stock_sh_rongzirongquan_detail(self, date='', symbol='', start='', end='', retry_count=3, pause=0.001):
        '''
        沪市融资融券明细数据
        参数说明：
            date:日期 format：YYYY-MM-DD 默认为空’‘,数据返回最近交易日明细数据
            symbol：标的代码，6位数字e.g.600848，默认为空’‘
            start:开始日期 format：YYYY-MM-DD 默认为空’‘
            end:结束日期 format：YYYY-MM-DD 默认为空’‘
            retry_count：当网络异常后重试次数，默认为3
            pause:重试时停顿秒数，默认为0
        返回值说明：
            opDate:信用交易日期
            stockCode:标的证券代码
            securityAbbr:标的证券简称
            rzye:本日融资余额(元)
            rzmre: 本日融资买入额(元)
            rzche:本日融资偿还额(元)
            rqyl: 本日融券余量
            rqmcl: 本日融券卖出量
            rqchl: 本日融券偿还量
        注：
            #如果不设symbol参数或者开始和结束日期时段设置过长，数据获取可能会比较慢，建议分段分步获取，比如一年为一个周期
        '''
        data = ts.sh_margin_details(date=date, symbol=symbol, start=start, end=end, retry_count=retry_count, pause=pause)
        return data

    def get_stock_sz_rongzirongquan(self, start=None, end=None, retry_count=3, pause=0.001):
        '''
        融资融券（深市）请转移到Tushare Pro 融资融券新接口
            深市的融资融券数据从深圳证券交易所网站直接获取，提供了有记录以来的全部汇总和明细数据。在深交所的网站上，对于融资融券的说明如下：
        说明：
            本报表基于证券公司报送的融资融券余额数据汇总生成，其中：
            本日融资余额(元)=前日融资余额＋本日融资买入-本日融资偿还额
            本日融券余量(股)=前日融券余量＋本日融券卖出量-本日融券买入量-本日现券偿还量
            本日融券余额(元)=本日融券余量×本日收盘价
            本日融资融券余额(元)=本日融资余额＋本日融券余额；
            2014年9月22日起，“融资融券交易总量”数据包含调出标的证券名单的证券的融资融券余额。
        深市融资融券汇总数据
        参数说明：
            start:开始日期 format：YYYY-MM-DD 为空时取去年今日
            end:结束日期 format：YYYY-MM-DD 为空时取当前日期
            retry_count：当网络异常后重试次数，默认为3
            pause:重试时停顿秒数，默认为0
        返回值说明：
            opDate:信用交易日期(index)
            rzmre: 融资买入额(元)
            rzye:融资余额(元)
            rqmcl: 融券卖出量
            rqyl: 融券余量
            rqye: 融券余量(元)
            rzrqye:融资融券余额(元)
        '''
        data = ts.sz_margins(start=start, end=end, retry_count=retry_count, pause=pause)
        return data

    def get_stock_sz_rongzirongquan_detail(self, date='', retry_count=3, pause=0.001):
        '''
        深市融资融券明细数据
        参数说明：
            date:日期 format：YYYY-MM-DD 默认为空’‘,数据返回最近交易日明细数据
            retry_count：当网络异常后重试次数，默认为3
            pause:重试时停顿秒数，默认为0
        返回值说明：
            stockCode:标的证券代码
            securityAbbr:标的证券简称
            rzmre: 融资买入额(元)
            rzye:融资余额(元)
            rqmcl: 融券卖出量
            rqyl: 融券余量
            rqye: 融券余量(元)
            rzrqye:融资融券余额(元)
            opDate:信用交易日期
        注:
            #深市融资融券明细一次只能获取一天的明细数据，如果不输入参数，则为最近一个交易日的明细数据
        '''
        data = ts.sz_margin_details(date=date, retry_count=retry_count, pause=pause)
        return data

    def get_stock_fenlei_hangye(self, standard='sina'):
        '''
        行业分类
            在现实交易中，经常会按行业统计股票的涨跌幅或资金进出，本接口按照sina财经对沪深股票进行的行业分类，返回所有股票所属行业的信息。
            考虑到是一次性在线获取数据，调用接口时会有一定的延时，请在数据返回后自行将数据进行及时存储。sina财经提供的行业分类信息大致
            如下图所示：
        参数:
            standard:
                'sina' -- 新浪行业
                'sw'   -- 申万 行业
        返回值说明：
            code：股票代码
            name：股票名称
            c_name：行业名称
        '''
        data = ts.get_industry_classified(standard=standard)
        return data

    def get_stock_fenlei_gainian(self):
        '''
        概念分类
            返回股票概念的分类数据，现实的二级市场交易中，经常会以”概念”来炒作，在数据分析过程中，可根据概念分类监测资金等信息的变动情况。
            本接口是一次性在线获取数据，调用接口时会有一定的延时，请在数据返回后自行将数据进行及时存储。
            sina财经提供的概念分类信息大致如下图所示：
        返回值说明：
            code：股票代码
            name：股票名称
            c_name：概念名称
        '''
        data = ts.get_concept_classified()
        return data

    def get_stock_fenlei_diyu(self):
        '''
        地域分类
            按地域对股票进行分类，即查找出哪些股票属于哪个省份。
        参数说明：
            file_path:文件路径，默认为None即由TuShare提供，可以设定自己的股票文件路径。
        返回值说明：
            code：股票代码
            name：股票名称
            area：地域名称
        '''
        data = ts.get_area_classified()
        return data

    def get_stock_fenlei_zhongxiaoban(self):
        '''
        中小板分类
            获取中小板股票数据，即查找所有002开头的股票
        参数说明：
            file_path:文件路径，默认为None即由TuShare提供，可以设定自己的股票文件路径。
        返回值说明：
            code：股票代码
            name：股票名称
        '''
        data = ts.get_sme_classified()
        return data

    def get_stock_fenlei_chuangyeban(self):
        '''
        创业板分类
            获取创业板股票数据，即查找所有300开头的股票
        参数说明：
            file_path:文件路径，默认为None即由TuShare提供，可以设定自己的股票文件路径。
        返回值说明：
            code：股票代码
            name：股票名称
        '''
        data = ts.get_gem_classified()
        return data

    def get_stock_fenlei_fengxianjingshi(self):
        '''
        风险警示板分类
            获取风险警示板股票数据，即查找所有st股票
        参数说明：
            file_path:文件路径，默认为None即由TuShare提供，可以设定自己的股票文件路径。
        返回值说明：
            code：股票代码
            name：股票名称
        '''
        data = ts.get_st_classified()
        return data

    def get_stock_hushen300_chengfenquanzhong(self):
        '''
        沪深300成份及权重
            获取沪深300当前成份股及所占权重
        返回值说明：
            code :股票代码
            name :股票名称
            date :日期
            weight:权重
        '''
        data = ts.get_hs300s()
        return data

    def get_stock_shangzheng50_chengfengu(self):
        '''
        上证50成份股
            获取上证50成份股
        返回值说明：
            code：股票代码
            name：股票名称
        '''
        data = ts.get_sz50s()
        return data

    def get_stock_zhongzheng500_chengfengu(self):
        '''
        中证500成份股
            获取中证500成份股
        返回值说明：
            code：股票代码
            name：股票名称
        '''
        data = ts.get_zz500s()
        return data

    def get_stock_zhongzhishangshi(self):
        '''
        终止上市股票列表
            获取已经被终止上市的股票列表，数据从上交所获取，目前只有在上海证券交易所交易被终止的股票。
        返回值说明：
            code：股票代码
            name：股票名称
            oDate:上市日期
            tDate:终止上市日期
        '''
        data = ts.get_terminated()
        return data

    def get_stock_zhantingshangshi(self):
        '''
        暂停上市股票列表
            获取被暂停上市的股票列表，数据从上交所获取，目前只有在上海证券交易所交易被终止的股票。
        返回值说明：
            code：股票代码
            name：股票名称
            oDate:上市日期
            tDate:暂停上市日期
        '''
        data = ts.get_suspended()
        return data

    def get_stock_gupiaoliebiao(self, date=None):
        '''
        股票列表 请转移到Tushare Pro 新接口
        参数说明：
            date:日期YYYY-MM-DD，默认为上一个交易日，目前只能提供2016-08-09之后的历史数据
        获取沪深上市公司基本情况。属性包括：
            code,代码
            name,名称
            industry,所属行业
            area,地区
            pe,市盈率
            outstanding,流通股本(亿)
            totals,总股本(亿)
            totalAssets,总资产(万)
            liquidAssets,流动资产
            fixedAssets,固定资产
            reserved,公积金
            reservedPerShare,每股公积金
            esp,每股收益
            bvps,每股净资
            pb,市净率
            timeToMarket,上市日期
            undp,未分利润
            perundp, 每股未分配
            rev,收入同比(%)
            profit,利润同比(%)
            gpr,毛利率(%)
            npr,净利润率(%)
            holders,股东人数
        '''
        data = ts.get_stock_basics(date=date)
        return data

    def get_stock_yeji(self, year, quarter):
        '''
        业绩报告（主表） 请转移到Tushare Pro 新接口
        按年度、季度获取业绩报表数据。数据获取需要一定的时间，网速取决于您的网速，请耐心等待。
        参数说明：
            year:int 年度 e.g:2014
            quarter:int 季度 :1、2、3、4，只能输入这4个季度
            说明：由于是从网站获取的数据，需要一页页抓取，速度取决于您当前网络速度
        Return
        DataFrame
            code,代码
            name,名称
            eps,每股收益
            eps_yoy,每股收益同比(%)
            bvps,每股净资产
            roe,净资产收益率(%)
            epcf,每股现金流量(元)
            net_profits,净利润(万元)
            profits_yoy,净利润同比(%)
            distrib,分配方案
            report_date,发布日期
        '''
        data = ts.get_report_data(year=year, quarter=quarter)
        return data

    def get_stock_yingli(self, year, quarter):
        '''
        盈利能力
        按年度、季度获取盈利能力数据.
        Parameters
            year:int 年度 e.g:2014
            quarter:int 季度 :1、2、3、4，只能输入这4个季度
               说明：由于是从网站获取的数据，需要一页页抓取，速度取决于您当前网络速度
        Return
            DataFrame
                code,代码
                name,名称
                roe,净资产收益率(%)
                net_profit_ratio,净利率(%)
                gross_profit_rate,毛利率(%)
                net_profits,净利润(万元)
                eps,每股收益
                business_income,营业收入(百万元)
                bips,每股主营业务收入(元)
        '''
        data = ts.get_profit_data(year=year, quarter=quarter)
        return data

    def get_stock_yunying(self, year, quarter):
        '''
        营运能力
            按年度、季度获取营运能力数据，
        Parameters
        year:int 年度 e.g:2014
        quarter:int 季度 :1、2、3、4，只能输入这4个季度
           说明：由于是从网站获取的数据，需要一页页抓取，速度取决于您当前网络速度
        Return
            DataFrame
                code,代码
                name,名称
                arturnover,应收账款周转率(次)
                arturndays,应收账款周转天数(天)
                inventory_turnover,存货周转率(次)
                inventory_days,存货周转天数(天)
                currentasset_turnover,流动资产周转率(次)
                currentasset_days,流动资产周转天数(天)
        '''
        data = ts.get_operation_data(year=year, quarter=quarter)
        return data

    def get_stock_chengzhang(self, year, quarter):
        '''
        成长能力
            按年度、季度获取成长能力数据，
        Parameters
            year:int 年度 e.g:2014
            quarter:int 季度 :1、2、3、4，只能输入这4个季度
               说明：由于是从网站获取的数据，需要一页页抓取，速度取决于您当前网络速度
        Return
            DataFrame
                code,代码
                name,名称
                mbrg,主营业务收入增长率(%)
                nprg,净利润增长率(%)
                nav,净资产增长率
                targ,总资产增长率
                epsg,每股收益增长率
                seg,股东权益增长率
        '''
        data = ts.get_growth_data(year=year, quarter=quarter)
        return data

    def get_stock_changzai(self, year, quarter):
        '''
        偿债能力
            按年度、季度获取偿债能力数据，
        Parameters
            year:int 年度 e.g:2014
            quarter:int 季度 :1、2、3、4，只能输入这4个季度
               说明：由于是从网站获取的数据，需要一页页抓取，速度取决于您当前网络速度
        Return
            DataFrame
                code,代码
                name,名称
                currentratio,流动比率
                quickratio,速动比率
                cashratio,现金比率
                icratio,利息支付倍数
                sheqratio,股东权益比率
                adratio,股东权益增长率
        '''
        data = ts.get_debtpaying_data(year=year, quarter=quarter)
        return data

    def get_stock_xianjinliuliang(self, year, quarter):
        '''
        现金流量
            按年度、季度获取现金流量数据，
        Parameters
            year:int 年度 e.g:2014
            quarter:int 季度 :1、2、3、4，只能输入这4个季度
               说明：由于是从网站获取的数据，需要一页页抓取，速度取决于您当前网络速度
        Return
            DataFrame
                code,代码
                name,名称
                cf_sales,经营现金净流量对销售收入比率
                rateofreturn,资产的经营现金流量回报率
                cf_nm,经营现金净流量与净利润的比率
                cf_liabilities,经营现金净流量对负债比率
                cashflowratio,现金流量比率
        '''
        data = ts.get_cashflow_data(year=year, quarter=quarter)
        return data

    def get_stock_meirilonghubang(self, date = None, retry_count=3, pause=0.001):
        '''
        每日龙虎榜列表 请转移到Tushare Pro 龙虎榜新接口，有全部历史数据和增量。
            按日期获取历史当日上榜的个股数据，如果一个股票有多个上榜原因，则会出现该股票多条数据。
        参数说明：
            date：日期，格式YYYY-MM-DD
            retry_count：当网络异常后重试次数，默认为3
            pause:重试时停顿秒数，默认为0
        返回值说明：
            code：代码
            name:名称
            pchange:当日涨跌幅
            amount：龙虎榜成交额(万)
            buy：买入额(万)
            bratio：买入占总成交比例
            sell：卖出额(万)
            sratio：卖出占总成交比例
            reason：上榜原因
            date：日期
        '''
        data = ts.top_list(date = date, retry_count=retry_count, pause=pause)
        return data

    def get_stock_gegushangbangtongji(self, days= 5, retry_count= 3, pause= 0.001):
        '''
        个股上榜统计
            获取近5、10、30、60日个股上榜统计数据,包括上榜次数、累积购买额、累积卖出额、净额、买入席位数和卖出席位数。
            参数说明：
                days：统计周期5、10、30和60日，默认为5日
                retry_count：当网络异常后重试次数，默认为3
                pause:重试时停顿秒数，默认为0
            返回值说明：
                code：代码
                name:名称
                count：上榜次数
                bamount：累积购买额(万)
                samount：累积卖出额(万)
                net：净额(万)
                bcount：买入席位数
                scount：卖出席位数
        '''
        data = ts.cap_tops(days=days, retry_count=retry_count, pause=pause)
        return data

    def get_stock_yingyebushangbangtongji(self, days= 5, retry_count= 3, pause= 0.001):
        '''
        营业部上榜统计
            获取营业部近5、10、30、60日上榜次数、累积买卖等情况。
        参数说明：
            days：统计周期5、10、30和60日，默认为5日
            retry_count：当网络异常后重试次数，默认为3
            pause:重试时停顿秒数，默认为0
        返回值说明：
            broker：营业部名称
            count：上榜次数
            bamount：累积购买额(万)
            bcount：买入席位数
            samount：累积卖出额(万)
            scount：卖出席位数
            top3：买入前三股票
        '''
        data = ts.broker_tops(days=days, retry_count=retry_count, pause=pause)
        return data

    def get_stock_jigouxiweizhuizong(self, days= 5, retry_count= 3, pause= 0.001):
        '''
        机构席位追踪
            获取机构近5、10、30、60日累积买卖次数和金额等情况。
        参数说明：
            days：统计周期5、10、30和60日，默认为5日
            retry_count：当网络异常后重试次数，默认为3
            pause:重试时停顿秒数，默认为0
        返回值说明：
            code:代码
            name:名称
            bamount:累积买入额(万)
            bcount:买入次数
            samount:累积卖出额(万)
            scount:卖出次数
            net:净额(万)
        '''
        data = ts.inst_tops(days=days, retry_count=retry_count, pause=pause)
        return data

    def get_stock_jigouchengjiaomingxi(self, retry_count= 3, pause= 0.001):
        '''
        机构成交明细
            获取最近一个交易日机构席位成交明细统计数据
        参数说明：
            retry_count：当网络异常后重试次数，默认为3
            pause:重试时停顿秒数，默认为0
        返回值说明：
            code:代码
            name:名称
            date:交易日期
            bamount:机构席位买入额(万)
            samount:机构席位卖出额(万)
            type:类型
        '''
        data = ts.inst_detail(retry_count=retry_count, pause=pause)
        return data
