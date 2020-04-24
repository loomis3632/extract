# encoding: utf-8
"""
@author: baimianhuluwa
@time: 2020/4/22 10:43
@file: extract_fund_code.py
@desc: 
"""
import os
import chardet
import re


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


def extract_fund_code():
    # res_txt = r'E:\dataset\test_分析.txt'
    # rootdir = r'E:\dataset\test'  # 待处理的数据文件夹
    res_txt = r'E:\dataset\基金代码_res12.txt'
    rootdir = r'E:\dataset\基金代码_pro'  # 待处理的数据文件夹
    path_lists = get_all_path(rootdir)
    count = 0
    key_lists1 = ['国家自然学基金', '国家级自然科学', '国家自科科学', '国家自科学基金', '国家杰出青年基金', '国家自然学科', '国家科学基金', '国家青年基金', '国家自然科',
                  '国家青年自然基金', '国家自然科研', '国家杰出青年科学', '国家杰出青年科学', '国家重点自然科学', '国家自科基金', '国家自然青年科学', '国家青年自然科学',
                  '中国自然科学基金', '国家青年科学基金', '国家自然基金', '国家自然资', '国家基础科学', '国家自然科技基金', '国家科学自然', '国家基金', '国家自然青年基金']
    key_lists2 = ['NSF China', 'National Scientific foundation of China', 'NSF of P.R.China', 'NSFC', 'NSF of China',
                  'Nature Science Foundation of China', 'National Natural Scientific', 'NNSF',
                  'National Natural Science', 'National Nature Science', 'National Natural Foundation',
                  'Natural Science Foundation', 'National Science Foundation']

    for path in path_lists:
        coding = get_encoding(path)
        with open(path, 'r', encoding=coding, errors='ignore') as rf, open(res_txt, 'a', encoding='utf-8',
                                                                           errors='ignore') as wf:
            file_content = ""  # 要处理的文件内容
            file_content_flag = 0  # 文件内容找到标志词

            for line in rf:
                count += 1
                print(count)
                if file_content_flag == 0 and not line.startswith('<基金>='):  # file_content_flag =0 不需要处理的内容直接写入
                    wf.write(line)
                if line.startswith('<基金>='):
                    line = line.replace('<基金>=', '')
                    file_content_flag = 1

                if file_content_flag == 1 and ((not line.startswith('<REC>'))):
                    file_content = file_content + line

                if  file_content_flag == 1 and line.startswith('<REC>') :

                    file_content_split = file_content.strip().split(";;")
                    file_content_split = [e for e in file_content_split if len(e) >= 0]  # 去空

                    fund_code_lists = [] # 用于保存基金代码
                    remove_count = 0  # 用于记录不符合要求的基金。

                    for ele in file_content_split:
                        if any(key.lower() in ele.lower() for key in key_lists1):
                            res_lists = re.findall(r'[A-Za-z0-9]+', ele)
                            res_lists = list(set([e for e in res_lists if (len(e) >= 5 and not e.isalpha())]))
                            print(res_lists)
                            fund_code_lists.extend(res_lists)
                        elif any(key.lower() in ele.lower() for key in key_lists2):
                            res_lists = re.findall(r'[A-Za-z0-9]+', ele)
                            res_lists = list(set([e for e in res_lists if (len(e) >= 5 and not e.isalpha())]))
                            print(res_lists)
                            fund_code_lists.extend(res_lists)
                        else:
                            remove_count += 1

                    fund_code_res = ';'.join(fund_code_lists)

                    fund_code_res_ = '<国家自然科学基金>=' + str(fund_code_res)
                    print(fund_code_res_)
                    file_content_split_length = '<基金总数>=' + str(len(file_content_split))
                    print(file_content_split_length)
                    remove_count_res = '<基金移除数>=' + str(remove_count)
                    print(remove_count_res)
                    # wf.write(file_content + '\n' + str(
                    #     file_content_split) + '\n' + fucd_code_res + '\n' + remove_count_res + '\n')

                    wf.write(
                        fund_code_res_ + '\n' + file_content_split_length + '\n' + remove_count_res + '\n' + '<REC>' + '\n')

                    file_content = ""  # 重置要处理的文件内容
                    file_content_flag = 0  # 重置文件内容找到标志词


if __name__ == '__main__':
    extract_fund_code()
