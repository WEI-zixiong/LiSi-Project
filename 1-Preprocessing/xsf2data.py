#%%
import numpy as np
import pandas as pd
import os
import re

# input_file = r'E:\file\...\1-LiSi\amorphous-LiSi-PBE\structure00001.xsf'
# output_file = r'E:\file\python-code\GNN\reshow\conv2txt\out.data'

# input_file_path = r'E:\file\...\1-LiSi\amorphous-LiSi-PBE'
input_file_path = r'E:\file\...\1-LiSi\test' # 小数据测试一下
output_file_path = r'E:\file\python-code\GNN\reshow\conv2txt\out-data-test'
os.mkdir(output_file_path) # 生成之后就可以注释了
input_path_list = os.listdir(input_file_path) # 列出文件

data_path_format = r'E:\file\python-code\GNN\reshow\conv2txt\out-data-test\{}'
data_name_format = r'{}'
data_path_name = []
data_out_name = []
file_num = [] # xsf文件名集合
regex = re.compile(r'structure+\d+\.+xsf$')
for i in input_path_list:
    file_num += regex.findall(i) # 统计xsf文件数量,并放在一起
file_po = [] # xsf文件位置集合
path_out = r'E:\file\...\1-LiSi\test\{}'
for i in list(range(len(file_num))):
    file_po.append(path_out.format(file_num[i]))
    data_path_name.append(data_path_format.format('structure' + str(i+1).zfill(5) + '.data'))
    data_out_name.append(data_name_format.format('structure' + str(i+1).zfill(5) + '.data'))

for i in list(range(len(file_num))):
    with open(file_po[i]) as f:
        lines = f.readlines()

# with open(input_file, 'r') as f1:
#     lines = f1.readlines() # 读取每一行数据

        count = 0 # 查询行数
        a = 0
        b = 0
        line_add_Li = []
        line_add_Si = [] # 存储
        # for count, lines1 in enumerate(open(input_file, "r")):
        for count, lines1 in enumerate(open(file_po[i], "r")):
            if lines1[0] == 'L': # 查询Li原子数
                a += 1
                line_add_Li.append(lines1) # 注意与extend的区别
            elif lines1[0] == 'S': # 查询Si原子数
                b += 1
                line_add_Si.append(lines1)
            count += 1

        line_numbers_Li = list(range(1, a + 1, 1)) # 从1开始
        line_numbers_Si = list(range(1, b + 1, 1))
        select_lines_all = []
        select_lines_Li = []
        select_lines_Si = [] # 存储要写入的总行数
        for line_number in line_numbers_Li:
            select_lines_Li.append(line_add_Li[line_number - 1].strip())
        for line_number in line_numbers_Si:
            select_lines_Si.append(line_add_Si[line_number - 1].strip())
        select_lines_all = select_lines_Li + select_lines_Si # 总行数

        final = []
        final_num = []
        final_all = []
        for line in select_lines_all:
            if re.match(r'\w+', line):
                final_all.append(re.split(r'\s+', line)) # 空格处分开
                # final = re.split(r'\D+\.?\D', line) # 忽略了负号
                final = re.split(r'\s+', line)
                final_temp = final[1:4] # 左闭右开
                final_num.append(final_temp)
        final_num = np.array(final_num) # 没有Li/Si在第一列
        final_all = np.array(final_all) # 有Li/Si在第一列，后续可替换

        atom_ID = list(range(1, a + b + 1, 1))
        atom_type_Li = [1] * a
        atom_type_Si = [2] * b
        atom_type = atom_type_Li + atom_type_Si
        final_num = np.insert(final_num, 0, values=atom_type, axis=1)
        final_num = np.insert(final_num, 0, values=atom_ID, axis=1) # 在0处插入atom_ID,1为列

        final_num_compare = final_num.astype(np.float16) # 用于后续计算box的大小

        # final_num_write = final_num.astype('str')
        # final_num_write = str(final_num) # write要写string
        final_num_write = np.array_str(final_num)
        # print(final_num_write)
        # print(type(final_num_write))
        # print(final_num[2, :])

        final_num_list = final_num.tolist()
        # print(final_num_list[0])
        test = list(range(len(final_num_list)))
        # for i in test:
        #     final_num_list2str = '  '.join(final_num_list[i]) # 合并在一起
        #     print(final_num_list2str)
        # print(final_num_list)
        # print(type(final_num_list))
        # print(final_num_list[2])

        # final_num_char = np.char.split(final_num, sep=' ') # 完全分开
        # print(final_num_char)

        max_box = np.max(final_num_compare, axis=0) # 0为列，1为行
        min_box = np.min(final_num_compare, axis=0)

        n = a + b
        os.chdir(output_file_path)
        with open(data_out_name[i], 'w') as f2:
            f2.write('lammps data\n')
            f2.write('\n')
            f2.write(str(n) + ' ' + 'atoms\n')
            f2.write('\n')
            f2.write(str(2) + ' ' + 'atom types\n')
            f2.write('\n')
            f2.write(str(min_box[2] - 1) + ' ' + str(max_box[2] + 1) + ' ' + 'xlo xhi\n')
            f2.write(str(min_box[3] - 1) + ' ' + str(max_box[3] + 1) + ' ' + 'ylo yhi\n')
            f2.write(str(min_box[4] - 1) + ' ' + str(max_box[4] + 1) + ' ' + 'zlo zhi\n')
            f2.write('\n')
            f2.write('Masses\n')
            f2.write('\n')
            f2.write(str(1) + ' ' + ' ' + str(6.9410) + '\n')
            f2.write(str(2) + ' ' + ' ' + str(28.0855) + '\n')
            f2.write('\n')
            f2.write('Atoms #atomic\n')
            f2.write('\n')
            for j in test:
                final_num_list2str = '   '.join(final_num_list[j])
                f2.write(final_num_list2str)
                f2.write('\n')
            f2.close()
    f.close()
