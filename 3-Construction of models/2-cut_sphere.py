
#%% 1-Orthorhombic, monitor
import numpy as np
import pandas as pd
import math
input_file_path = r'E:\file_path'
input_file_name = r'\out1.data'
output_file_name = r'\sphere1.data'
data_file = input_file_path + input_file_name
output_file = input_file_path + output_file_name
with open(data_file, 'r') as f:
    lines = f.readlines()
    original_coord_li_x = []
    original_coord_li_y = []
    original_coord_li_z = []
    original_coord_si_x = []
    original_coord_si_y = []
    original_coord_si_z = []
    original_coord_li = []
    original_coord_si = []
    box_x = np.float32(lines[6].split()[1])
    box_y = np.float32(lines[7].split()[1])
    box_z = np.float32(lines[8].split()[1])
    box_min = round(np.min([box_x, box_y, box_z]))
    box_half = np.float32(box_min)/2
    center_atom_li = []
    center_atom_si = []
    perturb_li = 1.5
    perturb_si = 1.5
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
    for j in list(range(len(original_coord_li_x))):
        if (box_half - perturb_li) < np.float32(original_coord_li_x[j]) < (box_half + perturb_li):
            if (box_half - perturb_li) < np.float32(original_coord_li_y[j]) < (box_half + perturb_li):
                if (box_half - perturb_li) < np.float32(original_coord_li_z[j]) < (box_half + perturb_li):
                    center_atom_li.append(original_coord_li[j])
    for k in list(range(len(original_coord_si_x))):
        if (box_half - perturb_si) < np.float32(original_coord_si_x[k]) < (box_half + perturb_si):
            if (box_half - perturb_si) < np.float32(original_coord_si_y[k]) < (box_half + perturb_si):
                if (box_half - perturb_si) < np.float32(original_coord_si_z[k]) < (box_half + perturb_si):
                    center_atom_si.append(original_coord_si[k])
    sphere_li = []
    sphere_si = []
    radius_li = 30
    radius_si = 30
    for m in list(range(len(original_coord_li_x))):
        if math.sqrt( (np.float32(original_coord_li_x[m]) - np.float32(center_atom_li[0][2])) ** 2
                 + (np.float32(original_coord_li_y[m]) - np.float32(center_atom_li[0][3])) ** 2
                 + (np.float32(original_coord_li_z[m]) - np.float32(center_atom_li[0][4])) ** 2 ) <= radius_li:
            sphere_li.append(original_coord_li[m])
    for n in list(range(len(original_coord_si_x))):
        if math.sqrt( (np.float32(original_coord_si_x[n]) - np.float32(center_atom_li[0][2])) ** 2
                 + (np.float32(original_coord_si_y[n]) - np.float32(center_atom_li[0][3])) ** 2
                 + (np.float32(original_coord_si_z[n]) - np.float32(center_atom_li[0][4])) ** 2 ) <= radius_li:
            sphere_si.append(original_coord_si[n])
    df_li = pd.DataFrame(sphere_li, columns=['order', 'type', 'x', 'y', 'z'])
    df_li_drop = df_li.drop('order', axis=1)
    order_li = list(range(len(sphere_li)))
    order_li = [str(i + 1) for i in order_li]
    df_li_drop.insert(loc = 0, column = 'order', value = order_li)

    df_si = pd.DataFrame(sphere_si, columns=['order', 'type', 'x', 'y', 'z'])
    df_si_drop = df_si.drop('order', axis=1)
    order_si = list(range(len(sphere_si)))
    order_si = [str(i + 1 +len(sphere_li)) for i in order_si]
    df_si_drop.insert(loc = 0, column = 'order', value = order_si)
    df = pd.concat([df_li_drop, df_si_drop])
    final = np.array(df).tolist()

    n = len(sphere_li) + len(sphere_si)
    w = [np.float32(sphere_li[i][2]) for i in list(range(len(sphere_li)))]
    z = [np.float32(sphere_li[i][3]) for i in list(range(len(sphere_li)))]
    x = [np.float32(sphere_li[i][4]) for i in list(range(len(sphere_li)))]
    max_box_x = 1 + np.max(w)
    max_box_y = 1 + np.max(z)
    max_box_z = 1 + np.max(x)

    with open(output_file, 'w') as f2:
        f2.write('lammps data\n')
        f2.write('\n')
        f2.write(str(n) + ' ' + 'atoms\n')
        f2.write('\n')
        f2.write(str(2) + ' ' + 'atom types\n')
        f2.write('\n')
        f2.write(str(0) + ' ' + str(max_box_x) + ' ' + 'xlo xhi\n')
        f2.write(str(0) + ' ' + str(max_box_y) + ' ' + 'ylo yhi\n')
        f2.write(str(0) + ' ' + str(max_box_z) + ' ' + 'zlo zhi\n')
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
f.close()

#%% 2-non-Orthorhombic, function
import numpy as np
import pandas as pd
import math
def cut(input_file_path, input_file_name, output_file_name, p_li, p_si, radius, offset):
    data_file = input_file_path + input_file_name
    output_file = input_file_path + output_file_name
    perturb_li = p_li
    perturb_si = p_si
    radius_li = radius
    offset = offset
    with open(data_file, 'r') as f:
        lines = f.readlines()
        original_coord_li_x = []
        original_coord_li_y = []
        original_coord_li_z = []
        original_coord_si_x = []
        original_coord_si_y = []
        original_coord_si_z = []
        original_coord_li = []
        original_coord_si = []
        box_x = np.float32(lines[6].split()[1])
        box_y = np.float32(lines[7].split()[1])
        box_z = np.float32(lines[8].split()[1])
        box_min = math.floor(np.min([box_x, box_y, box_z]))
        box_half = np.float32(box_min)/2
        box_half_modify = box_half + offset
        center_atom_li = []
        center_atom_si = []
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
        for j in list(range(len(original_coord_li_x))):
            if (box_half_modify - perturb_li) < np.float32(original_coord_li_x[j]) < (box_half_modify + perturb_li):
                if (box_half - perturb_li) < np.float32(original_coord_li_y[j]) < (box_half + perturb_li):
                    if (box_half - perturb_li) < np.float32(original_coord_li_z[j]) < (box_half + perturb_li):
                        center_atom_li.append(original_coord_li[j])
        for k in list(range(len(original_coord_si_x))):
            if (box_half_modify - perturb_si) < np.float32(original_coord_si_x[k]) < (box_half_modify + perturb_si):
                if (box_half - perturb_si) < np.float32(original_coord_si_y[k]) < (box_half + perturb_si):
                    if (box_half - perturb_si) < np.float32(original_coord_si_z[k]) < (box_half + perturb_si):
                        center_atom_si.append(original_coord_si[k])
        sphere_li = []
        sphere_si = []
        for m in list(range(len(original_coord_li_x))):
            if math.sqrt( (np.float32(original_coord_li_x[m]) - np.float32(center_atom_li[0][2])) ** 2
                     + (np.float32(original_coord_li_y[m]) - np.float32(center_atom_li[0][3])) ** 2
                     + (np.float32(original_coord_li_z[m]) - np.float32(center_atom_li[0][4])) ** 2 ) <= radius_li:
                sphere_li.append(original_coord_li[m])
        for n in list(range(len(original_coord_si_x))):
            if math.sqrt( (np.float32(original_coord_si_x[n]) - np.float32(center_atom_li[0][2])) ** 2
                     + (np.float32(original_coord_si_y[n]) - np.float32(center_atom_li[0][3])) ** 2
                     + (np.float32(original_coord_si_z[n]) - np.float32(center_atom_li[0][4])) ** 2 ) <= radius_li:
                sphere_si.append(original_coord_si[n])
        df_li = pd.DataFrame(sphere_li, columns=['order', 'type', 'x', 'y', 'z'])
        df_li_drop = df_li.drop('order', axis=1)
        order_li = list(range(len(sphere_li)))
        order_li = [str(i + 1) for i in order_li]
        df_li_drop.insert(loc = 0, column = 'order', value = order_li)

        df_si = pd.DataFrame(sphere_si, columns=['order', 'type', 'x', 'y', 'z'])
        df_si_drop = df_si.drop('order', axis=1)
        order_si = list(range(len(sphere_si)))
        order_si = [str(i + 1 +len(sphere_li)) for i in order_si]
        df_si_drop.insert(loc = 0, column = 'order', value = order_si)
        df = pd.concat([df_li_drop, df_si_drop])
        final = np.array(df).tolist()

        n = len(sphere_li) + len(sphere_si)
        w = [np.float32(sphere_li[i][2]) for i in list(range(len(sphere_li)))]
        z = [np.float32(sphere_li[i][3]) for i in list(range(len(sphere_li)))]
        x = [np.float32(sphere_li[i][4]) for i in list(range(len(sphere_li)))]
        max_box_x = 1 + np.max(w)
        max_box_y = 1 + np.max(z)
        max_box_z = 1 + np.max(x)
        min_box_x = max_box_x - (2 * radius_li + 2)
        min_box_y = max_box_y - (2 * radius_li + 2)
        min_box_z = max_box_z - (2 * radius_li + 2)

        with open(output_file, 'w') as f2:
            f2.write('lammps data\n')
            f2.write('\n')
            f2.write(str(n) + ' ' + 'atoms\n')
            f2.write('\n')
            f2.write(str(2) + ' ' + 'atom types\n')
            f2.write('\n')
            f2.write(str(min_box_x) + ' ' + str(max_box_x) + ' ' + 'xlo xhi\n')
            f2.write(str(min_box_y) + ' ' + str(max_box_y) + ' ' + 'ylo yhi\n')
            f2.write(str(min_box_z) + ' ' + str(max_box_z) + ' ' + 'zlo zhi\n')
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
    f.close()

#%% 3-non-Orthorhombic, monitor
import numpy as np
import pandas as pd
import math
input_file_path = r'E:\file_path'
input_file_name = r'\out3_test_modify.data'
output_file_name = r'\sphere3_test.data'
perturb_li = 1.8
perturb_si = 1.2
radius_li = 30
offset = -20
data_file = input_file_path + input_file_name
output_file = input_file_path + output_file_name
with open(data_file, 'r') as f:
    lines = f.readlines()
    original_coord_li_x = []
    original_coord_li_y = []
    original_coord_li_z = []
    original_coord_si_x = []
    original_coord_si_y = []
    original_coord_si_z = []
    original_coord_li = []
    original_coord_si = []
    box_x = np.float32(lines[6].split()[1])
    box_y = np.float32(lines[7].split()[1])
    box_z = np.float32(lines[8].split()[1])
    box_min = math.floor(np.min([box_x, box_y, box_z]))
    box_half = np.float32(box_min) / 2
    box_half_modify = box_half + offset
    center_atom_li = []
    center_atom_si = []
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
    for j in list(range(len(original_coord_li_x))):
        if (box_half_modify - perturb_li) < np.float32(original_coord_li_x[j]) < (box_half_modify + perturb_li):
            if (box_half - perturb_li) < np.float32(original_coord_li_y[j]) < (box_half + perturb_li):
                if (box_half - perturb_li) < np.float32(original_coord_li_z[j]) < (box_half + perturb_li):
                    center_atom_li.append(original_coord_li[j])
    for k in list(range(len(original_coord_si_x))):
        if (box_half_modify - perturb_si) < np.float32(original_coord_si_x[k]) < (box_half_modify + perturb_si):
            if (box_half - perturb_si) < np.float32(original_coord_si_y[k]) < (box_half + perturb_si):
                if (box_half - perturb_si) < np.float32(original_coord_si_z[k]) < (box_half + perturb_si):
                    center_atom_si.append(original_coord_si[k])
    sphere_li = []
    sphere_si = []
    for m in list(range(len(original_coord_li_x))):
        if math.sqrt((np.float32(original_coord_li_x[m]) - np.float32(center_atom_li[0][2])) ** 2
                     + (np.float32(original_coord_li_y[m]) - np.float32(center_atom_li[0][3])) ** 2
                     + (np.float32(original_coord_li_z[m]) - np.float32(center_atom_li[0][4])) ** 2) <= radius_li:
            sphere_li.append(original_coord_li[m])
    for n in list(range(len(original_coord_si_x))):
        if math.sqrt((np.float32(original_coord_si_x[n]) - np.float32(center_atom_li[0][2])) ** 2
                     + (np.float32(original_coord_si_y[n]) - np.float32(center_atom_li[0][3])) ** 2
                     + (np.float32(original_coord_si_z[n]) - np.float32(center_atom_li[0][4])) ** 2) <= radius_li:
            sphere_si.append(original_coord_si[n])
    df_li = pd.DataFrame(sphere_li, columns=['order', 'type', 'x', 'y', 'z'])
    df_li_drop = df_li.drop('order', axis=1)
    order_li = list(range(len(sphere_li)))
    order_li = [str(i + 1) for i in order_li]
    df_li_drop.insert(loc=0, column='order', value=order_li)

    df_si = pd.DataFrame(sphere_si, columns=['order', 'type', 'x', 'y', 'z'])
    df_si_drop = df_si.drop('order', axis=1)
    order_si = list(range(len(sphere_si)))
    order_si = [str(i + 1 + len(sphere_li)) for i in order_si]
    df_si_drop.insert(loc=0, column='order', value=order_si)
    df = pd.concat([df_li_drop, df_si_drop])
    final = np.array(df).tolist()

    n = len(sphere_li) + len(sphere_si)
    w = [np.float32(sphere_li[i][2]) for i in list(range(len(sphere_li)))]
    z = [np.float32(sphere_li[i][3]) for i in list(range(len(sphere_li)))]
    x = [np.float32(sphere_li[i][4]) for i in list(range(len(sphere_li)))]
    max_box_x = 1 + np.max(w)
    max_box_y = 1 + np.max(z)
    max_box_z = 1 + np.max(x)
    min_box_x = max_box_x - (2 * radius_li + 2)
    min_box_y = max_box_y - (2 * radius_li + 2)
    min_box_z = max_box_z - (2 * radius_li + 2)

    with open(output_file, 'w') as f2:
        f2.write('lammps data\n')
        f2.write('\n')
        f2.write(str(n) + ' ' + 'atoms\n')
        f2.write('\n')
        f2.write(str(2) + ' ' + 'atom types\n')
        f2.write('\n')
        f2.write(str(min_box_x) + ' ' + str(max_box_x) + ' ' + 'xlo xhi\n')
        f2.write(str(min_box_y) + ' ' + str(max_box_y) + ' ' + 'ylo yhi\n')
        f2.write(str(min_box_z) + ' ' + str(max_box_z) + ' ' + 'zlo zhi\n')
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
f.close()
