#!/usr/bin/env python

import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties

myfont=FontProperties(fname=r"/Users/edward/Library/Fonts/MSJH.ttc", size=14)

mat = np.load('/Users/edward/Desktop/CELL/algorithm/k_means/km.npy')
#print(mat[:,-1])
data = mat[:,:-2]
#print(data)

# 相機
x1 = mat[:,0]
sns.set(font=myfont.get_name())
sns.distplot(x1).set_title('相機')
plt.show()

# 續航力
x2 = mat[:,1]
sns.distplot(x2).set_title('續航力')
plt.show()

# 遊戲
x3 = mat[:,2]
sns.distplot(x3).set_title('遊戲')
plt.show()

# 價格
x4 = mat[:,3]
sns.distplot(x4).set_title('價格')
plt.show()

# 效能
x5 = mat[:,4]
sns.distplot(x5).set_title('效能')
plt.show()

# 音樂
x6 = mat[:,5]
sns.distplot(x6).set_title('音樂')
plt.show()

# 容量
x7 = mat[:,6]
sns.distplot(x7).set_title('容量')
plt.show()

# 外觀
x8 = mat[:,7]
sns.distplot(x8).set_title('外觀')
plt.show()

# 解析度
x9 = mat[:,8]
sns.distplot(x9).set_title('解析度')
plt.show()

# 真正的價錢
x10 = mat[:,9]
sns.distplot(x10).set_title('真正的價錢')
plt.show()