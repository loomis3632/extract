# encoding: utf-8
"""
@author: baimianhuluwa
@time: 2020/4/22 15:11
@file: merge_txt.py
@desc: 
"""
import os
import chardet


def get_all_path(open_file_path):
    """
    获取当前目录以及子目录下所有的.txt文件，
    :param open_file_path:
    :return:
    """
    rootdir = open_file_path
    path_list = []
    list = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
    for i in range(0, len(list)):
        com_path = os.path.join(rootdir, list[i])
        if os.path.isfile(com_path) and com_path.endswith(".txt"):
            path_list.append(com_path)
        if os.path.isdir(com_path):
            path_list.extend(get_all_path(com_path))
    return path_list


def get_encoding(file):
    """
    # 获取文件编码类型
    :param file: 文件路径
    :return: 编码
    """
    # 二进制方式读取，获取字节数据,不必全部read，检测编码类型
    with open(file, 'rb') as f:
        data = f.read(1024)
        return chardet.detect(data)['encoding']


def merge_txt():
    res_txt = r'E:\dataset\基金代码_pro\merge1.txt'
    # rootdir = r'E:\dataset\test'  # 待处理的数据文件夹
    rootdir = r'E:\dataset\基金代码'  # 待处理的数据文件夹
    path_lists = get_all_path(rootdir)
    print(path_lists)
    count = 0
    for path in path_lists:
        count += 1
        print(count)
        coding = get_encoding(path)
        with open(path, 'r', encoding=coding, errors='ignore') as rf, open(res_txt, 'a', encoding='utf-8',
                                                                           errors='ignore') as wf:
            for line in rf:
                count += 1
                print(count)
                wf.write(line)


if __name__ == '__main__':
    merge_txt()
