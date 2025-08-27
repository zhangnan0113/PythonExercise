from wordcloud import WordCloud
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import jieba
from pathlib import Path

# 拆分函数：读取文本
def read_text_file(file_path):
    try:
        with open(file_path, encoding="utf-8") as f:
            content = f.read()
        if not content.strip():
            raise ValueError(f"文本文件 {file_path} 内容为空，请检查！")
        return content
    except FileNotFoundError:
        raise FileNotFoundError(f"找不到文件 {file_path}，请确认路径！")
    except Exception as e:
        raise Exception(f"读取文件 {file_path} 失败：{str(e)}")

# 拆分函数：中文分词
def tokenize_text(text):
    return ' '.join(jieba.cut(text))

# 拆分函数：生成词云对象
def generate_wordcloud(text, mask_path, stopwords):
    try:
        img = Image.open(mask_path)
        mask = np.array(img)
        return WordCloud(
            font_path="C:/Windows/Fonts/msyh.ttc",  
            mask=mask,
            width=1200,
            height=900,
            background_color='white',
            max_words=200,
            stopwords=stopwords
        ).generate(text)
    except Exception as e:
        raise Exception(f"生成词云失败：{str(e)}")

# 拆分函数：显示并保存词云
def display_and_save_wordcloud(wc, output_path):
    try:
        plt.imshow(wc, interpolation='bilinear')
        plt.axis("off")
        plt.show()
        wc.to_file(output_path)
        print(f"词云已成功保存到：{output_path}")
    except Exception as e:
        raise Exception(f"显示或保存词云失败：{str(e)}")

# 主程序入口（必加）
if __name__ == "__main__":
    # 用 pathlib 优化路径
    practice_dir = Path(__file__).parent / "D:\shuhan_project\PythonExercise\practice"
    text_path = practice_dir / "ciyun1.txt"
    mask_path = practice_dir / "ciyun1.png"
    output_path = practice_dir / "ciyun_result.png"

    try:
        content = read_text_file(text_path)
        tokenized_text = tokenize_text(content)
        wc = generate_wordcloud(tokenized_text, mask_path, stopwords=[
            "全面","主题","大会","初心","使命","目标","发展","我国","平凡","全会","建设","改革",
            "重要","重大","局面","掌声","基本","必须","理论","完善","实现","系统","注重","坚持"
        ])
        display_and_save_wordcloud(wc, output_path)
    except Exception as e:
        print(f"程序运行出错：{str(e)}")