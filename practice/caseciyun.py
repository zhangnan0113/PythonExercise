# 导入库
from wordcloud import WordCloud
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import jieba

# 打开文本（确保ciyun1.txt在同一目录，编码UTF-8）
try:
    with open("practice\ciyun1.txt", encoding="utf-8") as f:
        s = f.read()
    if not s.strip():
        raise ValueError("practice\ciyun1.txt文本为空,请检查内容")
except FileNotFoundError:
    print("错误:找不到practice\ciyun1.txt,请放在代码同一目录")
    exit()

# 中文分词
text = ' '.join(jieba.cut(s))

# 生成对象
img = Image.open("practice\ciyun1.png") # 打开遮罩图片
mask = np.array(img) #将图片转换为数组

stopwords = ["全面","主题","大会","初心","使命","目标","发展","我国","平凡","全会","建设","改革",
             "重要","重大","局面","掌声","基本","必须","理论","完善","实现","系统","注重","坚持"]
wc = WordCloud(font_path="C:/Windows/Fonts/msyh.ttc",  #msyh.ttc电脑本地字体，可以写成绝对路径
               mask=mask,
               width = 1200,
               height = 900,
               background_color='white',
               max_words=200,
               stopwords=stopwords).generate(text) # 加载词云文本

# 显示词云
plt.imshow(wc, interpolation='bilinear')# 用plt显示图片
plt.axis("off")  # 不显示坐标轴
plt.show() # 显示图片

# 保存到文件
wc.to_file("practice\ciyun_result.png")
print("词云已保存为practice\ciyun_result.png")