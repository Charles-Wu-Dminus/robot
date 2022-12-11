import jieba 

# 定義要分詞的文本
text = "我是一個中文分詞的測試"

# 使用 jieba 對文本進行分詞
seg_list = list(jieba.cut(text))

# 輸出分詞結果
print(seg_list)

