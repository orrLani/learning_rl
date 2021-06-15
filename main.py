


from matplotlib import pyplot as plt
import numpy as np

fig1 = plt.figure()
ax = fig1.add_subplot(111)
cbaxes = fig1.add_axes([0.8, 0.1, 0.03, 0.8])
for i in range(100):
    temp = np.random.normal(0, 1, size=(10,10))
    im1 = ax.imshow(temp, cmap='coolwarm', aspect='equal')
    if i == 0:
        cbar = plt.colorbar(im1, cax = cbaxes)
    else:
        cbar.update_normal(im1)
    plt.pause(0.00000001)