# -*- coding: utf-8 -*-
"""
四则运算计算器 —— Python 入门学习项目

运行方式：在终端输入  py calculator.py

这个项目会带你学习以下 Python 基础知识：
  1. 变量与数据类型（int / float / str）
  2. 输入与输出（input / print / f-string 格式化）
  3. 函数的定义与调用（def、参数、返回值）
  4. 条件判断（if / elif / else）
  5. 循环（while）
  6. 异常处理（try / except / raise）
  7. 字典的高级用法（用字典代替 if-elif 分支）
"""

# ============ 第一部分：四则运算函数 ============
# 每个函数接收两个参数 a 和 b，用 return 返回计算结果


def add(a, b):
    """加法"""
    return a + b


def subtract(a, b):
    """减法"""
    return a - b


def multiply(a, b):
    """乘法"""
    return a * b


def divide(a, b):
    """除法：除数不能为 0，否则抛出异常"""
    if b == 0:
        # raise 用来主动抛出错误，程序会跳到调用方的 except 块
        raise ValueError("除数不能为 0！")
    return a / b


# ============ 第二部分：用字典代替大量 if-elif ============
# 字典的"值"可以是函数本身，这种用法叫"一等函数"
# OPERATIONS["+"](3, 5) 就等价于 add(3, 5)

OPERATIONS = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


# ============ 第三部分：安全地获取用户输入的数字 ============

def read_number(prompt):
    """反复提示用户输入，直到输入的是一个合法数字为止"""
    while True:
        text = input(prompt)
        try:
            # float() 尝试把字符串转成浮点数，比如 "3.14" -> 3.14
            return float(text)
        except ValueError:
            # 转换失败说明输入的不是数字（比如 "abc"）
            print(f"  「{text}」不是一个有效的数字，请重新输入！")


# ============ 第四部分：执行一次计算 ============

def calculate_once():
    """完成一次四则运算的完整流程"""
    print("\n可选择运算符：+  -  *  /")

    # 1. 获取运算符
    while True:
        op = input("请输入运算符：").strip()  # strip() 去掉首尾空格
        if op in OPERATIONS:
            break  # 合法运算符，跳出循环
        print(f"  「{op}」不是支持的运算符，请输入 + - * / 之一")

    # 2. 获取两个数字
    a = read_number("请输入第一个数字：")
    b = read_number("请输入第二个数字：")

    # 3. 从字典里取出对应的函数并调用
    try:
        result = OPERATIONS[op](a, b)
    except ValueError as error:
        # 捕获 divide 函数里 raise 出来的错误
        print(f"  计算出错：{error}")
        return  # 结束本次计算，回到主循环

    # 4. 展示结果
    # :g 表示用"紧凑"格式显示数字，4.0 会显示成 4，3.14 保持 3.14
    print(f"\n  结果：{a:g} {op} {b:g} = {result:g}")


# ============ 第五部分：程序入口 ============

def main():
    print("=" * 30)
    print("      Python 四则运算计算器")
    print("=" * 30)

    # while True 是无限循环，配合 break 或 return 退出
    while True:
        calculate_once()

        # 继续还是退出？
        choice = input("\n继续计算吗？(y 继续 / 其他键退出)：").strip().lower()
        if choice != "y":
            print("感谢使用，再见！")
            break


# 只有"直接运行"本文件时，下面的代码才会执行
# （被别的文件 import 时不会执行，这是 Python 的常见惯例）
if __name__ == "__main__":
    main()
