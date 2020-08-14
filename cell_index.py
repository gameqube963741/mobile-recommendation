import os
import pandas as pd

fileName = os.listdir('/Users/edward/Desktop/CELL/cell_Index')
df = pd.DataFrame()
n = -1
for i in fileName:

    with open('/Users/edward/Desktop/CELL/cell_Index/' + i, 'r', encoding='utf-8-sig') as f:

        x = f.read()
        s = x.split('\n')
        for sen in s:
            n += 1
            cell = sen.replace('[\'', '')
            cell = cell.split('\', \'')[0]
            print(n)
            print(cell)

            # dataframe
            df2 = pd.DataFrame([[n, cell]], columns=['Id', 'Name'])
            df = df.append(df2, ignore_index=True)

#print(df)
df.to_csv('C:/Users/Big data/PycharmProjects/CELL/cell_Index/cell_Index.csv', encoding='utf_8_sig')