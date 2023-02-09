import tensorflow as tf
from ctypes import *
from keras import Sequential
from keras.layers import Dense, LSTM, Dropout
import numpy as np
import matplotlib.pyplot as plt
from bloomberg import Analyzer

mk = Analyzer.MarketDB()
raw_df = mk.get_daily_price('삼성전자', )

model = Sequential()






# 이 파일 내에서만 실행되게 하고싶을때 
if __name__ == '__main__':
    pass
