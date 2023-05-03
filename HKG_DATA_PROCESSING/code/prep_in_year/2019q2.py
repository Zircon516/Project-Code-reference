import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import os
from BasicPrep import AirPortData
from HelperFunction import if_button

df2019q2 = pd.read_csv('C:/Shared/LMWData/y2019q2.csv', low_memory=False)

df_test_2019q2_r1 = AirPortData(df2019q2)
df_r1 = df_test_2019q2_r1.add_if_btn()

df_test_2019q2_r2 = AirPortData(df_r1)
df_r2 = df_test_2019q2_r2.add_cov_id()

df_test_2019q2_r3 = AirPortData(df_r2)
df_r3 = df_test_2019q2_r3.add_conv_num_before()

df_test_2019q2_r4 = AirPortData(df_r3)
df_r4 = df_test_2019q2_r4.drop_welc()

df_test_2019q2_r5 = AirPortData(df_r4)
df_r5 = df_test_2019q2_r5.drop_flight()

df_test_2019q2_r6 = AirPortData(df_r5)
df_r6 = df_test_2019q2_r6.only_en()

df_test_2019q2_r7 = AirPortData(df_r6)
df_r7 = df_test_2019q2_r7.add_conv_num_after()

df_r7.to_excel('C:/Shared/LMWData/NewFormCSV/y2019q2n.xlsx')