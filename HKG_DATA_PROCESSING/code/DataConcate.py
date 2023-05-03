import pandas as pd
#定义data拼接函数：2018,2020,2021,2022

#筛选
def select_data(datalist,year):
    dst=[]
    for i in datalist:
        if year in i:
            dst.append(i)
    return dst

# 拼接数据
def concate_data(data_folder,dst):
    df_formal = pd.read_parquet(data_folder+dst[0])
    for i in dst[1:]:
        df = pd.read_parquet(data_folder+i)
        df_formal = pd.concat([df_formal, df])
    return df_formal

# save data to excel
def save_to_xlsx(dataframe,name):
    dataframe.to_csv('C:/Shared/LMWData/'+name+'.csv')



