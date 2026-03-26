# tools.py
import json
import os

def read_json(filepath):
    """读取 JSON 文件并返回 Python 对象"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def write_json(filepath, data):
    """将 Python 对象写入 JSON 文件（格式化缩进）"""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# 为了方便 OpenClaw 调用，我们也可以直接提供文件读写的简单函数
def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    return True