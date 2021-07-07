#! /usr/bin/env python
# coding: utf-8
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import numpy as np
import akshare as ak
import stock_data.akshare_fund_data as AKSF
from stock_data.csv_io import CSVIO


class AKShareFundDownloader(object):
    def __init__(self, data_dir):
        self.data_dir = data_dir
        self.fund_data = AKSF.AKShareFund()

    def dump_fund_simu_congyerenyuanxinxi(self, cover=False):
        csv_path = os.path.join(self.data_dir, 'fund/simu')
        if not os.path.exists(csv_path):
            os.makedirs(csv_path)
        csv_file = os.path.join(csv_path, 'congyerenyuanxinxi.csv')
        if os.path.exists(csv_file):
            print(f'loading from exist file ......')
            df = self.load_fund_simu_congyerenyuanxinxi(csv_file='congyerenyuanxinxi.csv')
        else:
            df = self.fund_data.fund_simu_congyerenyuanxinxi()
        CSVIO.writer(df, csv_file=csv_file, append=False)
        return df

    def load_fund_simu_congyerenyuanxinxi(self):
        csv_file = os.path.join(self.data_dir, 'fund/simu/congyerenyuanxinxi.csv')
        if not os.path.exists(csv_file):
            print(f'downloading ......')
            df = self.dump_fund_simu_congyerenyuanxinxi()
            return df
        df = CSVIO.reader(csv_file=csv_file)
        return df

    def dump_fund_simu_jijincongyerenyuanzigezhucexinxi(self, cover=False):
        csv_path = os.path.join(self.data_dir, 'fund/simu')
        if not os.path.exists(csv_path):
            os.makedirs(csv_path)
        csv_file = os.path.join(csv_path, 'jijincongyerenyuanzigezhucexinxi.csv')
        if os.path.exists(csv_file):
            print(f'loading from exist file ......')
            df = self.load_fund_simu_jijincongyerenyuanzigezhucexinxi(csv_file='congyerenyuanxinxi.csv')
        else:
            df = self.fund_data.fund_simu_jijincongyerenyuanzigezhucexinxi()
        CSVIO.writer(df, csv_file=csv_file, append=False)
        return df

    def load_fund_simu_jijincongyerenyuanzigezhucexinxi(self):
        csv_file = os.path.join(self.data_dir, 'fund/simu/jijincongyerenyuanzigezhucexinxi.csv')
        if not os.path.exists(csv_file):
            print(f'downloading ......')
            df = self.dump_fund_simu_jijincongyerenyuanzigezhucexinxi()
            return df
        df = CSVIO.reader(csv_file=csv_file)
        return df

    def dump_fund_simu_jijinguanlirenzonghechaxun(self, cover=False):
        csv_path = os.path.join(self.data_dir, 'fund/simu')
        if not os.path.exists(csv_path):
            os.makedirs(csv_path)
        csv_file = os.path.join(csv_path, 'jijinguanlirenzonghechaxun.csv')
        if os.path.exists(csv_file):
            print(f'loading from exist file ......')
            df = self.load_fund_simu_jijinguanlirenzonghechaxun()
        else:
            df = self.fund_data.fund_simu_jijinguanlirenzonghechaxun()
        CSVIO.writer(df, csv_file=csv_file, append=False)
        return df

    def load_fund_simu_jijinguanlirenzonghechaxun(self):
        csv_file = os.path.join(self.data_dir, 'fund/simu/jijinguanlirenzonghechaxun.csv')
        if not os.path.exists(csv_file):
            print(f'downloading ......')
            df = self.dump_fund_simu_jijinguanlirenzonghechaxun()
            return df
        df = CSVIO.reader(csv_file=csv_file)
        return df

    def dump_fund_simu_jijinguanlirenfenleigongshi(self, cover=False):
        csv_path = os.path.join(self.data_dir, 'fund/simu')
        if not os.path.exists(csv_path):
            os.makedirs(csv_path)
        csv_file = os.path.join(csv_path, 'jijinguanlirenfenleigongshi.csv')
        if os.path.exists(csv_file):
            print(f'loading from exist file ......')
            df = self.load_fund_simu_jijinguanlirenfenleigongshi(csv_file='jijinguanlirenfenleigongshi.csv')
        else:
            df = self.fund_data.fund_simu_jijinguanlirenfenleigongshi()
        CSVIO.writer(df, csv_file=csv_file, append=False)
        return df

    def load_fund_simu_jijinguanlirenfenleigongshi(self):
        csv_file = os.path.join(self.data_dir, 'fund/simu/jijinguanlirenfenleigongshi.csv')
        if not os.path.exists(csv_file):
            print(f'downloading ......')
            df = self.dump_fund_simu_jijinguanlirenfenleigongshi()
            return df
        df = CSVIO.reader(csv_file=csv_file)
        return df

    def dump_fund_simu_zhengquangongsisimujijinzigongsiguanlirenxinxigongshi(self, cover=False):
        csv_path = os.path.join(self.data_dir, 'fund/simu')
        if not os.path.exists(csv_path):
            os.makedirs(csv_path)
        csv_file = os.path.join(csv_path, 'zhengquangongsisimujijinzigongsiguanlirenxinxigongshi.csv')
        if os.path.exists(csv_file):
            print(f'loading from exist file ......')
            df = self.load_fund_simu_zhengquangongsisimujijinzigongsiguanlirenxinxigongshi()
        else:
            df = self.fund_data.fund_simu_congyerenyuanxinxi()
        CSVIO.writer(df, csv_file=csv_file, append=False)
        return df

    def load_fund_simu_zhengquangongsisimujijinzigongsiguanlirenxinxigongshi(self):
        csv_file = os.path.join(self.data_dir, 'fund/simu/zhengquangongsisimujijinzigongsiguanlirenxinxigongshi.csv')
        if not os.path.exists(csv_file):
            print(f'downloading ......')
            df = self.dump_fund_simu_zhengquangongsisimujijinzigongsiguanlirenxinxigongshi()
            return df
        df = CSVIO.reader(csv_file=csv_file)
        return df

    def dump_fund_simu_jijinguanlirenjijinchanpin(self, cover=False):
        csv_path = os.path.join(self.data_dir, 'fund/simu')
        if not os.path.exists(csv_path):
            os.makedirs(csv_path)
        csv_file = os.path.join(csv_path, 'jijinguanlirenjijinchanpin.csv')
        if os.path.exists(csv_file):
            print(f'loading from exist file ......')
            df = self.load_fund_simu_jijinguanlirenjijinchanpin(csv_file='jijinguanlirenjijinchanpin.csv')
        else:
            df = self.fund_data.fund_simu_jijinguanlirenjijinchanpin()
        CSVIO.writer(df, csv_file=csv_file, append=False)
        return df

    def load_fund_simu_jijinguanlirenjijinchanpin(self):
        csv_file = os.path.join(self.data_dir, 'fund/simu/jijinguanlirenjijinchanpin.csv')
        if not os.path.exists(csv_file):
            print(f'downloading ......')
            df = self.dump_fund_simu_jijinguanlirenjijinchanpin()
            return df
        df = CSVIO.reader(csv_file=csv_file)
        return df

    def dump_fund_simu_zhengquangongsijiheziguanchanpingongshi(self, cover=False):
        csv_path = os.path.join(self.data_dir, 'fund/simu')
        if not os.path.exists(csv_path):
            os.makedirs(csv_path)
        csv_file = os.path.join(csv_path, 'zhengquangongsijiheziguanchanpingongshi.csv')
        if os.path.exists(csv_file):
            print(f'loading from exist file ......')
            df = self.load_fund_simu_zhengquangongsijiheziguanchanpingongshi(csv_file='zhengquangongsijiheziguanchanpingongshi.csv')
        else:
            df = self.fund_data.fund_simu_zhengquangongsijiheziguanchanpingongshi()
        CSVIO.writer(df, csv_file=csv_file, append=False)
        return df

    def load_fund_simu_zhengquangongsijiheziguanchanpingongshi(self):
        csv_file = os.path.join(self.data_dir, 'fund/simu/zhengquangongsijiheziguanchanpingongshi.csv')
        if not os.path.exists(csv_file):
            print(f'downloading ......')
            df = self.dump_fund_simu_zhengquangongsijiheziguanchanpingongshi()
            return df
        df = CSVIO.reader(csv_file=csv_file)
        return df

    def dump_fund_simu_zhengquangongsizhitoujijin(self, cover=False):
        csv_path = os.path.join(self.data_dir, 'fund/simu')
        if not os.path.exists(csv_path):
            os.makedirs(csv_path)
        csv_file = os.path.join(csv_path, 'zhengquangongsizhitoujijin.csv')
        if os.path.exists(csv_file):
            print(f'loading from exist file ......')
            df = self.load_fund_simu_zhengquangongsizhitoujijin(csv_file='zhengquangongsizhitoujijin.csv')
        else:
            df = self.fund_data.fund_simu_zhengquangongsizhitoujijin()
        CSVIO.writer(df, csv_file=csv_file, append=False)
        return df

    def load_fund_simu_zhengquangongsizhitoujijin(self):
        csv_file = os.path.join(self.data_dir, 'fund/simu/zhengquangongsizhitoujijin.csv')
        if not os.path.exists(csv_file):
            print(f'downloading ......')
            df = self.dump_fund_simu_zhengquangongsizhitoujijin()
            return df
        df = CSVIO.reader(csv_file=csv_file)
        return df

    def dump_fund_simu_zhengquangongsisimutouzijijin(self, cover=False):
        csv_path = os.path.join(self.data_dir, 'fund/simu')
        if not os.path.exists(csv_path):
            os.makedirs(csv_path)
        csv_file = os.path.join(csv_path, 'zhengquangongsisimutouzijijin.csv')
        if os.path.exists(csv_file):
            print(f'loading from exist file ......')
            df = self.load_fund_simu_zhengquangongsisimutouzijijin(csv_file='zhengquangongsisimutouzijijin.csv')
        else:
            df = self.fund_data.fund_simu_zhengquangongsisimutouzijijin()
        CSVIO.writer(df, csv_file=csv_file, append=False)
        return df

    def load_fund_simu_zhengquangongsisimutouzijijin(self):
        csv_file = os.path.join(self.data_dir, 'fund/simu/zhengquangongsisimutouzijijin.csv')
        if not os.path.exists(csv_file):
            print(f'downloading ......')
            df = self.dump_fund_simu_zhengquangongsisimutouzijijin()
            return df
        df = CSVIO.reader(csv_file=csv_file)
        return df

    def dump_fund_simu_jijingongsijizigongsijiheziguanchapingongshi(self, cover=False):
        csv_path = os.path.join(self.data_dir, 'fund/simu')
        if not os.path.exists(csv_path):
            os.makedirs(csv_path)
        csv_file = os.path.join(csv_path, 'jijingongsijizisongsijiheziguanchapingongshi.csv')
        if os.path.exists(csv_file):
            print(f'loading from exist file ......')
            df = self.load_fund_simu_jijingongsijizigongsijiheziguanchapingongshi(csv_file='jijingongsijizisongsijiheziguanchapingongshi.csv')
        else:
            df = self.fund_data.fund_simu_jijingongsijizigongsijiheziguanchapingongshi()
        CSVIO.writer(df, csv_file=csv_file, append=False)
        return df

    def load_fund_simu_jijingongsijizigongsijiheziguanchapingongshi(self):
        csv_file = os.path.join(self.data_dir, 'fund/simu/jijingongsijizisongsijiheziguanchapingongshi.csv')
        if not os.path.exists(csv_file):
            print(f'downloading ......')
            df = self.dump_fund_simu_jijingongsijizisongsijiheziguanchapingongshi()
            return df
        df = CSVIO.reader(csv_file=csv_file)
        return df

    def dump_fund_simu_zichanzhichizhuanxiangjihua(self, cover=False):
        csv_path = os.path.join(self.data_dir, 'fund/simu')
        if not os.path.exists(csv_path):
            os.makedirs(csv_path)
        csv_file = os.path.join(csv_path, 'zichanzhichizhuanxiangjihua.csv')
        if os.path.exists(csv_file):
            print(f'loading from exist file ......')
            df = self.load_fund_simu_zichanzhichizhuanxiangjihua(csv_file='zichanzhichizhuanxiangjihua.csv')
        else:
            df = self.fund_data.fund_simu_zichanzhichizhuanxiangjihua()
        CSVIO.writer(df, csv_file=csv_file, append=False)
        return df

    def load_fund_simu_zichanzhichizhuanxiangjihua(self):
        csv_file = os.path.join(self.data_dir, 'fund/simu/zichanzhichizhuanxiangjihua.csv')
        if not os.path.exists(csv_file):
            print(f'downloading ......')
            df = self.dump_fund_simu_zichanzhichizhuanxiangjihua()
            return df
        df = CSVIO.reader(csv_file=csv_file)
        return df

    def dump_fund_simu_qihuogongsijiheziguanchanpingongshi(self, cover=False):
        csv_path = os.path.join(self.data_dir, 'fund/simu')
        if not os.path.exists(csv_path):
            os.makedirs(csv_path)
        csv_file = os.path.join(csv_path, 'qihuogongsijiheziguanchanpingongshi.csv')
        if os.path.exists(csv_file):
            print(f'loading from exist file ......')
            df = self.load_fund_simu_qihuogongsijiheziguanchanpingongshi(csv_file='qihuogongsijiheziguanchanpingongshi.csv')
        else:
            df = self.fund_data.fund_simu_qihuogongsijiheziguanchanpingongshi()
        CSVIO.writer(df, csv_file=csv_file, append=False)
        return df

    def load_fund_simu_qihuogongsijiheziguanchanpingongshi(self):
        csv_file = os.path.join(self.data_dir, 'fund/simu/qihuogongsijiheziguanchanpingongshi.csv')
        if not os.path.exists(csv_file):
            print(f'downloading ......')
            df = self.dump_fund_simu_qihuogongsijiheziguanchanpingongshi()
            return df
        df = CSVIO.reader(csv_file=csv_file)
        return df

    def dump_fund_simu_yizhuxiaosimujijinguanlirenmingdan(self, cover=False):
        csv_path = os.path.join(self.data_dir, 'fund/simu')
        if not os.path.exists(csv_path):
            os.makedirs(csv_path)
        csv_file = os.path.join(csv_path, 'yizhuxiaosimujijinguanlirenmingdan.csv')
        if os.path.exists(csv_file):
            print(f'loading from exist file ......')
            df = self.load_fund_simu_yizhuxiaosimujijinguanlirenmingdan(csv_file='yizhuxiaosimujijinguanlirenmingdan.csv')
        else:
            df = self.fund_data.fund_simu_yizhuxiaosimujijinguanlirenmingdan()
        CSVIO.writer(df, csv_file=csv_file, append=False)
        return df

    def load_fund_simu_yizhuxiaosimujijinguanlirenmingdan(self):
        csv_file = os.path.join(self.data_dir, 'fund/simu/yizhuxiaosimujijinguanlirenmingdan.csv')
        if not os.path.exists(csv_file):
            print(f'downloading ......')
            df = self.dump_fund_simu_yizhuxiaosimujijinguanlirenmingdan()
            return df
        df = CSVIO.reader(csv_file=csv_file)
        return df

    # =============================================================================
    # 公募基金
    def dump_fund_gongmu_jijinjibenxinxi(self, cover=False):
        csv_path = os.path.join(self.data_dir, 'fund/gongmu')
        if not os.path.exists(csv_path):
            os.makedirs(csv_path)
        csv_file = os.path.join(csv_path, 'jijinjibenxinxi.csv')
        if os.path.exists(csv_file):
            print(f'loading from exist file ......')
            df = self.load_fund_gongmu_jijinjibenxinxi(csv_file='jijinjibenxinxi.csv')
        else:
            df = self.fund_data.fund_gongmu_jijinjibenxinxi()
        CSVIO.writer(df, csv_file=csv_file, append=False)
        return df

    def load_fund_gongmu_jijinjibenxinxi(self):
        csv_file = os.path.join(self.data_dir, 'fund/gongmu/jijinjibenxinxi.csv')
        if not os.path.exists(csv_file):
            print(f'downloading ......')
            df = self.dump_fund_gongmu_jijinjibenxinxi()
            return df
        df = CSVIO.reader(csv_file=csv_file)
        return df

    def dump_fund_gongmu_kaifangjijinshishishuju(self, cover=False):
        csv_path = os.path.join(self.data_dir, 'fund/gongmu/details/kaifang')
        if not os.path.exists(csv_path):
            os.makedirs(csv_path)
        csv_file = os.path.join(csv_path, f'kaifangjijinshishishuju.csv')
        if os.path.exists(csv_file):
            print(f'loading from exist file ......')
            df = self.load_fund_gongmu_kaifangjijinshishishuju(csv_file='kaifangjijinshishishuju.csv')
        else:
            df = self.fund_data.fund_gongmu_kaifangjijinshishishuju()
        CSVIO.writer(df, csv_file=csv_file, append=False)
        return df

    def load_fund_gongmu_kaifangjijinshishishuju(self):
        csv_file = os.path.join(self.data_dir, 'fund/gongmu//details/kaifang/kaifangjijinshishishuju.csv')
        if not os.path.exists(csv_file):
            print(f'downloading ......')
            df = self.dump_fund_gongmu_kaifangjijinshishishuju()
            return df
        df = CSVIO.reader(csv_file=csv_file)
        return df

    def dump_fund_gongmu_kaifangjijinlishishuju(self, fund="710001", indicator="单位净值走势", cover=False):
        csv_path = os.path.join(self.data_dir, 'fund/gongmu/details/kaifang')
        if not os.path.exists(csv_path):
            os.makedirs(csv_path)
        csv_file = os.path.join(csv_path, f'{fund}-{indicator}.csv')
        if os.path.exists(csv_file):
            print(f'loading from exist file ......')
            df = self.load_fund_gongmu_kaifangjijinlishishuju(fund=fund, indicator=indicator)
        else:
            df = self.fund_data.fund_gongmu_kaifangjijinlishishuju(fund=fund, indicator=indicator)
        CSVIO.writer(df, csv_file=csv_file, append=False)
        return df

    def load_fund_gongmu_kaifangjijinlishishuju(self, fund="710001", indicator="单位净值走势"):
        csv_file = os.path.join(self.data_dir, f'fund/gongmu/details/kaifang/{fund}-{indicator}.csv')
        if not os.path.exists(csv_file):
            print(f'downloading ......')
            df = self.dump_fund_gongmu_kaifangjijinlishishuju(fund=fund, indicator=indicator)
            return df
        df = CSVIO.reader(csv_file=csv_file)
        return df

    def dump_fund_gongmu_huobijijinshishishuju(self, fund="000009"):
        csv_path = os.path.join(self.data_dir, 'fund/gongmu/details/huobijijin')
        if not os.path.exists(csv_path):
            os.makedirs(csv_path)
        csv_file = os.path.join(csv_path, f'{fund}.csv')
        if os.path.exists(csv_file):
            print(f'loading from exist file ......')
            df = self.load_fund_gongmu_huobijijinshishishuju(fund=fund)
        else:
            df = self.fund_data.fund_gongmu_huobijijinshishishuju()
        CSVIO.writer(df, csv_file=csv_file, append=False)
        return df

    def load_fund_gongmu_huobijijinshishishuju(self, fund="000009"):
        csv_file = os.path.join(self.data_dir, f'fund/gongmu/details/huobijijin/{fund}.csv')
        if not os.path.exists(csv_file):
            print(f'downloading ......')
            df = self.dump_fund_gongmu_huobijijinshishishuju()
            return df
        df = CSVIO.reader(csv_file=csv_file)
        return df

    def dump_fund_gongmu_huobijijinlishishuju(self, fund="000009"):
        csv_path = os.path.join(self.data_dir, 'fund/gongmu/details/huobijijin')
        if not os.path.exists(csv_path):
            os.makedirs(csv_path)
        csv_file = os.path.join(csv_path, f'{fund}.csv')
        if os.path.exists(csv_file):
            print(f'loading from exist file ......')
            df = self.load_fund_gongmu_huobijijinlishishuju(fund=fund)
        else:
            df = self.fund_data.fund_gongmu_huobijijinlishishuju(fund=fund)
        CSVIO.writer(df, csv_file=csv_file, append=False)
        return df

    def load_fund_gongmu_huobijijinlishishuju(self, fund="000009"):
        csv_file = os.path.join(self.data_dir, f'fund/gongmu/details/huobijijin/{fund}.csv')
        if not os.path.exists(csv_file):
            print(f'downloading ......')
            df = self.dump_fund_gongmu_huobijijinlishishuju(fund=fund)
            return df
        df = CSVIO.reader(csv_file=csv_file)
        return df

    def dump_fund_gongmu_licaijijinshishishuju(self):
        csv_path = os.path.join(self.data_dir, 'fund/gongmu/details/licaijijin')
        if not os.path.exists(csv_path):
            os.makedirs(csv_path)
        csv_file = os.path.join(csv_path, f'licaijijinshishishuju.csv')
        if os.path.exists(csv_file):
            print(f'loading from exist file ......')
            df = self.load_fund_gongmu_licaijijinshishishuju()
        else:
            df = self.fund_data.fund_gongmu_licaijijinshishishuju()
        CSVIO.writer(df, csv_file=csv_file, append=False)
        return df

    def load_fund_gongmu_licaijijinshishishuju(self):
        csv_file = os.path.join(self.data_dir, f'fund/gongmu/details/licaijijin/licaijijinshishishuju.csv')
        if not os.path.exists(csv_file):
            print(f'downloading ......')
            df = self.dump_fund_gongmu_licaijijinshishishuju()
            return df
        df = CSVIO.reader(csv_file=csv_file)
        return df

    def dump_fund_gongmu_licaijijinlishishuju(self, fund="000134"):
        csv_path = os.path.join(self.data_dir, 'fund/gongmu/details/licaijijin')
        if not os.path.exists(csv_path):
            os.makedirs(csv_path)
        csv_file = os.path.join(csv_path, f'licaijijinlishishuju.csv')
        if os.path.exists(csv_file):
            print(f'loading from exist file ......')
            df = self.load_fund_gongmu_licaijijinlishishuju(fund=fund)
        else:
            df = self.fund_data.fund_gongmu_licaijijinlishishuju(fund=fund)
        CSVIO.writer(df, csv_file=csv_file, append=False)
        return df

    def load_fund_gongmu_licaijijinlishishuju(self, fund="000134"):
        csv_file = os.path.join(self.data_dir, f'fund/gongmu/details/licaijijin/licaijijinlishishuju.csv')
        if not os.path.exists(csv_file):
            print(f'downloading ......')
            df = self.dump_fund_gongmu_licaijijinlishishuju(fund=fund)
            return df
        df = CSVIO.reader(csv_file=csv_file)
        return df

    def dump_fund_gongmu_fenjijijinshishishuju(self):
        csv_path = os.path.join(self.data_dir, 'fund/gongmu/details/fenjijijin')
        if not os.path.exists(csv_path):
            os.makedirs(csv_path)
        csv_file = os.path.join(csv_path, f'fenjijijinshishishuju.csv')
        if os.path.exists(csv_file):
            print(f'loading from exist file ......')
            df = self.load_fund_gongmu_fenjijijinshishishuju()
        else:
            df = self.fund_data.fund_gongmu_fenjijijinshishishuju()
        CSVIO.writer(df, csv_file=csv_file, append=False)
        return df

    def load_fund_gongmu_fenjijijinshishishuju(self):
        csv_file = os.path.join(self.data_dir, f'fund/gongmu/details/fenjijijin/fenjijijinshishishuju.csv')
        if not os.path.exists(csv_file):
            print(f'downloading ......')
            df = self.dump_fund_gongmu_fenjijijinshishishuju()
            return df
        df = CSVIO.reader(csv_file=csv_file)
        return df

    def dump_fund_gongmu_fenjijijinlishishuju(self, fund="150232"):
        csv_path = os.path.join(self.data_dir, 'fund/gongmu/details/fenjijijin')
        if not os.path.exists(csv_path):
            os.makedirs(csv_path)
        csv_file = os.path.join(csv_path, f'{fund}.csv')
        if os.path.exists(csv_file):
            print(f'loading from exist file ......')
            df = self.load_fund_gongmu_fenjijijinlishishuju(fund=fund)
        else:
            df = self.fund_data.fund_gongmu_fenjijijinlishishuju(fund=fund)
        CSVIO.writer(df, csv_file=csv_file, append=False)
        return df

    def load_fund_gongmu_fenjijijinlishishuju(self, fund="150232"):
        csv_file = os.path.join(self.data_dir, f'fund/gongmu/details/fenjijijin/{fund}.csv')
        if not os.path.exists(csv_file):
            print(f'downloading ......')
            df = self.dump_fund_gongmu_fenjijijinlishishuju(fund=fund)
            return df
        df = CSVIO.reader(csv_file=csv_file)
        return df

    def dump_fund_gongmu_changneijiaoyijijinshishishuju(self):
        csv_path = os.path.join(self.data_dir, 'fund/gongmu/details/changneijiaoyijijin')
        if not os.path.exists(csv_path):
            os.makedirs(csv_path)
        csv_file = os.path.join(csv_path, f'changneijiaoyijijinshishishuju.csv')
        if os.path.exists(csv_file):
            print(f'loading from exist file ......')
            df = self.load_fund_gongmu_changneijiaoyijijinshishishuju()
        else:
            df = self.fund_data.fund_gongmu_changneijiaoyijijinshishishuju()
        CSVIO.writer(df, csv_file=csv_file, append=False)
        return df

    def load_fund_gongmu_changneijiaoyijijinshishishuju(self):
        csv_file = os.path.join(self.data_dir, f'fund/gongmu/details/changneijiaoyijijin/changneijiaoyijijinshishishuju.csv')
        if not os.path.exists(csv_file):
            print(f'downloading ......')
            df = self.dump_fund_gongmu_changneijiaoyijijinshishishuju()
            return df
        df = CSVIO.reader(csv_file=csv_file)
        return df

    def dump_fund_gongmu_changneijiaoyijijinlishishuju(self, fund="511280"):
        csv_path = os.path.join(self.data_dir, 'fund/gongmu/details/changneijiaoyijijin')
        if not os.path.exists(csv_path):
            os.makedirs(csv_path)
        csv_file = os.path.join(csv_path, f'{fund}.csv')
        if os.path.exists(csv_file):
            print(f'loading from exist file ......')
            df = self.load_fund_gongmu_changneijiaoyijijinlishishuju(fund=fund)
        else:
            df = self.fund_data.fund_gongmu_changneijiaoyijijinlishishuju(fund=fund)
        CSVIO.writer(df, csv_file=csv_file, append=False)
        return df

    def load_fund_gongmu_changneijiaoyijijinlishishuju(self, fund="511280"):
        csv_file = os.path.join(self.data_dir, f'fund/gongmu/details/changneijiaoyijijin/{fund}.csv')
        if not os.path.exists(csv_file):
            print(f'downloading ......')
            df = self.dump_fund_gongmu_changneijiaoyijijinshishishuju(fund=fund)
            return df
        df = CSVIO.reader(csv_file=csv_file)
        return df

    def dump_fund_gongmu_kaifangshijijinpaihang(self):
        csv_path = os.path.join(self.data_dir, 'fund/gongmu/details/jijinpaihang')
        if not os.path.exists(csv_path):
            os.makedirs(csv_path)
        csv_file = os.path.join(csv_path, f'kaifangshijijinpaihang.csv')
        if os.path.exists(csv_file):
            print(f'loading from exist file ......')
            df = self.load_fund_gongmu_kaifangshijijinpaihang()
        else:
            df = self.fund_data.fund_gongmu_kaifangshijijinpaihang()
        CSVIO.writer(df, csv_file=csv_file, append=False)
        return df

    def load_fund_gongmu_kaifangshijijinpaihang(self):
        csv_file = os.path.join(self.data_dir, f'fund/gongmu/details/jijinpaihang/kaifangshijijinpaihang.csv')
        if not os.path.exists(csv_file):
            print(f'downloading ......')
            df = self.dump_fund_gongmu_kaifangshijijinpaihang()
            return df
        df = CSVIO.reader(csv_file=csv_file)
        return df

    def dump_fund_gongmu_changneijijinpaihang(self):
        csv_path = os.path.join(self.data_dir, 'fund/gongmu/details/jijinpaihang')
        if not os.path.exists(csv_path):
            os.makedirs(csv_path)
        csv_file = os.path.join(csv_path, f'changneijijinpaihang.csv')
        if os.path.exists(csv_file):
            print(f'loading from exist file ......')
            df = self.load_fund_gongmu_changneijijinpaihang()
        else:
            df = self.fund_data.fund_gongmu_changneijijinpaihang()
        CSVIO.writer(df, csv_file=csv_file, append=False)
        return df

    def load_fund_gongmu_changneijijinpaihang(self):
        csv_file = os.path.join(self.data_dir, f'fund/gongmu/details/jijinpaihang/changneijijinpaihang.csv')
        if not os.path.exists(csv_file):
            print(f'downloading ......')
            df = self.dump_fund_gongmu_changneijijinpaihang()
            return df
        df = CSVIO.reader(csv_file=csv_file)
        return df

    def dump_fund_gongmu_huobijijinpaihang(self):
        csv_path = os.path.join(self.data_dir, 'fund/gongmu/details/jijinpaihang')
        if not os.path.exists(csv_path):
            os.makedirs(csv_path)
        csv_file = os.path.join(csv_path, f'huobijijinpaihang.csv')
        if os.path.exists(csv_file):
            print(f'loading from exist file ......')
            df = self.load_fund_gongmu_huobijijinpaihang()
        else:
            df = self.fund_data.fund_gongmu_huobijijinpaihang()
        CSVIO.writer(df, csv_file=csv_file, append=False)
        return df

    def load_fund_gongmu_huobijijinpaihang(self):
        csv_file = os.path.join(self.data_dir, f'fund/gongmu/details/jijinpaihang/huobijijinpaihang.csv')
        if not os.path.exists(csv_file):
            print(f'downloading ......')
            df = self.dump_fund_gongmu_huobijijinpaihang()
            return df
        df = CSVIO.reader(csv_file=csv_file)
        return df

    def dump_fund_gongmu_jingzhigusuan(self):
        csv_path = os.path.join(self.data_dir, 'fund/gongmu/details/jingzhigusuan')
        if not os.path.exists(csv_path):
            os.makedirs(csv_path)
        csv_file = os.path.join(csv_path, f'jingzhigusuan.csv')
        if os.path.exists(csv_file):
            print(f'loading from exist file ......')
            df = self.load_fund_gongmu_jingzhigusuan()
        else:
            df = self.fund_data.fund_gongmu_jingzhigusuan()
        CSVIO.writer(df, csv_file=csv_file, append=False)
        return df

    def load_fund_gongmu_jingzhigusuan(self):
        csv_file = os.path.join(self.data_dir, f'fund/gongmu/details/jingzhigusuan/jingzhigusuan.csv')
        if not os.path.exists(csv_file):
            print(f'downloading ......')
            df = self.dump_fund_gongmu_jingzhigusuan()
            return df
        df = CSVIO.reader(csv_file=csv_file)
        return df

    def dump_fund_gongmu_jijinhangqing(self, symbol="sz159996"):
        csv_path = os.path.join(self.data_dir, f'fund/gongmu/details/jijinhangqing')
        if not os.path.exists(csv_path):
            os.makedirs(csv_path)
        csv_file = os.path.join(csv_path, f'{symbol}.csv')
        if os.path.exists(csv_file):
            print(f'loading from exist file ......')
            df = self.load_fund_gongmu_jijinhangqing()
        else:
            df = self.fund_data.fund_gongmu_jijinhangqing(symbol=symbol)
        CSVIO.writer(df, csv_file=csv_file, append=False)
        return df

    def load_fund_gongmu_jijinhangqing(self, symbol="sz159996"):
        csv_file = os.path.join(self.data_dir, f'fund/gongmu/details/jijinhangqing/{symbol}.csv')
        if not os.path.exists(csv_file):
            print(f'downloading ......')
            df = self.dump_fund_gongmu_jijinhangqing()
            return df
        df = CSVIO.reader(csv_file=csv_file)
        return df

    def dump_fund_gongmu_jijinhangqing(self, symbol="sz159996"):
        csv_path = os.path.join(self.data_dir, f'fund/gongmu/details/jijinhangqing')
        if not os.path.exists(csv_path):
            os.makedirs(csv_path)
        csv_file = os.path.join(csv_path, f'{symbol}.csv')
        if os.path.exists(csv_file):
            print(f'loading from exist file ......')
            df = self.load_fund_gongmu_jijinhangqing()
        else:
            df = self.fund_data.fund_gongmu_jijinhangqing(symbol=symbol)
        CSVIO.writer(df, csv_file=csv_file, append=False)
        return df

    def load_fund_gongmu_jijinhangqing(self, symbol="sz159996"):
        csv_file = os.path.join(self.data_dir, f'fund/gongmu/details/jijinhangqing/{symbol}.csv')
        if not os.path.exists(csv_file):
            print(f'downloading ......')
            df = self.dump_fund_gongmu_jijinhangqing()
            return df
        df = CSVIO.reader(csv_file=csv_file)
        return df




    # 公募基金
    # =============================================================================


if __name__ == '__main__':

    data_dir = r'/data2/store/code/001/database/dbdata/funds'
    fund_downloader = AKShareFundDownloader(data_dir=data_dir)

    # df = fund_downloader.dump_fund_simu_congyerenyuanxinxi()
    # df = fund_downloader.load_fund_simu_congyerenyuanxinxi()
    # print(f'congyerenyuanxinxi: {df.values}')
    # print(f'='*80)

    # df = fund_downloader.dump_fund_simu_jijincongyerenyuanzigezhucexinxi()
    # df = fund_downloader.load_fund_simu_jijincongyerenyuanzigezhucexinxi()
    # print(f'jijincongyerenyuanzigezhucexinxi: {df.values}')
    # print(f'='*80)

    # df = fund_downloader.dump_fund_simu_jijinguanlirenzonghechaxun()
    # df = fund_downloader.load_fund_simu_jijinguanlirenzonghechaxun()
    # print(f'jijinguanlirenzonghechaxun: {df.values}')
    # print(f'='*80)

    # df = fund_downloader.dump_fund_simu_zhengquangongsisimujijinzigongsiguanlirenxinxigongshi()
    # df = fund_downloader.load_fund_simu_zhengquangongsisimujijinzigongsiguanlirenxinxigongshi()
    # print(f'zhengquangongsisimujijinzigongsiguanlirenxinxigongshi: {df.values}')
    # print(f'='*80)

    # df = fund_downloader.dump_fund_simu_jijinguanlirenjijinchanpin()
    # df = fund_downloader.load_fund_simu_jijinguanlirenjijinchanpin()
    # print(f'jijinguanlirenjijinchanpin: {df.values}')
    # print(f'='*80)

    # df = fund_downloader.dump_fund_simu_zhengquangongsijiheziguanchanpingongshi()
    # df = fund_downloader.load_fund_simu_zhengquangongsijiheziguanchanpingongshi()
    # print(f'zhengquangongsijiheziguanchanpingongshi: {df.values}')
    # print(f'='*80)

    # df = fund_downloader.dump_fund_simu_zhengquangongsizhitoujijin()
    # df = fund_downloader.load_fund_simu_zhengquangongsijiheziguanchanpingongshi()
    # print(f'zhengquangongsizhitoujijin: {df.values}')
    # print(f'='*80)

    # df = fund_downloader.dump_fund_simu_zhengquangongsisimutouzijijin()
    # df = fund_downloader.load_fund_simu_zhengquangongsisimutouzijijin()
    # print(f'zhengquangongsisimutouzijijin: {df.values}')
    # print(f'='*80)

    # df = fund_downloader.dump_fund_simu_jijingongsijizigongsijiheziguanchapingongshi()
    # df = fund_downloader.load_fund_simu_jijingongsijizigongsijiheziguanchapingongshi()
    # print(f'jijingongsijizisongsijiheziguanchapingongshi: {df.values}')
    # print(f'='*80)

    # df = fund_downloader.dump_fund_simu_zichanzhichizhuanxiangjihua()
    # df = fund_downloader.load_fund_simu_zichanzhichizhuanxiangjihua()
    # print(f'load_fund_simu_zichanzhichizhuanxiangjihua: {df.values}')
    # print(f'='*80)

    # df = fund_downloader.dump_fund_simu_qihuogongsijiheziguanchanpingongshi()
    # df = fund_downloader.load_fund_simu_qihuogongsijiheziguanchanpingongshi()
    # print(f'load_fund_simu_zichanzhichizhuanxiangjihua: {df.values}')
    # print(f'='*80)

    # df = fund_downloader.dump_fund_simu_yizhuxiaosimujijinguanlirenmingdan()
    # df = fund_downloader.load_fund_simu_yizhuxiaosimujijinguanlirenmingdan()
    # print(f'yizhuxiaosimujijinguanlirenmingdan: {df.values}')
    # print(f'='*80)

    # df = fund_downloader.dump_fund_gongmu_jijinjibenxinxi()
    # df = fund_downloader.load_fund_gongmu_jijinjibenxinxi()
    # print(f'load_fund_gongmu_jijinjibenxinxi: {df.values}')
    # print(f'='*80)

    # df = fund_downloader.dump_fund_gongmu_kaifangjijinshishishuju()
    # df = fund_downloader.load_fund_gongmu_kaifangjijinshishishuju()
    # print(f'load_fund_gongmu_kaifangjijinshishishuju: {df.values}')
    # print(f'='*80)

    # df = fund_downloader.dump_fund_gongmu_kaifangjijinlishishuju()
    # df = fund_downloader.load_fund_gongmu_kaifangjijinlishishuju()
    # print(f'load_fund_gongmu_kaifangjijinlishishuju: {df.values}')
    # print(f'='*80)

    # df = fund_downloader.dump_fund_gongmu_huobijijinshishishuju()
    # df = fund_downloader.load_fund_gongmu_huobijijinshishishuju()
    # print(f'load_fund_gongmu_huobijijinshishishuju: {df.values}')
    # print(f'='*80)

    # df = fund_downloader.dump_fund_gongmu_huobijijinlishishuju()
    # df = fund_downloader.load_fund_gongmu_huobijijinlishishuju()
    # print(f'load_fund_gongmu_huobijijinlishishuju: {df.values}')
    # print(f'='*80)

    # df = fund_downloader.dump_fund_gongmu_licaijijinshishishuju()
    # df = fund_downloader.load_fund_gongmu_licaijijinshishishuju()
    # print(f'load_fund_gongmu_licaijijinshishishuju: {df.values}')
    # print(f'='*80)

    # df = fund_downloader.dump_fund_gongmu_licaijijinlishishuju()
    # df = fund_downloader.load_fund_gongmu_licaijijinlishishuju()
    # print(f'load_fund_gongmu_licaijijinlishishuju: {df.values}')
    # print(f'='*80)

    # df = fund_downloader.dump_fund_gongmu_fenjijijinshishishuju()
    # df = fund_downloader.load_fund_gongmu_fenjijijinshishishuju()
    # print(f'load_fund_gongmu_fenjijijinshishishuju: {df.values}')
    # print(f'='*80)

    # df = fund_downloader.dump_fund_gongmu_fenjijijinlishishuju()
    # df = fund_downloader.load_fund_gongmu_fenjijijinlishishuju()
    # print(f'load_fund_gongmu_fenjijijinlishishuju: {df.values}')
    # print(f'='*80)

    # df = fund_downloader.dump_fund_gongmu_changneijiaoyijijinshishishuju()
    # df = fund_downloader.load_fund_gongmu_changneijiaoyijijinshishishuju()
    # print(f'load_fund_gongmu_changneijiaoyijijinshishishuju: {df.values}')
    # print(f'='*80)

    # df = fund_downloader.dump_fund_gongmu_changneijiaoyijijinlishishuju()
    # df = fund_downloader.load_fund_gongmu_changneijiaoyijijinlishishuju()
    # print(f'load_fund_gongmu_changneijiaoyijijinlishishuju: {df.values}')
    # print(f'='*80)

    # df = fund_downloader.dump_fund_gongmu_kaifangshijijinpaihang()
    # df = fund_downloader.load_fund_gongmu_kaifangshijijinpaihang()
    # print(f'load_fund_gongmu_kaifangshijijinpaihang: {df.values}')
    # print(f'='*80)

    # df = fund_downloader.dump_fund_gongmu_changneijijinpaihang()
    # df = fund_downloader.load_fund_gongmu_changneijijinpaihang()
    # print(f'load_fund_gongmu_changneijijinpaihang: {df.values}')
    # print(f'='*80)

    # df = fund_downloader.dump_fund_gongmu_huobijijinpaihang()
    # df = fund_downloader.load_fund_gongmu_huobijijinpaihang()
    # print(f'huobijijinpaihang: {df.values}')
    # print(f'='*80)

    df = fund_downloader.dump_fund_gongmu_jingzhigusuan()
    df = fund_downloader.load_fund_gongmu_jingzhigusuan()
    print(f'load_fund_gongmu_jingzhigusuan: {df.values}')
    print(f'='*80)

    # df = fund_downloader.dump_fund_gongmu_jijinhangqing()
    # df = fund_downloader.load_fund_gongmu_jijinhangqing()
    # print(f'load_fund_gongmu_jijinhangqing: {df.values}')
    # print(f'='*80)

    # df = fund_downloader.dump_fund_gongmu_jijinhangqing()
    # df = fund_downloader.load_fund_gongmu_jijinhangqing()
    # print(f'load_fund_gongmu_jijinhangqing: {df.values}')
    # print(f'='*80)