#%%
dump_lines = []
large = []
small = []
list_np_small = list(range(315))
np_coord_small = []
list_np_large = list(range(1015))
np_coord_large = []
list_cg = list(range(102))
cg_coord = []
modified_lines_small = []
modified_lines_large = []
large_coord = []
small_coord = []
pour_dump_file = r'E:\file\...\Pouring_funnel.dump'
small_data_file = r'E:\file\...\nano_6.data'
large_data_file = r'E:\file\...\nano_5.data'
final_data_file = r'E:\file\...\final3.data'
with open(pour_dump_file, 'r') as dump:
    lines_dump = dump.readlines()
    print(len(lines_dump))
    for i in range(1061573, 1061623, 1):
        print(lines_dump[i])
        dump_lines.append(lines_dump[i])
        cg_coord.append(lines_dump[i])
        dump_split_line = lines_dump[i].split()
        if dump_split_line[2] == '15':
            large.append(dump_split_line[0])
            large_coord.append(dump_split_line[4:7])
        elif dump_split_line[2] == '10':
            small.append(dump_split_line[0])
            small_coord.append(dump_split_line[4:7])
    print(large)
    print(small)
dump.close()

with open(small_data_file, 'r+') as file:
    lines_files = file.readlines()
    for i, line_files in enumerate(lines_files):
        if i == 2:
            files_split_line = line_files.split()
            files_split_line[0] = str(int(300) * int(len(small_coord)) + int(1000) * int(len(large_coord)))
            lines_files[i] = ' '.join(files_split_line) + '\n'
        elif i in [4, 5, 6]:
            files_split_line = line_files.split()
            files_split_line[0] = '-5'
            files_split_line[1] = '105'
            lines_files[i] = ' '.join(files_split_line) + '\n'
    file.seek(0)
    file.writelines(lines_files)
file.close()
with open(small_data_file, 'r') as nano1:
    lines_np = nano1.readlines()
    for k, line_k in enumerate(lines_np):
        if k in list_np_small[15:]:
            np_coord_small.append(lines_np[k].split())
            elements = lines_np[k].split()
            elements[2] = str(float(elements[2]) + float(small_coord[0][0]))
            elements[3] = str(float(elements[3]) + float(small_coord[0][1]))
            elements[4] = str(float(elements[4]) + float(small_coord[0][2]))
            modified_line_small = ' '.join(elements) + '\n'
            modified_lines_small.append(modified_line_small)
        else:
            modified_lines_small.append(line_k)
nano1.close()
with open(final_data_file, 'w') as nano2:
    nano2.writelines(modified_lines_small)
nano2.close()
copy_lines_small = lines_np[15:316].copy()
modified_orders_small = []
for i in range(len(small_coord)):
    if i+1 < len(small_coord):
        for j in range(len(copy_lines_small)):
            order = copy_lines_small[j].split()
            order[0] = str(int(order[0]) + 300 * (i+1))
            order[2] = str(float(order[2]) + float(small_coord[i+1][0]))
            order[3] = str(float(order[3]) + float(small_coord[i+1][1]))
            order[4] = str(float(order[4]) + float(small_coord[i+1][2]))
            modified_order_small = ' '.join(order) + '\n'
            modified_orders_small.append(modified_order_small)
with open(final_data_file, 'a+') as nano3:
    nano3.writelines(modified_orders_small)
nano3.close()

with open(large_data_file, 'r') as nano4:
    lines_np_large = nano4.readlines()
    for l, line_l in enumerate(lines_np_large):
        if l in list_np_large[15:]:
            np_coord_large.append(line_l.split())
            elements_large = line_l.split()
            elements_large[0] = str(int(elements_large[0]) + int(300) * int(len(small_coord)))
            elements_large[2] = str(float(elements_large[2]) + float(large_coord[0][0]))
            elements_large[3] = str(float(elements_large[3]) + float(large_coord[0][1]))
            elements_large[4] = str(float(elements_large[4]) + float(large_coord[0][2]))
            modified_line_large = ' '.join(elements_large) + '\n'
            modified_lines_large.append(modified_line_large)
nano4.close()
with open(final_data_file, 'a+') as nano5:
    nano5.writelines(modified_lines_large)
nano5.close()
copy_lines_large = lines_np_large[15:1015].copy()
modified_orders_large = []
for i in range(len(large_coord)):
    if i+1 < len(large_coord):
        for j in range(len(copy_lines_large)):
            order_large = copy_lines_large[j].split()
            order_large[0] = str(int(order_large[0]) + int(300) * int(len(small_coord)) + 1000 * (i+1))
            order_large[2] = str(float(order_large[2]) + float(large_coord[i+1][0]))
            order_large[3] = str(float(order_large[3]) + float(large_coord[i+1][1]))
            order_large[4] = str(float(order_large[4]) + float(large_coord[i+1][2]))
            modified_order_large = ' '.join(order_large) + '\n'
            modified_orders_large.append(modified_order_large)
with open(final_data_file, 'a+') as nano6:
    nano6.writelines(modified_orders_large)
nano6.close()
