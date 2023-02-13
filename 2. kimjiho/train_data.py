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

df = df_maker(2,50,0)
df.columns = ["대사","라벨"]
while(1):
    i = i + 1
    i_str = str(i)
    if os.path.isfile(r"D:\015.감성 및 발화 스타일별 음성합성 데이터\01.데이터\2.Validation\라벨링데이터\VL1\4.감정X발화스타일\9.상처X구연체\0047_G2A4E5S1C0_LSJ\0047_G2A4E5S1C0_LSJ_"+i_str.zfill(6)+".json"):
        with open(
                r"D:\015.감성 및 발화 스타일별 음성합성 데이터\01.데이터\2.Validation\라벨링데이터\VL1\4.감정X발화스타일\9.상처X구연체\0047_G2A4E5S1C0_LSJ\0047_G2A4E5S1C0_LSJ_" + i_str.zfill(6) + ".json", encoding='UTF-8') as f:
            json_object = json.load(f)
    df.iloc[i-1] = [json_object["전사정보"]["OrgLabelText"],0]
    if(i==50):
        break

df.to_csv(r"D:\test\rating_test(상처).txt",sep = '\t',index = False)
