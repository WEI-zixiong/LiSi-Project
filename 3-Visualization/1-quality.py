#%%
import numpy as np
import pandas as pd
import re
import matplotlib.pyplot as plt

errors1 = []
errors2 = []
errors3 = []
errors = []
with open(r"E:\file\...\train.out1") as fp1:
    for line in fp1:
        # m = re.search(r'(?<=\|)',line)
        # print(m)
        if re.match("^ *[0-9].* \|+", line):
            # print(line)
            # print(type(line))
            a1 = re.split(r'\W+\.?\W', line)
            # print(a1)
            # print(type(a1))
            b1 = a1[2:6]
            # print(b1)
            errors1.append(b1)
            # errors.append([float(a) for a in line.split()[1:-1]])
errors1 = np.array(errors1)
with open(r"E:\file\...\train.out2") as fp2:
    for line in fp2:
        if re.match("^ *[0-9].* \|+", line):
            a2 = re.split(r'\W+\.?\W', line)
            b2 = a2[2:6]
            errors2.append(b2)
errors2 = np.array(errors2)
with open(r"E:\file\...\train.out3") as fp3:
    for line in fp3:
        if re.match("^ *[0-9].* \|+", line):
            a3 = re.split(r'\W+\.?\W', line)
            b3 = a3[2:6]
            errors3.append(b3)
errors3 = np.array(errors3)
errors = np.vstack((errors1, errors2, errors3))
errors = pd.DataFrame(
    data=errors,
    columns=['ERROR(train)', 'ERROR(test)', 'E(train)', 'E(test)'])
errors = errors.astype(float)
# print(errors)
# print(type(errors))
# print(errors.size)
# print(errors.shape)
# print(errors.ndim)

# print(errors[['ERROR(train)', 'ERROR(test)']])
# ax = errors[['ERROR(train)', 'ERROR(test)']].plot(logy=True)
# ax.set_xlabel("Epoch"); ax.set_ylabel("ERROR (Ha/atom)")
# plt.show()

errors.plot(None, y = ['ERROR(train)', 'ERROR(test)'], kind = 'line', logy = True)
plt.xlabel('Epoch'); plt.ylabel('ERROR (Ha/atom)')
plt.legend()
plt.show()

fp1.close()
fp2.close()
fp3.close()

#%%
import os
import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

path = r'E:\file\...'
path_list = os.listdir(path)
num = []
regex = re.compile(r'\w+\.+out+\d$')
for i in path_list:
    num += regex.findall(i)
po = []
path_out = r'E:\file\...\{}'
for i in list(range(len(num))):
    po.append(path_out.format(num[i]))
errors = []
for i in list(range(len(num))):
    with open(po[i]) as fp:
        for line in fp:
            if re.match("^ *[0-9].* \|+", line):
                ai = re.split(r'\W+\.?\W', line)
                bi = ai[2:6]
                errors.append(bi)
errors = np.array(errors)
errors = pd.DataFrame(
    data=errors,
    columns=['ERROR(train)', 'ERROR(test)', 'E(train)', 'E(test)'])
errors = errors.astype(float)
errors.plot(None, y = ['ERROR(train)', 'ERROR(test)'], kind = 'line', logy = True, linewidth=3)
plt.xlabel('Epoch', fontsize=20); plt.ylabel('ERROR (eV/atom)', fontsize=20)
plt.legend(fontsize=20)
plt.show()
fp.close()

#%%
import numpy as np
import pandas as pd
import re
import matplotlib.pyplot as plt

errors = []
with open("t.txt") as fp:
  for line in fp:
    if re.match("^ *[0-9].*<$", line):
      errors.append([float(a) for a in line.split()[1:-1]])
errors = np.array(errors)
print(errors)
print(type(errors))
print(errors.size)
print(errors.shape)
print(errors.ndim)
errors = pd.DataFrame(
    data=errors,
    columns=['MAE_train', 'RMSE_train', 'MAE_test', 'RMSE_test'])
print(errors)
print(type(errors))
print(errors.size)
print(errors.shape)
print(errors.ndim)
ax = errors[['RMSE_train', 'RMSE_test']].plot(logy=True)
ax.set_xlabel("Epoch"); ax.set_ylabel("RMSE (Ha/atom)")
plt.show()

#%%
import numpy as np
import pandas as pd
import re
import matplotlib.pyplot as plt

test = r"E:\file\...\energies.test"
test_errors = np.loadtxt(test, skiprows=1, usecols=(3,4))
limits = np.linspace(-0.5, 0.8)
plt.plot(limits, limits, color="black", linewidth=3)
plt.ticklabel_format(useOffset=False)
plt.scatter(test_errors[:,0], test_errors[:,1], color="red", s=30, label="validation")
plt.xlabel('DFT (eV/atom)', fontsize=20)
plt.ylabel('ANN (eV/atom)', fontsize=20)
plt.show()