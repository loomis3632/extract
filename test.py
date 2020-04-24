# encoding: utf-8
"""
@author: baimianhuluwa
@time: 2020/4/22 11:42
@file: test.py
@desc: 
"""
#从字符串中提取字母字符串
import re
st = " (Grant Nos.61320106003,61222102,61201171)China(No.91124002,61372191,61472433,61202362,11301302)hello,world!!%[545]你好234世界China(973 Program)(2013CB329001)。。。No.asdfasdfl1243 dsaf12 l Science Foundation of China(61021001;61133015;61171065);;"
lista = re.findall(r'((?<=No.)[A-Za-z0-9]+\b|(?<=[(;,])[A-Za-z0-9]+\b)', st)
print(type(lista),lista)
lista = [e for e in lista if (len(e) >= 5 and not e.isalpha())]
result = ';'.join(lista)
print(result)

print('asdf'.isalpha())
print('中国TianJin tianjin TianJIn'.lower())

sta ="国家自然科学基金(5136 8015)国家级自然科学基金合作项目(41102121j)supported by the National Natural Science Founda-tion Jump-Dealing of China(7117-1181;71301155)"
listb = re.findall(r'([A-Za-z0-9-]+)', sta)
listb = [e for e in listb if (len(e) >= 5 and not e.isalpha())]
print(listb)
for i in listb:
    if '-' in i:
        i_split = i.split("-")
        print([a for a in i_split if a.isalpha()])
        if all([a for a in i_split if a.isalpha()]):
            listb.remove(i)

resultb = ';'.join(listb)
print(resultb)


# key_lists1 = ['国家自然学基金', '国家级自然科学', '国家自科科学', '国家自科学基金', '国家杰出青年基金', '国家自然学科', '国家科学基金', '国家青年基金', '国家自然科', '国家青年自然基金',
#               '国家自然科研', '国家杰出青年科学', '国家杰出青年科学', '国家重点自然科学', '国家自科基金', '国家自然青年科学', '国家青年自然科学', '中国自然科学基金', '国家青年科学基金',
#               '国家自然基金', '国家自然资', '国家基础科学', '国家自然科技基金', '国家科学自然', '国家基金', '国家自然青年基金']
# key_lists2 = ['NSF China', 'National Scientific foundation of China', 'NSF of P.R.China', 'NSFC', 'NSF of China',
#               'Nature Science Foundation of China', 'National Natural Scientific', 'NNSF', 'National Natural Science',
#               'National Nature Science', 'National Natural Foundation', 'Natural Science Foundation',
#               'National Science Foundation']
# fund_code_res = ''
# remove_count =0
# fund_code_lists =[]
# l = ['国家自然科学基金(70871124)', '\n\n国家杰出青年基金(70825002)', '\n\n中山大学高校基本科研业务费专项资金(0909063)的资助']
# for ele in l:
#     # if ele.startswith('国家自然科学基金'):
#     if any(key.lower() in ele.lower() for key in key_lists1):
#
#         res_lists = re.findall(r'[A-Za-z0-9-]+', ele)
#         res_lists = list(set([e for e in res_lists if (len(e) >= 5 and not e.isalpha())]))
#         print(res_lists)
#         fund_code_lists.extend(res_lists)
#         # fund_code = ';'.join(res_lists)
#         # fund_code_res += fund_code
#     elif any(key.lower() in ele.lower() for key in key_lists2):
#         res_lists = re.findall(r'[A-Za-z0-9]+', ele)
#         res_lists = list(set([e for e in res_lists if (len(e) >= 5 and not e.isalpha())]))
#         print(res_lists)
#         fund_code_lists.extend(res_lists)
#         # fund_code = ';'.join(res_lists)
#         # fund_code_res += fund_code
#
#     else:
#         remove_count += 1
# fund_code_res = ';'.join(fund_code_lists)
#
# print(fund_code_res)
# print(remove_count)
# aaa = []
# ccc= ['c']
# aaa.extend(ccc)
# print(aaa)
