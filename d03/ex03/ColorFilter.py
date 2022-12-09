from ImageProcessor import ImageProcessor as ip
import numpy as np

class	ColorFilter:
    def	invert(arr):
        try:
            inverted_arr = 255 - arr
            # inverted_arr = np.invert(arr)
            # ip.display(inverted_arr)
            # print(type(inverted_arr))
            return(inverted_arr)
        except:
            return None

    def to_blue(arr):
        try:
            blue_arr = arr.copy()
            blue_arr[:, :, (0, 1)] = 0
            # ip.display(blue_arr)
            return(blue_arr)
        except:
            return None

    def to_green(arr):
        try:
            green_arr = arr.copy()
            green_arr[:, :, (0, 2)] = 0
            # ip.display(green_arr)
            return(green_arr)
        except:
            return None

    def to_red(arr):
        try:
            red_arr = arr.copy()
            red_arr[:, :, (1, 2)] = 0
            # ip.display(red_arr)
            return(red_arr)
        except:
            return None

    def to_grayscale(arr):
        # try:
        rgb = arr[:, :, (0,1,2)]

        # rgb_average = rgb.sum(0)
        print(f"rgb shape: {rgb.shape} rgb len: {len(rgb[0])}")
        # new_arr = arr[:, :, 0]
        # print(f"shape: {new_arr.shape}")
        # ip.display(gray_arr)

        # print(arr_cpy.shape)
        # print(f"arr: {len(arr)} {len(arr[0])}")
        # print(f"len of grayscale array: {len(gray_arr)} {len(gray_arr[0])}")
        # print(arr.shape)
        # except:
            # return None





if	__name__=="__main__":
    loaded_arr = ip.load("sTrlc.png")
    print(loaded_arr.shape)
    # ColorFilter.invert(loaded_arr)
    # ColorFilter.to_blue(loaded_arr)
    # ColorFilter.to_green(loaded_arr)
    # ColorFilter.to_red(loaded_arr)
    ColorFilter.to_grayscale(loaded_arr)
