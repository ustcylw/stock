#! /usr/bin/env python
# coding: utf-8
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import pandas as pd


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
