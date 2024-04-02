import json
import pandas as pd
import os
i=0


def df_maker(col_num, ind_num, fill):
    col = []
    ind = []
    con = []
    for i in range(0,col_num):
        col.append(fill)
    for i in range(0,ind_num):
        ind.append(fill)
    for i in range(0,ind_num):
        con.append(col)
    return pd.DataFrame(con, columns = col, index = ind)

df = df_maker(2,500,0)
df.columns = ["대사","라벨"]
while(1):
    i = i + 1
    i_str = str(i)
    if os.path.isfile(r"D:\015.감성 및 발화 스타일별 음성합성 데이터\01.데이터\1.Training\라벨링데이터\TL1\TL1\1.감정\3.분노\0001_G1A3E3S0C0_PSB\0001_G1A3E3S0C0_PSB_"+i_str.zfill(6)+".json"):
        with open(
                r"D:\015.감성 및 발화 스타일별 음성합성 데이터\01.데이터\1.Training\라벨링데이터\TL1\TL1\1.감정\3.분노\0001_G1A3E3S0C0_PSB\0001_G1A3E3S0C0_PSB_" + i_str.zfill(6) + ".json", encoding='UTF-8') as f:
            json_object = json.load(f)
    df.iloc[i-1] = [json_object["전사정보"]["OrgLabelText"],0]
    if(i==500):
        break

df.to_csv(r"D:\test\rating_train(분노).txt",sep = '\t',index = False)
