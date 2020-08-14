# mobile-recommendation-system
# 手機推薦系統：
# 目的：
利用爬蟲將各大論壇的手機頻論進行輿論分析，建立模型，利用使用者愛好進行篩選手機型號，並作推薦

# 方法：
        資料爬取：巴哈姆特、mobile01、eprice、Dcard、PTT、DCFever
        資料倉儲：Hadoop HDFS、mongo DB
        資料清洗：jieba、中研院CKIP
                1.分數轉向量
                2.斷字斷詞
                3.字頻計算、關鍵字依功能性貼標
                4.SnowNLP:
                        訓練SnowNLP
                        SnowNLP視覺化
        K-means演算法建模
        雲端架構：Google GCP
        Spark自動化：自動執行每日爬取的資料處理
        LineBOT:客戶端操作，並呈現結果
