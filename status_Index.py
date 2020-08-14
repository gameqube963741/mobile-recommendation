import os
import json
import pandas as pd

path = 'C:/Users/Big data/Desktop/Project/all_model_detail/'

df = pd.DataFrame()
fileName = os.listdir(path)
for f in fileName:
    with open(path + f, 'r', encoding='utf-8-sig') as f:
        x = json.load(f)
        y = pd.DataFrame()

        # status
        if x['price1'] == '已下市' or x['price1'] == '無報價':
            pass
        else:
            y['name'] = [x['name']]
            y['status'] = str(x['price1']).split('\">$')[1].split('</a>')[0]

        # dataframe
        df2 = pd.DataFrame(y)
        print(df2)
        df = df.append(df2, ignore_index=True)

df.to_csv('C:/Users/Big data/PycharmProjects/CELL/cell_Index/status_Index.csv', encoding='utf_8_sig')