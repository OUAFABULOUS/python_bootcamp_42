import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import numpy as np

class	ImageProcessor:
    def	load(path):
        img = Image.open(path)
        # print(img)
        # img = mping.open(path)
        print(f"{img.width}x{img.height}")
        arr = np.array(img)
        return(arr)

    def	display(array):
        img = Image.fromarray(array, 'RGB')
        img.show()

if 	__name__=="__main__":
    imp = ImageProcessor
    imp.display(imp.load("sTrlc.png"))
