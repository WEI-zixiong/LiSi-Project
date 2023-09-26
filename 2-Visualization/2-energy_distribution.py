import numpy as np
import pandas as pd
import os
import re
import matplotlib
import matplotlib.pyplot as plt
input_file_path = r'E:\file\...'
input_path_list = os.listdir(input_file_path)
file_path = []
path_out = input_file_path +'\{}'
energy = []
ratio = []
pure_li = []
pure_si = []
norm_energy = []
num_li = []
num_si = []
for i in list(range(len(input_path_list[:10000]))):
    file_path.append(path_out.format(input_path_list[i]))

    with open(file_path[i]) as f:
        lines = f.readlines()
        a = 0
        b = 0
        line_add_Li = []
        line_add_Si = []
        line_all = []
        for count, lines1 in enumerate(open(file_path[i], "r")):
            if lines1[0] == 'L':
                a += 1
                line_add_Li.append(lines1)
            elif lines1[0] == 'S':
                b += 1
                line_add_Si.append(lines1)
        line_all = line_add_Si + line_add_Li
        num_li.append(len(line_add_Li))
        num_si.append(len(line_add_Si))
        if len(line_add_Li) == 0:
            pure_li.append(1)
        elif len(line_add_Si) == 0:
            pure_si.append(1)
        if a != 0:
            if b != 0:
                ratio.append(np.float32(a/b))
        energy_value = lines[0].split(' ')[4]
        energy.append(energy_value)
        norm_energy.append(np.float32(energy_value)/int(len(line_all)))
    f.close()

energy = [np.float32(x) for x in energy]
num_li = [int(x) for x in num_li]
num_si = [int(x) for x in num_si]
matplotlib.rcParams['font.sans-serif']=['SimHei']   
matplotlib.rcParams['axes.unicode_minus']=False     

y = 3
if y == 0 :
    # ratios #
    plt.hist(ratio, bins=20, edgecolor='black')
    plt.xlabel("Li/Si Ratio")
    plt.ylabel("Frequency")
    plt.title("Histogram")
    plt.show()
elif y == 1 :
    # energy #
    plt.hist(energy, bins=20, density=False, histtype='bar', align='mid', facecolor="blue", edgecolor="black", alpha=0.7)
    plt.xlabel("Total Energy (eV)")
    plt.ylabel("Frequency")
    plt.title("Histogram")
    plt.show()
elif y == 2:
    # averaged energy #
    plt.hist(norm_energy, bins=20, edgecolor='black')
    plt.xlabel("Energy per atom")
    plt.ylabel("Frequency")
    plt.title("Histogram")
    plt.show()
elif y == 3:
    # li number #
    plt.hist(num_li, bins=20, edgecolor='black')
    plt.xlabel("Number of Li atoms")
    plt.ylabel("Frequency")
    plt.title("Histogram")
    plt.show()
elif y == 4:
    # si number #
    plt.hist(num_si, bins=20, edgecolor='black')
    plt.xlabel("Number of Si atoms")
    plt.ylabel("Frequency")
    plt.title("Histogram")
    plt.show()