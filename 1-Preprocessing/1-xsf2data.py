#%%
import numpy as np
import pandas as pd
import os
import re

input_file_path = r'E:\file_path1' # specify xsf file path
output_file_path = r'E:\file_path2'
os.mkdir(output_file_path)
input_path_list = os.listdir(input_file_path) # list all files

data_path_format = r'E:\file_path2\{}'
data_name_format = r'{}'
data_path_name = []
data_out_name = []
file_num = [] # store the names of xsf files
regex = re.compile(r'structure+\d+\.+xsf$')
for i in input_path_list:
    file_num += regex.findall(i) 
file_po = [] # store the paths of xsf files
path_out = r'E:\file_path1\{}'
for i in list(range(len(file_num))):
    file_po.append(path_out.format(file_num[i]))
    data_path_name.append(data_path_format.format('structure' + str(i+1).zfill(5) + '.data'))
    data_out_name.append(data_name_format.format('structure' + str(i+1).zfill(5) + '.data'))

for i in list(range(len(file_num))):
    with open(file_po[i]) as f:
        lines = f.readlines()

        count = 0 # check the number of lines
        a = 0
        b = 0
        line_add_Li = []
        line_add_Si = [] # store
        for count, lines1 in enumerate(open(file_po[i], "r")):
            if lines1[0] == 'L': # check the number of Li atoms
                a += 1
                line_add_Li.append(lines1) 
            elif lines1[0] == 'S': # check the number of Si atoms
                b += 1
                line_add_Si.append(lines1)
            count += 1

        line_numbers_Li = list(range(1, a + 1, 1)) # starting from 1
        line_numbers_Si = list(range(1, b + 1, 1))
        select_lines_all = []
        select_lines_Li = []
        select_lines_Si = [] # store all lines to be written
        for line_number in line_numbers_Li:
            select_lines_Li.append(line_add_Li[line_number - 1].strip())
        for line_number in line_numbers_Si:
            select_lines_Si.append(line_add_Si[line_number - 1].strip())
        select_lines_all = select_lines_Li + select_lines_Si # total number of all lines

        final = []
        final_num = []
        final_all = []
        for line in select_lines_all:
            if re.match(r'\w+', line):
                final_all.append(re.split(r'\s+', line)) # split from blankspace
                final = re.split(r'\s+', line)
                final_temp = final[1:4] 
                final_num.append(final_temp)
        final_num = np.array(final_num) 
        final_all = np.array(final_all) 

        atom_ID = list(range(1, a + b + 1, 1))
        atom_type_Li = [1] * a
        atom_type_Si = [2] * b
        atom_type = atom_type_Li + atom_type_Si
        final_num = np.insert(final_num, 0, values=atom_type, axis=1)
        final_num = np.insert(final_num, 0, values=atom_ID, axis=1) 

        final_num_compare = final_num.astype(np.float16) 
        final_num_write = np.array_str(final_num)
        final_num_list = final_num.tolist()
        test = list(range(len(final_num_list)))
        
        max_box = np.max(final_num_compare, axis=0) # 0: column, 1: line
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
