# FILENAME: common_criminal_traits.py
# FILE OWNER: JOHN MICHAEL POTTER
# PROGRAM NAME: LIMS (LAB INFORMATION MANAGEMENT SYSTEM)
# CREATED ON: 6/5/2024 at 7:00pm
# LAST MODIFIED ON: 6/5/2024 at 7:08pm


import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)

plt.title("Average School Shooter Pulse", loc='center')
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.show()
