#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# Created by Mario Chen, 01.04.2021, Shenzhen
# My Github site: https://github.com/Mario-Hero

import sys
import os
from PIL import Image

SIZE_CUT = 6   # picture over this size should be compressed. Units: MB
QUALITY = 90  # 90 is good, this number should not be smaller than 80.



SIZE_CUT_B = SIZE_CUT * 1024 * 1024


def isPic(name):
    namelower = name.lower()
    return namelower.endswith("jpg") or namelower.endswith("jpeg") or namelower.endswith("png")


def compressImg(file):
    #print("The size of", file, "is: ", os.path.getsize(file))
    im = Image.open(file)
    im.save(file, quality=QUALITY)


def compress(folder):
    try:
        if os.path.isdir(folder):
            print(folder)
            file_list = os.listdir(folder)
            for file in file_list:
                temp = os.path.join(folder, file)
                if os.path.isdir(temp):
                    # print(temp)
                    compress(temp)
                else:
                    if isPic(file):
                        if os.path.getsize(temp) > SIZE_CUT_B:
                            compressImg(temp)
                            print(file)
        else:
            if isPic(folder):
                if os.path.getsize(folder) > SIZE_CUT_B:
                    compressImg(folder)
    except BaseException:
        return


if __name__ == '__main__':
    for folder in sys.argv[1:]:
        #print(folder)
        compress(folder)
    print("Finish.")
    #os.system("pause")
