import numpy as np
from PIL import Image

# Create 3D numpy array of zeros, then replace zeros (black pixels) with yellow pixels
data = np.zeros((5, 4, 3), dtype=np.uint8)
# for item in data[:]:
#     print(item)
data[:] = [255, 255, 0]
# print(data)

# Make a red patch
# data[1:3] = [255, 0, 0]     # Make red row patch
# data[:, 1:3] = [255, 0, 0]      # Make red column patch
data[1:3, 1:3] = [255, 0, 0]

img = Image.fromarray(data, 'RGB')
img.save('canvas.png')
