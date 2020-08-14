from collections import Counter
import os

path = '/Users/edward/Desktop/CELL/words/apple/content/'
fileNames = os.listdir(path)

for fn in fileNames:
    with open(path + fn, 'r', encoding='utf-8-sig') as f:
        x = f.read()
        word = x.replace('[[[', '')
        word = word.replace(']]]', '')
        word = word.replace('\', \'', ', ')
        word = word[4:-4]           #delete [[[' & ']]]
        word = word.split(', ')
        #print(word)

        count = Counter(word)
        #print(count)
        #print(count.keys())
        #print(count.most_common())
        #print(count.most_common()[0][0])

        with open('/Users/edward/Desktop/CELL/stop.txt', 'r', encoding='utf-8-sig') as f:
            stop = f.read()
            for i in count.most_common():
                if i[0] not in stop and len(i[0])>1:
                    print(i)
                    f = open('/Users/edward/Desktop/CELL/count/count_%s.txt' % fn, 'a+', encoding='utf-8-sig')
                    f.write(str(i))
                    f.close()