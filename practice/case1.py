# 先定义函数（必须在调用前）
def func():
    # 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
    digits = [1, 2, 3, 4]
    nums = []
    for a in digits:
        for b in digits:
            if b == a:
                continue
            for c in digits:
                if c == a or c == b:
                    continue
                nums.append(a * 100 + b * 10 + c)
    print(f"共有 {len(nums)} 个三位数：")
    print(", ".join(map(str, nums)))

# 主程序入口（函数调用在定义之后）
if __name__ == '__main__':
    print('This is the main program of case1.py')
    func()  # 现在调用时，func() 已经被定义过了
    
    # 以下是被注释的备用逻辑（保持正确缩进作为注释）
    '''
    print('能组成的互不相同且无重复数字的三位数有：')
    count = 0  
    # 有四个数字：1、2、3、4
    # 能组成多少个互不相同且无重复数字的三位数？
    # 各是多少？
    for bai in range(1,5):
        for shi in range(1,5):
            if shi == bai:
                continue
            for ge in range(1,5):
                if ge != bai and ge != shi:
                    number = bai*100 + shi*10 + ge
                    print(number,end=' ')
                    count += 1
    print(f'\n总共有{count}个符合条件的三位数')
    '''