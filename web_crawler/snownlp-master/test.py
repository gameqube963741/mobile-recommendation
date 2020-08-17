# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals

text = '''
漢皇重色思傾國，御宇多年求不得。楊家有女初長成，養在深閨人未識。天生麗質難自棄，一朝選在君王側。回眸一笑百媚生，六宮粉黛無顏色。春寒賜浴華清池，溫泉水滑洗凝脂。侍兒扶起嬌無力，始是新承恩澤時。雲鬢花顏金步搖，芙蓉帳暖度春宵。春宵苦短日高起，從此君王不早朝承歡侍宴無閒暇，春從春遊夜專夜。後宮佳麗三千人，三千寵愛在一身。金屋妝成嬌侍夜，玉樓宴罷醉和春。姊妹弟兄皆列土，可憐光彩生門戶。遂令天下父母心，不重生男重生女。驪宮高處入青雲，仙樂風飄處處聞。緩歌慢舞凝絲竹，盡日君王看不足。漁陽鼙鼓動地來，驚破霓裳羽衣曲。
'''


from snownlp import normal
from snownlp import seg
from snownlp.summary import textrank


if __name__ == '__main__':
    t = normal.zh2hans(text)
    sents = normal.get_sentences(t)
    doc = []
    for sent in sents:
        words = seg.seg(sent)
        words = normal.filter_stop(words)
        doc.append(words)
    rank = textrank.TextRank(doc)
    rank.solve()
    for index in rank.top_index(5):
        print(sents[index])
    keyword_rank = textrank.KeywordTextRank(doc)
    keyword_rank.solve()
    for w in keyword_rank.top_index(5):
        print(w)