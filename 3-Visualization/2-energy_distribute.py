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
matplotlib.rcParams['font.sans-serif']=['SimHei']   # 用黑体显示中文
matplotlib.rcParams['axes.unicode_minus']=False     # 正常显示负号

y = 3
if y == 0 :
    # 比例 #
    plt.hist(ratio, bins=20, edgecolor='black')
    # 显示横轴标签
    plt.xlabel("Li/Si Ratio")
    # 显示纵轴标签
    plt.ylabel("Frequency")
    # 显示图标题
    plt.title("Histogram")
    plt.show()
elif y == 1 :
    # 能量 #
    plt.hist(energy, bins=20, density=False, histtype='bar', align='mid', facecolor="blue", edgecolor="black", alpha=0.7)
    # interval_boundaries = np.linspace(-210, -190, 20)  # Creates 10 equally spaced intervals from -204 to -194
    # plt.hist(energy, bins=interval_boundaries, edgecolor='black')  # Adjust the number of bins as needed
    # 显示横轴标签
    plt.xlabel("Total Energy (eV)")
    # 显示纵轴标签
    plt.ylabel("Frequency")
    # 显示图标题
    plt.title("Histogram")
    plt.show()
elif y == 2:
    # averaged energy #
    plt.hist(norm_energy, bins=20, edgecolor='black')
    # 显示横轴标签
    plt.xlabel("Energy per atom")
    # 显示纵轴标签
    plt.ylabel("Frequency")
    # 显示图标题
    plt.title("Histogram")
    plt.show()
elif y == 3:
    # li num #
    plt.hist(num_li, bins=20, edgecolor='black')
    # 显示横轴标签
    plt.xlabel("Number of Li atoms")
    # 显示纵轴标签
    plt.ylabel("Frequency")
    # 显示图标题
    plt.title("Histogram")
    plt.show()
elif y == 4:
    # si num #
    plt.hist(num_si, bins=20, edgecolor='black')
    # 显示横轴标签
    plt.xlabel("Number of Si atoms")
    # 显示纵轴标签
    plt.ylabel("Frequency")
    # 显示图标题
    plt.title("Histogram")
    plt.show()