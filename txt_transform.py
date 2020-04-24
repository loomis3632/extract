# encoding: utf-8
"""
@author: baimianhuluwa
@time: 2020/4/23 15:59
@file: txt_transform.py
@desc: 
"""
import collections


def txt_transform():
    """
    把文本进行格式转换
    :return:
    """
    read_path = r"E:\dataset\test1\test1.txt"
    read_path = r"E:\dataset\基金代码_res2.txt"
    write_path = r"E:\dataset\基金代码_res2_.txt"
    with open(read_path, 'r', encoding="utf-8", errors='ignore') as rf, open(write_path, 'a', encoding='utf-8',
                                                                             errors='ignore') as wf:
        # 基金代码 基金代码重复个数 分类号 专题代码 文件名 年 篇名 基金总数 基金移除总数
        # -----------------------
        # <REC>
        # <篇名>=中国环境规制体制的反思――基于国际比较视角的分析
        # <年>=2014
        # <文件名>=GYJP201402011
        # <分类号>=X321
        # <专题代码>=B027;
        # <基金代码>=0001;F0;
        # <国家自然科学基金>=71303034
        # <基金总数>=3
        # <基金移除数>=2
        # <REC>
        file_content_flag = 0
        file_end_flag = 0
        article_name = ''  # 篇名
        date = ''  # 年
        file_name = ''  # 文件名
        class_num = ''  # 分类号
        subject_num = ''  # 专题号
        fund_num = ''  # 基金代码
        national_fund_num = ''  # 国家基金代码
        national_fund_total = ''  # 基金总数
        national_fund_rv_count = ''  # 移除基金数

        for line in rf:
            # print(line)
            # 得到文件名，并标记
            # if file_content_flag == 0 and line.startswith('<REC>'):
            #     file_content_flag = 1
            if line.startswith('<篇名>='):
                article_name = line[5:].strip()
            if line.startswith('<年>='):
                date = line[4:].strip()
            if line.startswith('<文件名>='):
                file_name = line[6:].strip()
            if line.startswith('<分类号>='):
                class_num = line[6:].strip()
            if line.startswith('<专题代码>='):
                subject_num = line[7:].strip()
            if line.startswith('<基金代码>='):
                fund_num = line[7:].strip()
            if line.startswith('<国家自然科学基金>='):
                national_fund_num = line[11:].strip()
            if line.startswith('<基金总数>='):
                national_fund_total = line[7:].strip()
            if line.startswith('<基金移除数>='):
                file_end_flag = 1
                national_fund_rv_count = line[8:].strip()
                # if file_content_flag == 1 and file_end_flag == 1:
                # print(article_name, date, file_name, national_fund_num, national_fund_rv_count)
                national_fund_num_split = national_fund_num.split(";")
                res = ""  # 记录处理结果，用于写入文件
                # 基金代码 基金代码重复个数 分类号 专题代码 文件名 年 篇名 基金总数 基金移除总数
                # if len(national_fund_num_split) > 1:
                #     pass
                for ele in national_fund_num_split:
                    res = "%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s" % (
                        res, ele, "\t", class_num, "\t", subject_num, "\t", file_name, "\t", date, "\t", article_name,
                        "\t",
                        str(national_fund_total), "\t", str(national_fund_rv_count), "\n")

                wf.write(res)
                print(res)

                file_content_flag = 0
                file_end_flag = 0
                article_name = ''  # 篇名
                date = ''  # 年
                file_name = ''  # 文件名
                class_num = ''  # 分类号
                subject_num = ''  # 专题号
                fund_num = ''  # 基金代码
                national_fund_num = ''  # 国家基金代码
                national_fund_total = ''  # 基金总数
                national_fund_rv_count = ''  # 移除基金数


def txt_process():
    """
    对格式转换后的进一步处理，此函数是统计基金代码数，并添加为第二个字段
    :return:
    """
    read_path = r"E:\dataset\test1\test1_res2.txt"
    write_path = r"E:\dataset\test1\test1_res2__.txt"
    read_path = r"E:\dataset\基金代码_res2_.txt"
    write_path = r"E:\dataset\基金代码_res2___.txt"
    fund_dict = collections.defaultdict(list)
    count = 0
    with open(read_path, 'r', encoding="utf-8", errors='ignore') as rf:
        for line in rf:
            count += 1
            print(count)
            national_fund_num = line.split('\t', 1)
            if len(national_fund_num) > 1:
                key = national_fund_num[0].strip()
                value = national_fund_num[1]
                fund_dict[key].append(value)

    with open(write_path, 'a', encoding='utf-8', errors='ignore') as wf:
        for k, v in fund_dict.items():
            v_length = len(v)
            res = ""
            for ele in v:
                res = "%s%s%s%s%s%s" % (res, k, "\t", v_length, "\t", "".join(ele))
            wf.write(res)


def test():
    read_path = r"E:\dataset\基金代码_res2__.txt"
    with open(read_path, 'r', encoding="utf-8", errors='ignore') as rf:
        for line in rf:
            print(line)
            line_split = line.split('\t')
            print(line_split)


if __name__ == '__main__':
    # txt_transform()
    txt_process()
    # test()
