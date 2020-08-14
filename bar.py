import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties

myfont=FontProperties(fname=r'/Users/edward/Library/Fonts/MSJH.ttc',size=14)

mat = np.load('/Users/edward/Desktop/CELL/algorithm/k_means/km.npy')
#print(mat[:,-1])
data = mat[:,:-2]
#print(data)

labels = ['相機', '續航力', '遊戲', '價格', '效能', '音樂', '容量', '外觀', '解析度']

for m, l in enumerate(labels):
    brands = ['Apple', 'Asus', 'Huawei', 'Oppo', 'Samsung', 'Sony']
    pos = []
    neg = []
    for b in brands:
        if b =='Apple':
            mat_brand = mat[12:22, m]
        elif b == 'Asus':
            mat_brand = mat[0:8, m]
        elif b == 'Huawei':
            mat_brand = mat[8:12, m]
        elif b == 'Oppo':
            mat_brand = mat[22:33, m]
        elif b == 'Samsung':
            mat_brand = mat[33:46, m]
        else:
            mat_brand = mat[46:50, m]

        p=0
        n=0
        for a in mat_brand:
            if a < 0.5:
                n += 1
            else:
                p += 1

            total = p + n


        p_ = p / total
        n_ = n / total

        pos.append(p_)
        neg.append(n_)

    #print(pos)
    #print(neg)

    x = np.arange(len(brands))  # the label locations
    width = 0.35  # the width of the bars

    brands = ['a', 'Apple', 'Asus', 'Huawei', 'Oppo', 'Samsung', 'Sony']
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, pos, width, label='Positive')
    rects2 = ax.bar(x + width/2, neg, width, label='Negative')
    ax.set_title(l, fontproperties=myfont)
    ax.set_xticklabels(brands)
    ax.legend()
    plt.show()





'''
# 相機
apple = mat[0:11, 0]
asus = mat[11:19, 0]
hua = mat[19:23, 0]
oppo = mat[23:34, 0]
sam = mat[34:51, 0]
sony = mat[51:55, 0]

sns.set(font=myfont.get_name())
sns.barplot(x="day", y="total_bill", hue="sex", data=x1).set_title('相機')
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

'''