import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


with open('my_mountain_data（处理后）.txt', 'r') as f:
    data = f.readlines()

x = np.arange(64)
y = np.arange(15)
x, y = np.meshgrid(x, y)
temp_z = []
for line in data:
    line = line.split()
    temp_line = []
    for i in line:
        temp_line.append(float(i))
    temp_z.append(temp_line)
z = np.array(temp_z)

ax = plt.subplot(projection='3d')
ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap='rainbow')
ax.set_xlabel("步长（x8字节）", fontproperties='simhei')
ax.set_ylabel("大小（字节）", fontproperties='simhei')
ax.set_zlabel("读吞吐量（MB/s）", fontproperties='simhei')
ax.set_title("memory mountain \n AMD Ryzen 7 5800H \n 3.2 GHz")
x_ticks = []
for i in range(64):
    temp = "s" + str(i + 1)
    x_ticks.append(temp)
y_ticks = ["32m", "16m", "8m", "4m", "2m", "1024k", "512k", "256k", "128k", "64k", "32k", "16k", "8k", "4k", "2k"]
ax.set_xticklabels(x_ticks)
ax.set_yticklabels(y_ticks)
plt.draw()
plt.savefig('my_mountain.jpg')
plt.show()

# CPU型号 AMD Ryzen 7 5800H
# CPU主频 3.2 GHz
