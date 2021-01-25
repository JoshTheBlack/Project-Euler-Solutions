# coding=utf-8
# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers. (in 13.txt)
import os, time
import numpy as np

t0 = time.time()
data = np.transpose(np.loadtxt(os.path.join(os.sys.path[0], "13.txt"), skiprows=0, delimiter=" "))
total = 0

for i in data:
    total += int(i)

print(str(total)[0:10])
t1 = time.time()
print(f"This calculation took {t1-t0} seconds.") # Display time elapsed during calculation.