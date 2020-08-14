import numpy as np
import pandas as pd
from snownlp import sentiment, SnowNLP
import os

dict = {
    '相機': ['拍照', '相機', '鏡頭', '照片', '照相', '畫素', '鏡頭', '影片', '自拍', '主相機', '拍攝', '夜景', '雙鏡頭', '手震', '錄影'],
    '續航力': ['電池', '充電', '續航', '續航力', '省電', '電力'],
    '遊戲': ['遊戲'],
    '價格': ['價格', '預算', '免費', '價錢', '降價', '價位'],
    '效能': ['系統', '軟體', '效能', '處理器', '速度', '處理器', '核心', '順暢', '晶片', '硬體'],
    '音樂': ['音樂', '音量', '音效'],
    '容量': ['容量', '記憶體', '空間', '儲存'],
    '外觀': ['外觀', '顏色', '尺寸', '金屬'],
    '解析度': ['解析度', '亮度', '色彩', '螢幕', '畫質']
}

dict2 = {
    '相機': 0,
    '續航力': 1,
    '遊戲': 2,
    '價格': 3,
    '效能': 4,
    '音樂': 5,
    '容量': 6,
    '外觀': 7,
    '解析度': 8,
}




brand = os.listdir('C:/Users/Big data/Desktop/Project/csvByPhone/')

for b in brand:
    path ='C:/Users/Big data/Desktop/Project/csvByPhone/' + b + '/content/'
    fileName = os.listdir(path)


    for fn in fileName:
        #print(fn)
        df = pd.DataFrame()
        x = pd.read_csv(path + fn, encoding='utf-8-sig', names=['Title', 'Date', 'Content'])
        mat = np.array([9, 9, 9, 9, 9, 9, 9, 9, 9])

        # search each article
        for n, i in enumerate(x.Content):
            #print(n)
            mat1 = np.array([0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5])
            for j in dict.values():
                for k in j:
                    try:
                        if i.find(k) != -1:
                            #search for dictionary values and print out its keys
                            for title, similar in dict.items():
                                for s in similar:
                                    if s == k:
                                        #print(title)
                                        s = SnowNLP(i)
                                        mat1[dict2[title]] = s.sentiments

                    except AttributeError:
                        pass

            #append the array of each article
            if n == 0:
                mat = np.append([mat], [mat1], axis=0)
            else:
                mat = np.append(mat, [mat1], axis=0)

        mat = mat[1:]       # delete the first column with 9s
        #print(mat)
        #print(mat.shape)
        mat_mean = np.mean(mat, axis=0)
        #print(mat_mean)


        name = str(fn).split('-c')[0].split('\']')[0]
        print(name)

        # ID
        p = pd.read_csv('C:/Users/Big data/PycharmProjects/CELL/cell_Index/cell_Index.csv', encoding='ANSI')
        # 以name取出id
        id = p[p['Name']==name]['Id'].iloc[0]
        print(id)


        # price
        status = pd.read_csv('C:/Users/Big data/PycharmProjects/CELL/cell_Index/status_Index.csv', encoding='ANSI', sep='\t')
        price = status[status['id']==id]['status'].iloc[0]


        if price<3251:
            x10=0.1
        elif price<6501:
            x10 = 0.2
        elif price<9751:
            x10 = 0.3
        elif price<13001:
            x10 = 0.4
        elif price<16251:
            x10 = 0.5
        elif price<19501:
            x10 = 0.6
        elif price<22751:
            x10 = 0.7
        elif price<26001:
            x10 = 0.8
        elif price<29251:
            x10 = 0.9
        else:
            x10 = 1

    
    
    
        # save to npy
        mat_mean = np.hstack((mat_mean, x10, id))
        print(mat_mean)
        name = name.replace(' ', '_')
        np.save('C:/Users/Big data/PycharmProjects/CELL/matrix/npy/' + name, mat_mean)
    
    
        # save to dataframe
        df2 = {"ID": id, "Matrix": mat_mean, "Price": x10}
        #print(df2)
        df = df.append(df2, ignore_index=True)
        #print(df)
        name = name.replace(' ', '_')
        df.to_csv('C:/Users/Big data/PycharmProjects/CELL/matrix/csv/' + name + '.csv')
