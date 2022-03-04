from PIL import Image
import numpy as np


class Canvas:
    def __init__(self, height, width, color):
        self.color = color
        self.height = height
        self.width = width

        # Create a 3D numpy array of zeros
        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)

        # Change [0, 0, 0] with user given values for color
        self.data[:] = self.color

    def make(self, imagePath):
        """Converts the current array into an image file"""
        img = Image.fromarray(self.data, 'RGB')
        img.save(imagePath)
