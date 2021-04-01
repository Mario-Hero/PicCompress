#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# Created by Mario Chen, 01.04.2021, Shenzhen
# My Github site: https://github.com/Mario-Hero

import sys
import os
from PIL import Image

SIZE_CUT = 5   # picture over this size should be compressed. Units: MB
QUALITY = 90  # 90 is good, this number should not be smaller than 80.


def isPic(name):
    namelower = name.lower()
    return namelower.endswith("jpeg") or namelower.endswith("jpg") or namelower.endswith("png")


def compressImg(file):
    #print("The size of", file, "is: ", os.path.getsize(file))
    if os.path.getsize(file) > (SIZE_CUT * 1024 * 1024):
        im = Image.open(file)
        im.save(file, quality=QUALITY)


def compress(folder):
    if os.path.isdir(folder):
        file_list = os.listdir(folder)
        for file in file_list:
            print(file)
            if os.path.isdir(file):
                compress(folder + file + "/")
            else:
                if isPic(file):
                    compressImg(folder+file)
    else:
        if isPic(folder):
            compressImg(folder)


if __name__ == '__main__':
    for folder in sys.argv:
        #print(folder)
        compress(folder)
    print("Finish.")
    os.system("pause")
