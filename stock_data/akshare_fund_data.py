#! /usr/bin/env python
# coding: utf-8
import os, sys
import numpy as np
import akshare as ak


class AKShareFund(object):
    def __init__(self):
        pass

    def fund_simu_congyerenyuanxinxi(self):
        '''
        中国证券投资基金业协会
        会员信息
        会员机构综合查询
        接口: amac_member_info
        目标地址: http://gs.amac.org.cn/amac-infodisc/res/pof/member/index.html
        描述: 获取中国证券投资基金业协会-信息公示-会员信息-会员机构综合查询
        限量: 单次返回当前时刻所有历史数据
        输入参数
            名称	类型	必选	描述
            -	-	-	-
        输出参数
            名称	类型	默认显示	描述
            机构（会员）名称	str	Y	-
            会员代表	str	Y	-
            会员类型	str	Y	-
            会员编号	str	Y	-
            入会时间	datetime.date	Y	-
            机构类型	str	Y	-
            是否星标	str	Y	-
        '''
        data = ak.amac_member_info()
        return data

    def fund_simu_jijincongyerenyuanzigezhucexinxi(self):
        '''
        基金从业人员资格注册信息
        接口: amac_person_org_list
        目标地址: http://gs.amac.org.cn/amac-infodisc/res/pof/person/personOrgList.html
        描述: 获取中国证券投资基金业协会-信息公示-从业人员信息-基金从业人员资格注册信息
        限量: 单次返回当前时刻所有历史数据
        输入参数
            名称	类型	必选	描述
            -	-	-	-
        输出参数
            名称	类型	默认显示	描述
            机构名称	str	Y	-
            员工人数	str	Y	-
            基金从业资格	str	Y	-
            基金销售业务资格	str	Y	-
            基金经理	datetime.date	Y	-
            投资经理	str	Y	-
        '''
        df = ak.amac_person_org_list()
        return df

    def fund_simu_jijinguanlirenzonghechaxun(self):
        '''
        私募基金管理人综合查询
        接口: amac_manager_info
        目标地址: http://gs.amac.org.cn/amac-infodisc/res/pof/manager/index.html
        描述: 获取中国证券投资基金业协会-信息公示-私募基金管理人公示-私募基金管理人综合查询
        限量: 单次返回当前时刻所有历史数据
        输入参数
            名称	类型	必选	描述
            -	-	-	-
        输出参数
            名称	类型	默认显示	描述
            私募基金管理人名称	str	Y	-
            法定代表人/执行事务合伙人(委派代表)姓名	float	Y	-
            机构类型	float	Y	-
            注册地	float	Y	-
            登记编号	float	Y	-
            成立时间	float	Y	-
            登记时间	float	Y	-
        '''
        df = ak.amac_manager_info()
        return df

    def fund_simu_jijinguanlirenfenleigongshi(self):
        '''
        私募基金管理人分类公示
        接口: amac_manager_classify_info
        目标地址: http://gs.amac.org.cn/amac-infodisc/res/pof/manager/managerList.html
        描述: 获取中国证券投资基金业协会-信息公示-私募基金管理人公示-私募基金管理人分类公示
        限量: 单次返回当前时刻所有历史数据
        输入参数
            名称	类型	必选	描述
            -	-	-	-
        输出参数
            名称	类型	默认显示	描述
            私募基金管理人名称	str	Y	-
            法定代表人/执行事务合伙人(委派代表)姓名	float	Y	-
            机构类型	float	Y	-
            注册地	float	Y	-
            登记编号	float	Y	-
            成立时间	float	Y	-
            登记时间	float	Y	-
        '''
        df = ak.amac_manager_classify_info()
        return df

    def fund_simu_zhengquangongsisimujijinzigongsiguanlirenxinxigongshi(self):
        '''
        证券公司私募基金子公司管理人信息公示
        接口: amac_member_sub_info
        目标地址: http://gs.amac.org.cn/amac-infodisc/res/pof/member/index.html?primaryInvestType=private
        描述: 获取中国证券投资基金业协会-信息公示-私募基金管理人公示-证券公司私募基金子公司管理人信息公示
        限量: 单次返回当前时刻所有历史数据
        输入参数
            名称	类型	必选	描述
            -	-	-	-
        输出参数
            名称	类型	默认显示	描述
            机构（会员）名称	str	Y	-
            会员代表	float	Y	-
            会员类型	float	Y	-
            会员编号	float	Y	-
            入会时间	float	Y	-
            公司类型	float	Y	-
        '''
        df = ak.amac_member_sub_info()
        return df

    def fund_simu_jijinguanlirenjijinchanpin(self):
        '''
        募基金管理人基金产品
        接口: amac_fund_info
        目标地址: http://gs.amac.org.cn/amac-infodisc/res/pof/fund/index.html
        描述: 获取中国证券投资基金业协会-信息公示-基金产品公示-私募基金管理人基金产品
        限量: 单次返回当前时刻所有历史数据
        输入参数
            名称	类型	必选	描述
            -	-	-	-
        输出参数
            名称	类型	默认显示	描述
            基金名称	str	Y	-
            私募基金管理人名称	float	Y	-
            私募基金管理人类型	float	Y	-
            运行状态	float	Y	-
            备案时间	float	Y	-
            建立时间	float	Y	-
            托管人名称	float	Y	-
        '''
        df = ak.amac_fund_info()
        return df

    def fund_simu_zhengquangongsijiheziguanchanpingongshi(self):
        '''
        接口: amac_securities_info
        目标地址: http://gs.amac.org.cn/amac-infodisc/res/pof/securities/index.html
        描述: 获取中国证券投资基金业协会-信息公示-基金产品公示-证券公司集合资管产品公示
        限量: 单次返回当前时刻所有历史数据
        输入参数
            名称	类型	必选	描述
            -	-	-	-
        输出参数
            名称	类型	默认显示	描述
            产品名称	str	Y	-
            产品编码	float	Y	-
            管理人名称	float	Y	-
            成立日期	float	Y	-
            到期时间	float	Y	-
            投资类型	float	Y	-
            是否分级	float	Y	-
            托管人名称	float	Y	-
            备案日期	float	Y	-
            运作状态	float	Y	-
        '''
        df = ak.amac_securities_info()
        return df

    def fund_simu_zhengquangongsizhitoujijin(self):
        '''
        证券公司直投基金
        接口: amac_aoin_info
        目标地址: http://gs.amac.org.cn/amac-infodisc/res/aoin/product/index.html
        描述: 获取中国证券投资基金业协会-信息公示-基金产品公示-证券公司直投基金
        限量: 单次返回当前时刻所有历史数据
        输入参数
            名称	类型	必选	描述
            -	-	-	-
        输出参数
            名称	类型	默认显示	描述
            产品编码	str	Y	-
            产品名称	float	Y	-
            直投子公司	float	Y	-
            管理机构	float	Y	-
            设立日期	float	Y	-
        '''
        df = ak.amac_aoin_info()
        return df

    def fund_simu_zhengquangongsisimutouzijijin(self):
        '''
        证券公司私募投资基金
        接口: amac_fund_sub_info
        目标地址: http://gs.amac.org.cn/amac-infodisc/res/pof/subfund/index.html
        描述: 获取中国证券投资基金业协会-信息公示-基金产品公示-证券公司私募投资基金
        限量: 单次返回当前时刻所有历史数据
        输入参数
            名称	类型	必选	描述
            -	-	-	-
        输出参数
            名称	类型	默认显示	描述
            产品编码	str	Y	-
            产品名称	str	Y	-
            私募基金管理人名称	str	Y	-
            托管人名称	str	Y	-
            成立日期	datetime.date	Y	-
            备案日期	datetime.date	Y	-
        '''
        df = ak.amac_fund_sub_info()
        return df

    def fund_simu_jijingongsijizigongsijiheziguanchapingongshi(self):
        '''
        基金公司及子公司集合资管产品公示
        接口: amac_fund_account_info
        目标地址: http://gs.amac.org.cn/amac-infodisc/res/fund/account/index.html
        描述: 获取中国证券投资基金业协会-信息公示-基金产品公示-基金公司及子公司集合资管产品公示
        限量: 单次返回当前时刻所有历史数据
        输入参数
            名称	类型	必选	描述
            -	-	-	-
        输出参数
            名称	类型	默认显示	描述
            成立日期	str	Y	-
            产品编码	str	Y	-
            产品名称	str	Y	-
            管理人名称	str	Y	-
        '''
        df = ak.amac_fund_account_info()
        return df

    def fund_simu_zichanzhichizhuanxiangjihua(self):
        '''
        资产支持专项计划
        接口: amac_fund_abs
        目标地址: http://gs.amac.org.cn/amac-infodisc/res/fund/account/index.html
        描述: 获取中国证券投资基金业协会-信息公示-基金产品公示-资产支持专项计划
        限量: 单次返回当前时刻所有历史数据
        输入参数
            名称	类型	必选	描述
            -	-	-	-
        输出参数
            名称	类型	默认显示	描述
            成立日期	str	Y	-
            产品编码	str	Y	-
            产品名称	str	Y	-
            管理人名称	str	Y	-
        '''
        df = ak.amac_fund_abs()
        return df

    def fund_simu_qihuogongsijiheziguanchanpingongshi(self):
        '''
        期货公司集合资管产品公示
        接口: amac_futures_info
        目标地址: http://gs.amac.org.cn/amac-infodisc/res/pof/futures/index.html
        描述: 获取中国证券投资基金业协会-信息公示-基金产品公示-期货公司集合资管产品公示
        限量: 单次返回当前时刻所有历史数据
        输入参数
            名称	类型	必选	描述
            -	-	-	-
        输出参数
            名称	类型	默认显示	描述
            产品名称	str	Y	-
            产品编码	str	Y	-
            管理人名称	str	Y	-
            托管人名称	str	Y	-
            成立日期	str	Y	-
            投资类型	str	Y	-
            是否分级	str	Y	-
            备案日期	str	Y	-
            到期日	str	Y	-
            运作状态	str	Y	-
        '''
        df = ak.amac_futures_info()
        return df

    def fund_simu_yizhuxiaosimujijinguanlirenmingdan(self):
        '''
        已注销私募基金管理人名单
        接口: amac_manager_cancelled_info
        目标地址: http://gs.amac.org.cn/amac-infodisc/res/cancelled/manager/index.html
        描述: 获取中国证券投资基金业协会-信息公示-诚信信息-已注销私募基金管理人名单
        限量: 单次返回当前时刻所有历史数据
        输入参数
            名称	类型	必选	描述
            -	-	-	-
        输出参数
            名称	类型	默认显示	描述
            管理人名称	str	Y	-
            统一社会信用代码	str	Y	-
            登记时间	str	Y	-
            注销时间	str	Y	-
            注销类型	str	Y	-
        '''
        df = ak.amac_manager_cancelled_info()
        return df

    def fund_gongmu_jijinjibenxinxi(self):
        '''
        基金基本信息
        接口: fund_em_fund_name
        目标地址: http://fund.eastmoney.com/fund.html#os_0;isall_0;ft_;pt_1
        描述: 获取东方财富网站-天天基金网-基金数据-所有基金的基本信息数据
        限量: 单次返回当前时刻所有历史数据
        输入参数
            名称	类型	必选	描述
            -	-	-	-
        输出参数
            名称	类型	默认显示	描述
            基金代码	str	Y	-
            拼音缩写	str	Y	-
            基金简称	str	Y	-
            基金类型	str	Y	-
            拼音全称	str	Y	-
        '''
        df = ak.fund_em_fund_name()
        return df

    def fund_gongmu_kaifangjijinshishishuju(self):
        '''
        开放式基金-实时数据
        接口: fund_em_open_fund_daily
        目标地址: http://fund.eastmoney.com/fund.html#os_0;isall_0;ft_;pt_1
        描述: 获取东方财富网站-天天基金网-基金数据, 此接口在每个交易日 16:00-23:00 更新当日的最新开放式基金净值数据
        限量: 单次返回当前时刻所有历史数据
        输入参数
            名称	类型	必选	描述
            -	-	-	-
        输出参数
            名称	类型	默认显示	描述
            基金代码	str	Y	-
            基金简称	str	Y	-
            单位净值	float	Y	随时间变动
            累计净值	float	Y	随时间变动
            前交易日-单位净值	float	Y	随时间变动
            前交易日-累计净值	float	Y	随时间变动
            日增长值	float	Y	-
            日增长率	float	Y	-
            申购状态	str	Y	-
            赎回状态	str	Y	-
            手续费	str	Y	注意单位: %
        '''
        df = ak.fund_em_open_fund_daily()
        return df

    def fund_gongmu_kaifangjijinlishishuju(self, fund="710001", indicator="单位净值走势"):
        '''
        开放式基金-历史数据
        接口: fund_em_open_fund_info
        目标地址: http://fund.eastmoney.com/pingzhongdata/710001.js
        描述: 获取东方财富网站-天天基金网-基金数据-具体基金信息
        限量: 单次返回当前时刻所有历史数据
        输入参数
            名称	类型	必选	描述
            fund	str	Y	fund="710001"; 需要基金代码, 可以通过调用 fund_em_open_fund_daily 获取
            indicator	str	Y	indicator="单位净值走势"; 参见 fund_em_open_fund_info 参数一览表
            fund_em_open_fund_info 参数一览表
            参数名称	备注
            单位净值走势	-
            累计净值走势	-
            累计收益率走势	-
            同类排名走势	-
            同类排名百分比	-
            分红送配详情	-
            拆分详情	-
        输出参数-单位净值走势
            名称	类型	默认显示	描述
            净值日期	str	Y	-
            单位净值	str	Y	-
            日增长率	str	Y	注意单位: %
        例子：
            ak.fund_em_open_fund_info(fund="710001", indicator="单位净值走势")
            ak.fund_em_open_fund_info(fund="710001", indicator="累计净值走势")
            ak.fund_em_open_fund_info(fund="710001", indicator="累计收益率走势")
            ak.fund_em_open_fund_info(fund="710001", indicator="同类排名走势")
            ak.fund_em_open_fund_info(fund="710001", indicator="同类排名百分比")
            ak.fund_em_open_fund_info(fund="161606", indicator="分红送配详情")
            ak.fund_em_open_fund_info(fund="161606", indicator="拆分详情")
        '''
        df = ak.fund_em_open_fund_info(fund=fund, indicator=indicator)
        return df

    def fund_gongmu_huobijijinshishishuju(self):
        '''
        货币型基金-实时数据
        接口: fund_em_money_fund_daily
        目标地址: http://fund.eastmoney.com/HBJJ_pjsyl.html
        描述: 获取东方财富网站-天天基金网-基金数据-货币型基金收益, 此接口数据每个交易日 16:00～23:00
        限量: 单次返回当前时刻所有历史数据
        输入参数
            名称	类型	必选	描述
            -	-	-	-
        输出参数
            名称	类型	默认显示	描述
            基金代码	str	Y	-
            基金简称	str	Y	-
            当前交易日-万份收益	float	Y	-
            当前交易日-7日年化%	float	Y	-
            当前交易日-单位净值	float	Y	-
            前一交易日-万份收益	float	Y	-
            前一交易日-7日年化%	float	Y	-
            前一交易日-单位净值	float	Y	-
            日涨幅	str	Y	-
            成立日期	str	Y	-
            基金经理	str	Y	-
            手续费	str	Y	-
            可购全部	str	Y	-
        接口示例
            import akshare as ak
            fund_em_money_fund_daily_df = ak.fund_em_money_fund_daily()
            print(fund_em_money_fund_daily_df)
        '''
        df = ak.fund_em_money_fund_daily()
        return df

    def fund_gongmu_huobijijinlishishuju(self, fund="000009"):
        '''
        货币型基金-历史数据
        接口: fund_em_money_fund_info
        目标地址: http://fundf10.eastmoney.com/jjjz_004186.html
        描述: 获取东方财富网站-天天基金网-基金数据-货币型基金历史净值
        限量: 单次返回当前时刻所有历史数据
        输入参数
            名称	类型	必选	描述
            fund	str	Y	fund="000009"; 需要基金代码, 可以通过调用 fund_em_money_fund_daily 获取
        输出参数
            名称	类型	默认显示	描述
            净值日期	str	Y	-
            每万份收益	str	Y	-
            7日年化收益率	float	Y	-
            申购状态	str	Y	-
            赎回状态	str	Y	-
        '''
        df = ak.fund_em_money_fund_info(fund=fund)
        return df

    def fund_gongmu_licaijijinshishishuju(self):
        '''
        理财型基金-实时数据
        接口: fund_em_financial_fund_daily
        目标地址: http://fund.eastmoney.com/lcjj.html#1_1__0__ljjz,desc_1_os1
        描述: 获取东方财富网站-天天基金网-基金数据-理财型基金-实时数据, 此接口数据每个交易日 16:00～23:00 更新
        限量: 单次返回当前时刻所有历史数据
        输入参数
            名称	类型	必选	描述
            -	-	-	-
        输出参数
            名称	类型	默认显示	描述
            序号	int	Y	-
            基金代码	str	Y	-
            基金简称	str	Y	-
            上一期年化收益率	float	Y	-
            当前交易日-万份收益	float	Y	-
            当前交易日-7日年华	float	Y	-
            前一个交易日-万份收益	float	Y	-
            前一个交易日-7日年华	float	Y	-
            封闭期	float	Y	-
            申购状态	str	Y	-
        '''
        df = ak.fund_em_financial_fund_daily()
        return df

    def fund_gongmu_licaijijinlishishuju(self, fund="000134"):
        '''
        理财型基金-历史数据
        接口: fund_em_financial_fund_info
        目标地址: http://fundf10.eastmoney.com/jjjz_000791.html
        描述: 获取东方财富网站-天天基金网-基金数据-理财型基金-基金净值数据
        限量: 单次返回当前时刻所有历史数据
        输入参数
            名称	类型	必选	描述
            fund	str	Y	fund="000134"; 需要基金代码, 可以通过调用 fund_em_financial_fund_daily 获取
        输出参数
            名称	类型	默认显示	描述
            净值日期	str	Y	-
            每万份收益	str	Y	-
            7日年化收益率	float	Y	-
            申购状态	str	Y	-
            赎回状态	str	Y	-
        '''
        df = ak.fund_em_financial_fund_info(fund=fund)
        return df

    def fund_gongmu_fenjijijinshishishuju(self):
        '''
        分级基金-实时数据
        接口: fund_em_graded_fund_daily
        目标地址: http://fund.eastmoney.com/fjjj.html#1_1__0__zdf,desc_1
        描述: 获取东方财富网站-天天基金网-基金数据-分级基金-实时数据, 此接口数据每个交易日 16:00～23:00
        限量: 单次返回当前时刻所有历史数据
        输入参数
            名称	类型	必选	描述
            -	-	-	-
        输出参数
            名称	类型	默认显示	描述
            基金代码	str	Y	-
            基金简称	str	Y	-
            单位净值	float	Y	-
            累计净值	float	Y	-
            前交易日-单位净值	float	Y	-
            前交易日-累计净值	float	Y	-
            日增长值	float	Y	-
            日增长率	float	Y	注意单位
            市价	str	Y	-
            折价率	str	Y	-
            手续费	str	Y	-
        '''
        df = ak.fund_em_graded_fund_daily()
        return df

    def fund_gongmu_fenjijijinlishishuju(self, fund="150232"):
        '''
        分级基金-历史数据
        接口: fund_em_graded_fund_info
        目标地址: http://fundf10.eastmoney.com/jjjz_004186.html
        描述: 获取东方财富网站-天天基金网-基金数据-分级基金-历史数据
        限量: 单次返回当前时刻所有历史数据
        输入参数
            名称	类型	必选	描述
            fund	str	Y	fund="150232"; 需要基金代码, 可以通过调用 fund_em_graded_fund_daily 获取
        输出参数
            名称	类型	默认显示	描述
            净值日期	str	Y	-
            单位净值	float	Y	-
            累计净值	float	Y	-
            日增长率	float	Y	注意单位: %; 日增长率为空原因如下: 1. 非交易日净值不参与日增长率计算(灰色数据行). 2. 上一交易日净值未披露, 日增长率无法计算.
            申购状态	str	Y	-
            赎回状态	str	Y	-
        '''
        df = ak.fund_em_graded_fund_info(fund=fund)
        return df

    def fund_gongmu_changneijiaoyijijinshishishuju(self):
        '''
        场内交易基金-实时数据
        接口: fund_em_etf_fund_daily
        目标地址: http://fund.eastmoney.com/cnjy_dwjz.html
        描述: 获取东方财富网站-天天基金网-基金数据-场内交易基金-实时数据, 此接口数据每个交易日 16:00～23:00
        限量: 单次返回当前时刻所有数据
        输入参数
            名称	类型	必选	描述
            -	-	-	-
        输出参数
            名称	类型	默认显示	描述
            基金代码	str	Y	-
            基金简称	str	Y	-
            类型	float	Y	-
            当前交易日-单位净值	float	Y	会返回具体的日期值作为字段
            当前交易日-累计净值	float	Y	会返回具体的日期值作为字段
            前一个交易日-单位净值	float	Y	会返回具体的日期值作为字段
            前一个交易日-累计净值	float	Y	会返回具体的日期值作为字段
            增长值	float	Y	-
            增长率	str	Y	-
            市价	str	Y	-
            折价率	str	Y	-
        '''
        df = ak.fund_em_etf_fund_daily()
        return df

    def fund_gongmu_changneijiaoyijijinlishishuju(self, fund="511280"):
        '''
        场内交易基金-历史数据
        接口: fund_em_etf_fund_info
        目标地址: http://fundf10.eastmoney.com/jjjz_004186.html
        描述: 获取东方财富网站-天天基金网-基金数据-场内交易基金-历史净值数据
        限量: 单次返回当前时刻所有历史数据
        输入参数
            名称	类型	必选	描述
            fund	str	Y	fund="511280"; 需要基金代码, 可以通过调用 fund_em_etf_fund_daily 获取
        输出参数
            名称	类型	默认显示	描述
            净值日期	str	Y	-
            单位净值	float	Y	-
            累计净值	float	Y	-
            日增长率	float	Y	注意单位(%)
            申购状态	str	Y	-
            赎回状态	str	Y	-
        '''
        df = ak.fund_em_etf_fund_info(fund=fund)
        return df

    def fund_gongmu_kaifangshijijinpaihang(self):
        '''
        开放式基金排行
        接口: fund_em_open_fund_rank
        目标地址: http://fund.eastmoney.com/data/fundranking.html
        描述: 获取东方财富网-数据中心-开放式基金排行
        限量: 单次返回当前时刻所有数据
        输入参数
            名称	类型	必选	描述
            -	-	-	-
        输出参数
            名称	类型	默认显示	描述
            序号	int	Y	-
            基金代码	str	Y	-
            基金简称	str	Y	-
            日期	str	Y	-
            单位净值	float	Y	-
            累计净值	float	Y	-
            日增长率	float	Y	注意单位: %
            近1周	float	Y	注意单位: %
            近1月	float	Y	注意单位: %
            近3月	float	Y	注意单位: %
            近6月	float	Y	注意单位: %
            近1年	float	Y	注意单位: %
            近2年	float	Y	注意单位: %
            近3年	float	Y	注意单位: %
            今年来	float	Y	注意单位: %
            成立来	float	Y	注意单位: %
            自定义	float	Y	注意单位: %
            手续费	str	Y	-
        '''
        df = ak.fund_em_open_fund_rank()
        return df

    def fund_gongmu_changneijijinpaihang(self):
        '''
        场内交易基金排行榜
        接口: fund_em_exchange_rank
        目标地址: http://fund.eastmoney.com/data/fbsfundranking.html
        描述: 获取东方财富网-数据中心-场内交易基金排行榜
        限量: 单次返回当前时刻所有数据, 每个交易日17点后更新
        输入参数
            名称	类型	必选	描述
            -	-	-	-
        输出参数
            名称	类型	默认显示	描述
            序号	int	Y	-
            基金代码	str	Y	-
            基金简称	str	Y	-
            日期	str	Y	-
            单位净值	float	Y	-
            累计净值	float	Y	-
            近1周	float	Y	注意单位: %
            近1月	float	Y	注意单位: %
            近3月	float	Y	注意单位: %
            近6月	float	Y	注意单位: %
            近1年	float	Y	注意单位: %
            近2年	float	Y	注意单位: %
            近3年	float	Y	注意单位: %
            今年来	float	Y	注意单位: %
            成立来	float	Y	注意单位: %
        '''
        df = ak.fund_em_exchange_rank()
        return df

    def fund_gongmu_huobijijinpaihang(self):
        '''
        货币型基金排行
        接口: fund_em_money_rank
        目标地址: http://fund.eastmoney.com/data/hbxfundranking.html
        描述: 获取东方财富网-数据中心-货币型基金排行
        限量: 单次返回当前时刻所有数据, 每个交易日17点后更新, 货币基金的单位净值均为 1.0000 元，最新一年期定存利率: 1.50%
        输入参数
            名称	类型	必选	描述
            -	-	-	-
        输出参数
            名称	类型	默认显示	描述
            序号	int	Y	-
            基金代码	str	Y	-
            基金简称	str	Y	-
            日期	str	Y	-
            万份收益	float	Y	注意单位: %
            年化收益率7日	float	Y	注意单位: %
            年化收益率14日	float	Y	注意单位: %
            年化收益率28日	float	Y	注意单位: %
            近1月	float	Y	注意单位: %
            近3月	float	Y	注意单位: %
            近6月	float	Y	注意单位: %
            近1年	float	Y	注意单位: %
            近2年	float	Y	注意单位: %
            近3年	float	Y	注意单位: %
            近5年	float	Y	注意单位: %
            今年来	float	Y	注意单位: %
            成立来	float	Y	注意单位: %
            手续费	float	Y	-
        '''
        df = ak.fund_em_money_rank()
        return df

    def fund_gongmu_jingzhigusuan(self):
        '''
        净值估算
        接口: fund_em_value_estimation
        目标地址: http://fund.eastmoney.com/fundguzhi.html
        描述: 获取东方财富网-数据中心-净值估算
        限量: 单次返回当前时刻所有数据
        输入参数
            名称	类型	必选	描述
            symbol	str	Y	symbol='股票指数'; 默认返回所有数据; choice of {'股票指数', '联接基金', '混合型', '股票型', 'QDII-指数', '债券型', '定开债券', '债券指数', '其他创新', 'QDII', '混合-FOF', '股票-FOF'}
        输出参数
            名称	类型	默认显示	描述
            基金代码	str	Y	-
            基金类型	str	Y	-
            估算值	float	Y	-
            估算增长率	str	Y	注意单位: %
            单位净值	float	Y	-
            基金名称	str	Y	-
        '''
        df = ak.fund_em_value_estimation()
        return df

    def fund_gongmu_jijinhangqing(self, symbol="sz159996"):
        '''
        基金行情
        接口: fund_etf_hist_sina
        目标地址: http://vip.stock.finance.sina.com.cn/fund_center/index.html#jjhqetf
        描述: 获取新浪财经-基金行情的日频率行情数据
        限量: 单次返回指定基金的所有数据
        输入参数
            名称	类型	必选	描述
            symbol	str	Y	symbol="sz169103"; 基金列表可以通过 fund_etf_category_sina(symbol="LOF基金") 可选参数为: 封闭式基金, ETF基金, LOF基金 查询
        输出参数
            名称	类型	默认显示	描述
            date	str	Y	-
            open	str	Y	-
            high	float	Y	-
            low	str	Y	-
            close	float	Y	-
            volume	str	Y	注意单位: 手
        '''
        df = ak.fund_etf_hist_sina(symbol=symbol)
        return df