import pyabf
import os 
import matplotlib.pyplot as plt
import numpy as np

current_dir = os.path.dirname(__file__)
relative_path = "../Cell1/20220729_Cell1_0001.abf"
abf = pyabf.ABF(os.path.join(current_dir, relative_path))
print(abf)
# plt.figure(figsize=(8, 5))
# plt.title(f"<exp title> <cell_id>")
# plt.ylabel(abf.sweepLabelY)
# plt.xlabel(abf.sweepLabelX)
# for i in abf.sweepList:
#     abf.setSweep(i, baseline=[0.0, 0.1])
#     plt.plot(abf.sweepX, abf.sweepY, alpha=.5, label="sweep %d" % (i))
# plt.legend()
# plt.show()
x_unit = 5e-05
start_l = 0.1640
start_r = 0.1740
end_l = 2.1350
end_r = 2.1450
start_l_idx = int(start_l // x_unit)
start_r_idx = int(start_r // x_unit)
end_l_idx = int(end_l // x_unit)
end_r_idx = int(end_r // x_unit) 

for i in abf.sweepList:
    abf.setSweep(i, baseline=[0.0, 0.1])
    start_avg = np.mean(abf.sweepY[start_l_idx:start_r_idx])
    end_avg = np.mean(abf.sweepY[end_l_idx:end_r_idx])
    print(f'sweep {i}')
    print(f'start = {start_avg}, end = {end_avg}, delta = {start_avg - end_avg}')
