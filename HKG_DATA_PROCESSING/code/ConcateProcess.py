import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import os

data_folder = 'C:/Users/user2/Desktop/chatbot_data/'
data_list = set(os.listdir(data_folder))-set(['.DS_Store'])
data_list = list(data_list)
print(data_list)

from DataConcate import select_data,concate_data,save_to_xlsx

#concate 2018 data
lst2018 = select_data(data_list,'2018')
df2018 = concate_data(data_folder,lst2018)
df2018=df2018.drop(columns=['chat_datetime','record_uploaded_time'])
save_to_xlsx(df2018,'y2018')

#concate 2020 data
lst2020 = select_data(data_list,'2020')
df2020 = concate_data(data_folder,lst2020)
df2020=df2020.drop(columns=['chat_datetime','record_uploaded_time'])
save_to_xlsx(df2020,'y2020')

#concate 2021 data
lst2021 = select_data(data_list,'2021')
df2021 = concate_data(data_folder,lst2021)
df2021=df2021.drop(columns=['chat_datetime','record_uploaded_time'])
save_to_xlsx(df2021,'y2021')

#concate 2022 data
lst2022 = select_data(data_list,'2022')
df2022 = concate_data(data_folder,lst2022)
df2022=df2022.drop(columns=['chat_datetime','record_uploaded_time'])
save_to_xlsx(df2022,'y2022')

# for 2019, concate in season
lst2019 = select_data(data_list,'2019')
print(lst2019)

#concate q1
lst2019q1 = ['conversationlog20190101.parquet','conversationlog20190201.parquet','conversationlog20190301.parquet']
df2019q1 = concate_data(data_folder,lst2019q1)
df2019q1=df2019q1.drop(columns=['chat_datetime','record_uploaded_time'])
save_to_xlsx(df2019q1,'y2019q1')

#concate q2
lst2019q2 = ['conversationlog20190401.parquet','conversationlog20190501.parquet','conversationlog20190601.parquet']
df2019q2 = concate_data(data_folder,lst2019q2)
df2019q2=df2019q2.drop(columns=['chat_datetime','record_uploaded_time'])
save_to_xlsx(df2019q2,'y2019q2')

#concate q3
lst2019q3 = ['conversationlog20190701.parquet','conversationlog20190801.parquet','conversationlog20190901.parquet']
df2019q3 = concate_data(data_folder,lst2019q3)
df2019q3=df2019q3.drop(columns=['chat_datetime','record_uploaded_time'])
save_to_xlsx(df2019q3,'y2019q3')

#concate q4
lst2019q4 = ['conversationlog20191001.parquet','conversationlog20191101.parquet','conversationlog20191201.parquet']
df2019q4 = concate_data(data_folder,lst2019q4)
df2019q4=df2019q4.drop(columns=['chat_datetime','record_uploaded_time'])
save_to_xlsx(df2019q4,'y2019q4')