
#%% 1-modified replicate
import numpy as np
import pandas as pd
input_file_path = r'E:\file\...\8-LiSi'
data_file = input_file_path + r'\1.data'
output_file = input_file_path + r'\out1.data'
original_coord_li_x = []; original_coord_li_y = []; original_coord_li_z = []
original_coord_si_x = []; original_coord_si_y = []; original_coord_si_z = []
original_coord_li = []; original_coord_si = []
with open(data_file, 'r') as f:
    lines = f.readlines()
    box_x = lines[5].split()[1]
    box_y = lines[6].split()[1]
    box_z = lines[7].split()[1]
    for i in list(range(int(len(lines)) - 16)):
        a = lines[i + 16].split()
        if a[1] == '1':
            original_coord_li_x.append(a[2])
            original_coord_li_y.append(a[3])
            original_coord_li_z.append(a[4])
            original_coord_li.append(a)
        elif a[1] == '2':
            original_coord_si_x.append(a[2])
            original_coord_si_y.append(a[3])
            original_coord_si_z.append(a[4])
            original_coord_si.append(a)
f.close()
num_x = int(2); num_y = int(2); num_z = int(2)
coord_li_x = []; coord_li_y = []; coord_li_z = []
coord_si_x = []; coord_si_y = []; coord_si_z = []
box_x_new = np.float32(box_x) * (num_x + 1)
box_y_new = np.float32(box_y) * (num_y + 1)
box_z_new = np.float32(box_z) * (num_z + 1)

for a in list(range(num_x)):
    for j in list(range(len(original_coord_li_x))):
        coord_li_x.append(np.float32(original_coord_li_x[j]) + np.float32(box_x) * int(a + 1))
    for k in list(range(len(original_coord_si_x))):
        coord_si_x.append(np.float32(original_coord_si_x[k]) + np.float32(box_x) * int(a + 1))
coord_li_x = original_coord_li_x + coord_li_x
coord_li_y = original_coord_li_y * (num_x + 1); coord_li_z = original_coord_li_z * (num_x + 1)
coord_si_x = original_coord_si_x + coord_si_x
coord_si_y = original_coord_si_y * (num_x + 1); coord_si_z = original_coord_si_z * (num_x + 1)
for b in list(range(num_y)):
    for j in list(range(len(coord_li_x))): # or coord_li_y or coord_li_z
        coord_li_y.append(np.float32(coord_li_y[j]) + np.float32(box_y) * int(b + 1))
    for k in list(range(len(coord_si_x))):
        coord_si_y.append(np.float32(coord_si_y[k]) + np.float32(box_y) * int(b + 1))
coord_li_x = coord_li_x * (num_y + 1); coord_li_z = coord_li_z * (num_y + 1)
coord_si_x = coord_si_x * (num_y + 1); coord_si_z = coord_si_z * (num_y + 1)
for c in list(range(num_z)):
    for j in list(range(len(coord_li_x))):
        coord_li_z.append(np.float32(coord_li_z[j]) + np.float32(box_z) * int(c + 1))
    for k in list(range(len(coord_si_x))):
        coord_si_z.append(np.float32(coord_si_z[k]) + np.float32(box_z) * int(c + 1))
coord_li_x = coord_li_x * (num_z + 1); coord_li_y = coord_li_y * (num_z + 1)
coord_si_x = coord_si_x * (num_z + 1); coord_si_y = coord_si_y * (num_z + 1)

atom_num_li = int(len(coord_li_x))
atom_num_si = int(len(coord_si_x))
atom_num_total = atom_num_li + atom_num_si
atom_type_li = [1] * atom_num_li
atom_type_si = [2] * atom_num_si
list_li = list(range(len(coord_li_x))); list_li = [str(i + 1) for i in list_li]
length = 1 + int(len(coord_li_x))
list_si = list(range(len(coord_si_x))); list_si = [str(i + length) for i in list_si]
id_li = [1] * int(len(coord_li_x)); id_li = [str(i) for i in id_li]
id_si = [2] * int(len(coord_si_x)); id_si = [str(i) for i in id_si]
df_li = pd.DataFrame({'order': list_li, 'id': id_li,
                      'x': coord_li_x, 'y': coord_li_y, 'z': coord_li_z})
df_si = pd.DataFrame({'order': list_si, 'id': id_si,
                      'x': coord_si_x, 'y': coord_si_y, 'z': coord_si_z})
df = pd.concat([df_li, df_si])
# df.to_csv('2.data', sep= ' ', header=False, index=False)
final = np.array(df).tolist()

#%% 2-modify box
import numpy as np
# input_file_path = r'E:\file\...\8-LiSi'
# input_file_name = r'\3.data'
# output_file_name = r'\3_modify.data'
def modify_box(input_file_path, input_file_name, output_file_name):
    data_file = input_file_path + input_file_name
    output_file = input_file_path + output_file_name
    original_coord_li_x = []; original_coord_li_y = []; original_coord_li_z = []
    original_coord_si_x = []; original_coord_si_y = []; original_coord_si_z = []
    original_coord_li = []; original_coord_si = []
    box_x_store = []; box_y_store = []; box_z_store = []
    with open(data_file, 'r') as f:
        lines = f.readlines()
        for i in list(range(int(len(lines)) - 17)):
            a = lines[i + 17].split()
            if a[1] == '1':
                original_coord_li_x.append(a[2])
                original_coord_li_y.append(a[3])
                original_coord_li_z.append(a[4])
                original_coord_li.append(a)
            elif a[1] == '2':
                original_coord_si_x.append(a[2])
                original_coord_si_y.append(a[3])
                original_coord_si_z.append(a[4])
                original_coord_si.append(a)
        box_x_store = original_coord_li_x + original_coord_si_x
        box_y_store = original_coord_li_y + original_coord_si_y
        box_z_store = original_coord_li_z + original_coord_si_z
        box_x_max = 0.5 + np.max(np.float32(box_x_store))
        box_y_max = 0.5 + np.max(np.float32(box_y_store))
        box_z_max = 0.5 + np.max(np.float32(box_z_store))
        box_x_min = np.min(np.float32(box_x_store)) - 0.5
        box_y_min = np.min(np.float32(box_y_store)) - 0.5
        box_z_min = np.min(np.float32(box_z_store)) - 0.5
        final = original_coord_li + original_coord_si
        atom_num_total = len(final)
    with open(output_file, 'w') as f2:
        f2.write('lammps data\n')
        f2.write('\n')
        f2.write(str(atom_num_total) + ' ' + 'atoms\n')
        f2.write('\n')
        f2.write(str(2) + ' ' + 'atom types\n')
        f2.write('\n')
        f2.write(str(box_x_min) + ' ' + str(box_x_max) + ' ' + 'xlo xhi\n')
        f2.write(str(box_y_min) + ' ' + str(box_y_max) + ' ' + 'ylo yhi\n')
        f2.write(str(box_z_min) + ' ' + str(box_z_max) + ' ' + 'zlo zhi\n')
        f2.write('\n')
        f2.write('Masses\n')
        f2.write('\n')
        f2.write(str(1) + ' ' + ' ' + str(6.9410) + '\n')
        f2.write(str(2) + ' ' + ' ' + str(28.0855) + '\n')
        f2.write('\n')
        f2.write('Atoms #atomic\n')
        f2.write('\n')
        for j in list(range(len(final))):
            final_num_list2str = '   '.join(str(x) for x in final[j])
            f2.write(final_num_list2str)
            f2.write('\n')
    f2.close()
modify_box(r'E:\file\...\8-LiSi', r'\out3_test.data', r'\out3_test_modify.data')

#%% 3-final function, squared
import numpy as np
import pandas as pd
def replicate(num_x, num_y, num_z, input_file_path, input_file_name, output_file_name, x, y, z, start):
    data_file = input_file_path + input_file_name
    output_file = input_file_path + output_file_name
    original_coord_li_x = []
    original_coord_li_y = []
    original_coord_li_z = []
    original_coord_si_x = []
    original_coord_si_y = []
    original_coord_si_z = []
    original_coord_li = []
    original_coord_si = []
    with open(data_file, 'r') as f:
        lines = f.readlines()
        box_x = lines[x].split()[1]
        box_y = lines[y].split()[1]
        box_z = lines[z].split()[1]
        for i in list(range(int(len(lines)) - int(start))):
            a = lines[i + int(start)].split()
            if a[1] == '1':
                original_coord_li_x.append(a[2])
                original_coord_li_y.append(a[3])
                original_coord_li_z.append(a[4])
                original_coord_li.append(a)
            elif a[1] == '2':
                original_coord_si_x.append(a[2])
                original_coord_si_y.append(a[3])
                original_coord_si_z.append(a[4])
                original_coord_si.append(a)
    f.close()
    num_x = int(num_x)
    num_y = int(num_y)
    num_z = int(num_z)
    coord_li_x = []
    coord_li_y = []
    coord_li_z = []
    coord_si_x = []
    coord_si_y = []
    coord_si_z = []
    box_x_new = np.float32(box_x) * (num_x + 1)
    box_y_new = np.float32(box_y) * (num_y + 1)
    box_z_new = np.float32(box_z) * (num_z + 1)
    for a in list(range(num_x)):
        for j in list(range(len(original_coord_li_x))):
            coord_li_x.append(np.float32(original_coord_li_x[j]) + np.float32(box_x) * int(a + 1))
        for k in list(range(len(original_coord_si_x))):
            coord_si_x.append(np.float32(original_coord_si_x[k]) + np.float32(box_x) * int(a + 1))
    coord_li_x = original_coord_li_x + coord_li_x
    coord_li_y = original_coord_li_y * (num_x + 1)
    coord_li_z = original_coord_li_z * (num_x + 1)
    coord_si_x = original_coord_si_x + coord_si_x
    coord_si_y = original_coord_si_y * (num_x + 1)
    coord_si_z = original_coord_si_z * (num_x + 1)
    for b in list(range(num_y)):
        for j in list(range(len(coord_li_x))):  # or coord_li_y or coord_li_z
            coord_li_y.append(np.float32(coord_li_y[j]) + np.float32(box_y) * int(b + 1))
        for k in list(range(len(coord_si_x))):
            coord_si_y.append(np.float32(coord_si_y[k]) + np.float32(box_y) * int(b + 1))
    coord_li_x = coord_li_x * (num_y + 1)
    coord_li_z = coord_li_z * (num_y + 1)
    coord_si_x = coord_si_x * (num_y + 1)
    coord_si_z = coord_si_z * (num_y + 1)
    for c in list(range(num_z)):
        for j in list(range(len(coord_li_x))):
            coord_li_z.append(np.float32(coord_li_z[j]) + np.float32(box_z) * int(c + 1))
        for k in list(range(len(coord_si_x))):
            coord_si_z.append(np.float32(coord_si_z[k]) + np.float32(box_z) * int(c + 1))
    coord_li_x = coord_li_x * (num_z + 1)
    coord_li_y = coord_li_y * (num_z + 1)
    coord_si_x = coord_si_x * (num_z + 1)
    coord_si_y = coord_si_y * (num_z + 1)

    atom_num_li = int(len(coord_li_x))
    atom_num_si = int(len(coord_si_x))
    atom_num_total = atom_num_li + atom_num_si
    atom_type_li = [1] * atom_num_li
    atom_type_si = [2] * atom_num_si
    list_li = list(range(len(coord_li_x)))
    list_li = [i + 1 for i in list_li]
    length = 1 + int(len(coord_li_x))
    list_si = list(range(len(coord_si_x)))
    list_si = [i + length for i in list_si]
    id_li = [1] * int(len(coord_li_x))
    id_li = [str(i) for i in id_li]
    id_si = [2] * int(len(coord_si_x))
    id_si = [str(i) for i in id_si]
    df_li = pd.DataFrame({'order': list_li, 'id': id_li,
                          'x': coord_li_x, 'y': coord_li_y, 'z': coord_li_z})
    df_si = pd.DataFrame({'order': list_si, 'id': id_si,
                          'x': coord_si_x, 'y': coord_si_y, 'z': coord_si_z})
    df = pd.concat([df_li, df_si])
    # df.to_csv('2.data', sep=' ', header=False, index=False)
    final = np.array(df).tolist() # first two columns: int

    with open(output_file, 'w') as f2:
        f2.write('lammps data\n')
        f2.write('\n')
        f2.write(str(atom_num_total) + ' ' + 'atoms\n')
        f2.write('\n')
        f2.write(str(2) + ' ' + 'atom types\n')
        f2.write('\n')
        f2.write(str(0) + ' ' + str(box_x_new) + ' ' + 'xlo xhi\n')
        f2.write(str(0) + ' ' + str(box_y_new) + ' ' + 'ylo yhi\n')
        f2.write(str(0) + ' ' + str(box_z_new) + ' ' + 'zlo zhi\n')
        f2.write('\n')
        f2.write('Masses\n')
        f2.write('\n')
        f2.write(str(1) + ' ' + ' ' + str(6.9410) + '\n')
        f2.write(str(2) + ' ' + ' ' + str(28.0855) + '\n')
        f2.write('\n')
        f2.write('Atoms #atomic\n')
        f2.write('\n')
        for j in list(range(len(final))):
            final_num_list2str = '   '.join(str(x) for x in final[j])
            f2.write(final_num_list2str)
            f2.write('\n')
    f2.close()
    return "DONE!"
replicate(25, 16, 6, r'E:\file\...\8-LiSi', r'\1.data', r'\out1_4.data', 5, 6, 7, 16)

#%% 4-function, non-squared
import numpy as np
import pandas as pd
def replicate(num_x, num_y, num_z, input_file_path, input_file_name, output_file_name, x, y, z, start, dx, dz, xy, xz):
    data_file = input_file_path + input_file_name
    output_file = input_file_path + output_file_name
    original_coord_li_x = []
    original_coord_li_y = []
    original_coord_li_z = []
    original_coord_si_x = []
    original_coord_si_y = []
    original_coord_si_z = []
    original_coord_li = []
    original_coord_si = []
    with open(data_file, 'r') as f:
        lines = f.readlines()
        box_x = lines[x].split()[1]
        box_y = lines[y].split()[1]
        box_z = lines[z].split()[1]
        for i in list(range(int(len(lines)) - int(start))):
            a = lines[i + int(start)].split()
            if a[1] == '1':
                original_coord_li_x.append(a[2])
                original_coord_li_y.append(a[3])
                original_coord_li_z.append(a[4])
                original_coord_li.append(a)
            elif a[1] == '2':
                original_coord_si_x.append(a[2])
                original_coord_si_y.append(a[3])
                original_coord_si_z.append(a[4])
                original_coord_si.append(a)
    f.close()
    num_x = int(num_x)
    num_y = int(num_y)
    num_z = int(num_z)
    coord_li_x = []
    coord_li_x_store_1 = []
    coord_li_x_store_2 = []
    coord_li_y = []
    coord_li_z = []
    coord_si_x = []
    coord_si_x_store_1 = []
    coord_si_x_store_2 = []
    coord_si_y = []
    coord_si_z = []
    box_x_new = np.float32(box_x) * (num_x + 1)
    box_y_new = np.float32(box_y) * (num_y + 1)
    box_z_new = np.float32(box_z) * (num_z + 1)

    for a in list(range(num_x)):
        for j in list(range(len(original_coord_li_x))):
            coord_li_x.append(np.float32(original_coord_li_x[j]) + np.float32(box_x) * int(a + 1) + dx * int(a + 1))
        for k in list(range(len(original_coord_si_x))):
            coord_si_x.append(np.float32(original_coord_si_x[k]) + np.float32(box_x) * int(a + 1) + dx * int(a + 1))
    coord_li_x = original_coord_li_x + coord_li_x
    coord_li_y = original_coord_li_y * (num_x + 1)
    coord_li_z = original_coord_li_z * (num_x + 1)
    coord_si_x = original_coord_si_x + coord_si_x
    coord_si_y = original_coord_si_y * (num_x + 1)
    coord_si_z = original_coord_si_z * (num_x + 1)

    for b in list(range(num_y)):
        for j in list(range(len(coord_li_x))):  # or coord_li_y or coord_li_z
            coord_li_y.append(np.float32(coord_li_y[j]) + np.float32(box_y) * int(b + 1))
        for k in list(range(len(coord_si_x))):
            coord_si_y.append(np.float32(coord_si_y[k]) + np.float32(box_y) * int(b + 1))
    coord_li_x_store_1 = coord_li_x
    coord_si_x_store_1 = coord_si_x
    for p in list(range(num_y)):
        coord_li_x = coord_li_x + [np.float32(i) + xy * int(p + 1) for i in coord_li_x_store_1]
        coord_si_x = coord_si_x + [np.float32(i) + xy * int(p + 1) for i in coord_si_x_store_1]
    coord_li_z = coord_li_z * (num_y + 1)
    coord_si_z = coord_si_z * (num_y + 1)

    for c in list(range(num_z)):
        for j in list(range(len(coord_li_x))):
            coord_li_z.append(np.float32(coord_li_z[j]) + np.float32(box_z) * int(c + 1) + dz * int(c + 1))
        for k in list(range(len(coord_si_x))):
            coord_si_z.append(np.float32(coord_si_z[k]) + np.float32(box_z) * int(c + 1) + dz * int(c + 1))
    coord_li_x_store_2 = coord_li_x
    coord_si_x_store_2 = coord_si_x
    for q in list(range(num_z)):
        coord_li_x = coord_li_x + [np.float32(i) + xz * int(q + 1) for i in coord_li_x_store_2]
        coord_si_x = coord_si_x + [np.float32(i) + xz * int(q + 1) for i in coord_si_x_store_2]
    coord_li_y = coord_li_y * (num_z + 1)
    coord_si_y = coord_si_y * (num_z + 1)

    atom_num_li = int(len(coord_li_x))
    atom_num_si = int(len(coord_si_x))
    atom_num_total = atom_num_li + atom_num_si
    atom_type_li = [1] * atom_num_li
    atom_type_si = [2] * atom_num_si
    list_li = list(range(len(coord_li_x)))
    list_li = [i + 1 for i in list_li]
    length = 1 + int(len(coord_li_x))
    list_si = list(range(len(coord_si_x)))
    list_si = [i + length for i in list_si]
    id_li = [1] * int(len(coord_li_x))
    id_li = [str(i) for i in id_li]
    id_si = [2] * int(len(coord_si_x))
    id_si = [str(i) for i in id_si]
    df_li = pd.DataFrame({'order': list_li, 'id': id_li,
                          'x': coord_li_x, 'y': coord_li_y, 'z': coord_li_z})
    df_si = pd.DataFrame({'order': list_si, 'id': id_si,
                          'x': coord_si_x, 'y': coord_si_y, 'z': coord_si_z})
    df = pd.concat([df_li, df_si])
    # df.to_csv('2.data', sep=' ', header=False, index=False)
    final = np.array(df).tolist() # first two columns: int

    with open(output_file, 'w') as f2:
        f2.write('lammps data\n')
        f2.write('\n')
        f2.write(str(atom_num_total) + ' ' + 'atoms\n')
        f2.write('\n')
        f2.write(str(2) + ' ' + 'atom types\n')
        f2.write('\n')
        f2.write(str(0) + ' ' + str(box_x_new) + ' ' + 'xlo xhi\n')
        f2.write(str(0) + ' ' + str(box_y_new) + ' ' + 'ylo yhi\n')
        f2.write(str(0) + ' ' + str(box_z_new) + ' ' + 'zlo zhi\n')
        f2.write('\n')
        f2.write('Masses\n')
        f2.write('\n')
        f2.write(str(1) + ' ' + ' ' + str(6.9410) + '\n')
        f2.write(str(2) + ' ' + ' ' + str(28.0855) + '\n')
        f2.write('\n')
        f2.write('Atoms #atomic\n')
        f2.write('\n')
        for j in list(range(len(final))):
            final_num_list2str = '   '.join(str(x) for x in final[j])
            f2.write(final_num_list2str)
            f2.write('\n')
    f2.close()
    return "DONE!"
replicate(15, 15, 15, r'E:\file\...\8-LiSi', r'\3_modify.data', r'\out3_test.data', 6,7,8,17,0.8,0.5,-2.7,0) # LiSi3
