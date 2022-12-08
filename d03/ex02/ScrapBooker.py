import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import numpy as np
import os

class	ImageProcessor:
    def	load(path):
        if not os.path.exists(path):
            return None
        img = Image.open(path)
        print(f"{img.width}x{img.height}")
        arr = np.array(img)
        return(arr)

class	ScrapBooker:
    def	crop(arr, dim, position=(0,0)):
        try:
            img = Image.fromarray(np.uint8(arr)).convert('RGB')
            crop_image = img.crop((position[0], position[1], position[0] + dim[0], position[1] + dim[1]))
            return(np.array(crop_image))
        except:
            return None

    def	thin(arr, n, axis):
        try:
            new_arr = np.delete(arr, list(range(0, arr.shape[axis], n)), axis)
            return(new_arr)
        # img = Image.fromarray(np.uint8(new_arr)).convert('RGB')
        # img.show()
        except:
            return None

    def	juxtapose(arr, n, axis):
        # try:
        new_arr = arr
        for i in range(n - 1):
            new_arr = np.concatenate((new_arr, arr), axis)
        # img = Image.fromarray(np.uint8(new_arr)).convert('RGB')
        # img.show()
        return new_arr

    def	mosaic(self, arr, dim):

        new_arr1 = self.juxtapose(arr,dim[0],0)
        new_arr2 = self.juxtapose(new_arr1,dim[1],1)
        # img = Image.fromarray(np.uint8(new_arr2)).convert('RGB')
        # img.show()
        return new_arr2


if __name__=="__main__":
    ip = ImageProcessor
    arr = ip.load("sTrlc.png")
    sb = ScrapBooker
    # sb = sb.crop(arr,[100,100],(0,0))
    # sb.thin(arr, 2, 1)
    # sb.juxtapose(arr, 4, 0)
    # sb.mosaic(sb,arr,(10,4))


