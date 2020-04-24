# encoding: utf-8
"""
@author: baimianhuluwa
@time: 2020/4/24 13:16
@file: file_sort_pro.py
@desc: 
"""
import collections

r_file = r'E:\dataset\test1\test2.txt'
w_file = r'E:\dataset\test1\test2_sort.txt'
w_file2 = r'E:\dataset\test1\test2_sort_pro.txt'


def file_sort():
    """
    # 文件排序
    :return:
    """
    with open(r_file, 'r', encoding='utf-8', errors='ignore')as rf, \
            open(w_file, 'a', encoding='utf-8', errors='ignore')as wf:
        # ''.join(sorted(f1, key=lambda x: x.split('\t')[3], reverse=True))
        res = ''.join(sorted(rf, key=lambda x: x.split('\t', 1)[0], reverse=False))
        print(res)
        wf.write(res)


def file_sort_pro():
    """
    排序后，排序字段相同的值，作为要处理的文件块进行处理
    :return:
    71102009	4
    71102113	2
    71102113	3
    71303034	18
    71303034	18
    71303034	18

    """
    with open(w_file, 'r', encoding='utf-8', errors='ignore')as rf, \
            open(w_file2, 'a', encoding='utf-8', errors='ignore')as wf:
        temp_res = []
        flag_set = set()
        for line in rf:
            print(line)
            line_split = line.split('\t')
            code = line_split[0].strip()
            count = line_split[1]
            if len(line_split) > 1:
                if code in flag_set:
                    temp_res.append(line)
                if code not in flag_set:
                    flag_set.clear()
                    temp_res.clear()
                    flag_set.add(code)
                    temp_res.append(line)
                    print(code)
                    print(flag_set)

                else:
                    print("---------",temp_res)

                    temp_res = []
                    flag_set.clear()
            # if len(temp_res)>0:
            #     print(temp_res)
def file_sort_pro2():
    path = r'E:\dataset\test1\test2_sort.txt'
    with open(path, 'r', encoding='utf-8') as rf:
        res = []
        mail_set = set()
        print(rf)

        for ele in rf:
            ele_split = ele.split('\t')
            if len(ele_split) > 1:
                mail = ele_split[0].strip() #处理基础的字段
                if mail in mail_set:
                    res.append(mail)
                else:
                    # 防止首行未被处理
                    if len(mail_set) != 0:
                        print(res)
                        res = []
                        mail_set = set()

                    res.append(mail)
                    mail_set.add(mail)
        # 最后一行或者几行的处理
        if len(res) != 0:
            # 此处可以对进行邮箱相同的行进行处理。
            print(res)



if __name__ == '__main__':
    # file_sort()
    file_sort_pro2()
