# 导入所需的库和模块
from wordcloud import WordCloud  # 用于生成词云的主要库
from PIL import Image  # Python图像处理库，用于加载图像
import numpy as np  # 数值计算库，用于将图像转换为数组
import matplotlib.pyplot as plt  # 绘图库，用于显示词云
import jieba  # 中文分词库
from pathlib import Path  # 路径处理库，用于处理文件路径
import traceback  # 异常处理库，用于打印详细的错误信息
from typing import Set, Optional  # 类型注解支持，用于指定函数参数和返回值的类型

# 全局常量定义
# 停用词集合：这些词在生成词云时会被过滤掉，不会显示
STOPWORDS: Set[str] = {
    "全面", "主题", "大会", "初心", "使命", "目标", "发展", "我国", "平凡", "全会",
    "建设", "改革", "重要", "重大", "局面", "掌声", "基本", "必须", "理论", "完善",
    "实现", "系统", "注重", "坚持"
}

# 默认字体路径（Windows系统）
# 指定生成词云时使用的字体文件路径
DEFAULT_FONT_PATH = Path("C:/Windows/Fonts/msyh.ttc")

# 函数定义：读取文本文件
def read_text_file(file_path: Path) -> str:
    """
    读取文本文件内容
    
    Args:
        file_path: 文本文件路径
        
    Returns:
        str: 文件内容字符串
        
    Raises:
        FileNotFoundError: 当文件不存在时
        ValueError: 当文件内容为空时
        Exception: 其他读取错误
    """
    try:
        # 打开文件并读取内容
        # 'with'语句确保文件在使用后正确关闭
        # encoding="utf-8"确保正确处理中文文本
        with open(file_path, encoding="utf-8") as f:
            content = f.read()  # 读取文件的全部内容
        
        # 检查文件内容是否为空或只包含空白字符
        if not content.strip():
            # 如果内容为空，抛出ValueError异常
            raise ValueError(f"文本文件 {file_path} 内容为空，请检查！")
        
        # 返回文件内容
        return content
    
    # 处理文件不存在的异常
    except FileNotFoundError:
        raise FileNotFoundError(f"找不到文件 {file_path}，请确认路径！")
    
    # 处理其他所有可能的异常
    except Exception as e:
        raise Exception(f"读取文件 {file_path} 失败：{str(e)}")

# 函数定义：中文分词
def tokenize_text(text: str) -> str:
    """
    对中文文本进行分词处理
    
    Args:
        text: 待分词的中文文本
        
    Returns:
        str: 以空格分隔的分词结果
    """
    # 使用jieba库进行中文分词
    # jieba.cut(text)返回一个生成器，包含分词结果
    # ' '.join()用空格将分词结果连接成一个字符串
    return ' '.join(jieba.cut(text))

# 函数定义：生成词云对象
def generate_wordcloud(text: str, mask_path: Path, stopwords: Set[str], 
                      font_path: Optional[Path] = None) -> WordCloud:
    """
    生成词云对象
    
    Args:
        text: 已分词的文本
        mask_path: 词云形状掩码图像路径
        stopwords: 停用词集合
        font_path: 字体文件路径，默认为None（使用系统默认字体）
        
    Returns:
        WordCloud: 生成的词云对象
        
    Raises:
        Exception: 生成词云过程中的任何错误
    """
    try:
        # 处理字体路径
        # 如果未提供字体路径，使用默认字体路径
        font_path = font_path or DEFAULT_FONT_PATH
        
        # 检查字体文件是否存在
        if not font_path.exists():
            raise FileNotFoundError(f"字体文件不存在: {font_path}")
        
        # 加载掩码图像
        # Image.open()打开图像文件
        # np.array()将图像转换为NumPy数组，WordCloud需要使用数组格式的掩码
        img = Image.open(mask_path)
        mask = np.array(img)
        
        # 创建WordCloud对象并生成词云
        return WordCloud(
            font_path=str(font_path),  # 指定字体文件路径
            mask=mask,  # 指定词云形状的掩码
            width=1200,  # 设置词云宽度
            height=900,  # 设置词云高度
            background_color='white',  # 设置背景颜色
            max_words=200,  # 设置最多显示的词数
            stopwords=stopwords  # 设置停用词
        ).generate(text)  # 根据文本生成词云
    
    # 处理生成词云过程中可能出现的异常
    except Exception as e:
        raise Exception(f"生成词云失败：{str(e)}")

# 函数定义：显示并保存词云图像
def display_and_save_wordcloud(wc: WordCloud, output_path: Path) -> None:
    """
    显示并保存词云图像
    
    Args:
        wc: 词云对象
        output_path: 输出图像文件路径
        
    Raises:
        Exception: 显示或保存过程中的任何错误
    """
    try:
        # 显示词云
        # plt.imshow()显示图像
        # interpolation='bilinear'设置插值方法，使图像显示更平滑
        plt.imshow(wc, interpolation='bilinear')
        
        # 隐藏坐标轴
        plt.axis("off")
        
        # 显示图像窗口
        plt.show()
        
        # 保存词云到文件
        wc.to_file(str(output_path))
        
        # 打印成功信息
        print(f"词云已成功保存到：{output_path}")
    
    # 处理显示或保存过程中可能出现的异常
    except Exception as e:
        # 使用traceback打印详细错误信息，包括调用栈
        traceback.print_exc()
        raise Exception(f"显示或保存词云失败：{str(e)}")

# 主程序入口
# 当直接运行此脚本时，以下代码块会被执行
# 如果此脚本被导入到其他脚本中，以下代码不会执行
if __name__ == "__main__":
    # 使用pathlib处理路径
    # Path(__file__).parent 获取当前脚本所在的目录
    base_dir = Path(__file__).parent
    
    # 定义数据文件目录
    data_dir = base_dir / "practice"  # 组合路径，创建子目录路径
    
    # 确保数据目录存在
    # 如果目录不存在，创建它（包括所有父目录）
    if not data_dir.exists():
        data_dir.mkdir(parents=True, exist_ok=True)
    
    # 定义文件路径
    text_path = data_dir / "ciyun1.txt"  # 文本文件路径
    mask_path = data_dir / "ciyun1.png"  # 掩码图像路径
    output_path = data_dir / "ciyun_result.png"  # 输出图像路径
    
    # 使用try-except块捕获和处理可能出现的异常
    try:
        # 读取文本内容
        content = read_text_file(text_path)
        
        # 中文分词
        tokenized_text = tokenize_text(content)
        
        # 生成词云
        wc = generate_wordcloud(
            tokenized_text,  # 分词后的文本
            mask_path,  # 掩码图像路径
            STOPWORDS  # 停用词集合
        )
        
        # 显示并保存词云
        display_and_save_wordcloud(wc, output_path)
    
    # 捕获和处理所有异常
    except Exception as e:
        # 打印详细错误信息，包括调用栈
        traceback.print_exc()
        # 打印简化的错误信息
        print(f"程序运行出错：{str(e)}")