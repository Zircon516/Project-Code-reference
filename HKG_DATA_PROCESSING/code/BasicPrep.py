from HelperFunction import if_button
import numpy as np
import pandas as pd
class AirPortData():
    # define some attributes
    def __init__(self, df):
        self.row_num = df.shape[0]
        self.col_num = df.shape[1]
        self.col_name = df.columns
        self.df = df
    # define some methods

    def add_if_btn(self):
        self.df['if_button'] = self.df['flowCategory'].apply(lambda x: if_button(x))
        return self.df

    def add_cov_id(self):
        lst = self.df['conversationId']
        rk = 1
        rk_lst = [1]
        for i in range(1, len(lst)):
            if lst[i] == lst[i-1]:
                pass
            else:
                rk += 1
            rk_lst.append(rk)
        gp_rk = np.array(rk_lst)
        self.df['conv_gp'] = gp_rk
        return self.df

    def add_conv_num_before(self):
        convnum_bf = self.df[['conversationId', 'id']].groupby(['conversationId']).count()
        convnum_bf =convnum_bf.rename(columns={'id': 'convnum_bf'})
        self.df = pd.merge(self.df, convnum_bf, on=['conversationId'], how='inner')
        return self.df

    def add_conv_num_after(self):
        convnum_aft = self.df[['conversationId', 'id']].groupby(['conversationId']).count()
        convnum_aft =convnum_aft.rename(columns={'id': 'convnum_aft'})
        self.df = pd.merge(self.df, convnum_aft, on=['conversationId'], how='inner')
        return self.df

    def only_en(self):
        self.df = self.df[self.df['lang'] == 'EN']
        return self.df

    def drop_flight(self):
        self.df = self.df.drop(self.df[self.df.flowCategory == 'flight'].index)
        self.df = self.df.drop(self.df[self.df.flowCategory == 'flight_btn'].index)
        return self.df


    def long_conv(self):
        self.df = self.df[self.df['convnum'] > 2]
        return self.df

    def drop_welc(self):
        self.df = self.df[(self.df['flowCategory'] != 'capability_btn')]
        self.df = self.df[(self.df['flowCategory'] != 'capability')]
        return self.df