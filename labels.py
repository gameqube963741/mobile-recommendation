import pandas as pd
from ckiptagger import data_utils, construct_dictionary, WS, POS, NER
import os
import tensorflow as tf

#path ='C:/Users/Big data/Desktop/Project/ptt_iphone6_content.csv'
savePath = '/Users/edward/Desktop/CELL/words/sony/'
path = '/Users/edward/Desktop/我的Desktop/專題/phoneproject/csvByPhone/sony/'

def labels(path, savePath):
    fileNames = os.listdir(path)
    for f in fileNames:
        x = pd.read_csv(path + f, encoding='utf-8-sig', names=['Title', 'Date', 'Content'])
        # print(x.Content)

        l = []
        for n, i in enumerate(x.Content):
            ws = WS("./data")
            # pos = POS("./data")
            # ner = NER("./data")
            try:
                ws_results = ws([i])
                print(n)
                print(ws_results)
                # save as different .txt
                l.append(ws_results)
            except TypeError:
                ws_results = ''
        f = open(savePath + f + '.txt', 'w', encoding='utf-8-sig')
        f.write(str(l))
        f.close()
labels(path, savePath)