import torch
import numpy as np


class BatchColorize(object):
    def __init__(self, n=40):
        self.cmap = color_map(n)
        self.cmap = torch.from_numpy(self.cmap[:n])

    def __call__(self, gray_image):
        size = gray_image.shape
        color_image = np.zeros((size[0], 3, size[1], size[2]), dtype=np.float32)

        for label in range(0, len(self.cmap)):
            mask = (label == gray_image)
            color_image[:,0][mask] = self.cmap[label][0]
            color_image[:,1][mask] = self.cmap[label][1]
            color_image[:,2][mask] = self.cmap[label][2]

        # handle void
        mask = (255 == gray_image)
        color_image[:,0][mask] = color_image[:,1][mask] = color_image[:,2][mask] = 255

        return color_image

def color_map(N=256, normalized=True):
    def bitget(byteval, idx):
        return ((byteval & (1 << idx)) != 0)

    dtype = 'float32' if normalized else 'uint8'
    cmap = np.zeros((N, 3), dtype=dtype)
    for i in range(N):
        r = g = b = 0
        c = i
        for j in range(8):
            r = r | (bitget(c, 0) << 7-j)
            g = g | (bitget(c, 1) << 7-j)
            b = b | (bitget(c, 2) << 7-j)
            c = c >> 3

        cmap[i] = np.array([r, g, b])

    cmap = cmap/255 if normalized else cmap
    return cmap