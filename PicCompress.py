#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# Created by Mario Chen, 01.04.2021, Shenzhen
# My Github site: https://github.com/Mario-Hero

import sys
import os
try:
    from PIL import Image
except ImportError:
    os.system('pip install pillow')
    from PIL import Image

# you can change it >>>>>

SIZE_CUT = 6   # picture over this size should be compressed. Units: MB
QUALITY = 95  # 95 is good, this number should not be smaller than 80.
DEFAULT_TARGET = ''

# <<<<< you can change it


SIZE_CUT_B = SIZE_CUT * 1024 * 1024
spaceSavedThisTime = 0
spaceNotSavedTime = 0

def isPic(name):
    namelower = name.lower()
    return namelower.endswith("jpg") or namelower.endswith("jpeg") or namelower.endswith("png")


def fileRename(file, n):
    pathName, fileName = os.path.split(file)
    if '.' in fileName:
        cutPos = fileName.rfind('.')
        return os.path.join(pathName, fileName[:cutPos] + '(' + str(n) + ')' + fileName[cutPos:])
    else:
        return os.path.join(pathName, fileName + '(' + str(n) + ')')


def compressImg(file):
    global spaceSavedThisTime, spaceNotSavedTime
    #print("The size of", file, "is: ", os.path.getsize(file))
    im = Image.open(file)
    i = 1
    originalName = file
    moveTemp = fileRename(file, i)
    while os.path.exists(moveTemp):
        i += 1
        moveTemp = fileRename(originalName, i)
    im.save(moveTemp, quality=QUALITY)
    spaceSaved = os.path.getsize(file) - os.path.getsize(moveTemp)
    if spaceSaved > 1024 * 1024:   # save > 1MB
        os.remove(file)
        os.rename(moveTemp, file)
        spaceSavedThisTime = spaceSavedThisTime + spaceSaved/(1024*1024)
    else:
        spaceNotSavedTime += 1
        os.remove(moveTemp)


def compress(folder):
    global spaceNotSavedTime
    try:
        if os.path.isdir(folder):
            spaceNotSavedTime = 0
            print(folder)
            file_list = os.listdir(folder)
            for file in file_list:
                temp = os.path.join(folder, file)
                if os.path.isdir(temp):
                    # print(temp)
                    compress(temp)
                else:
                    if isPic(file):
                        if spaceNotSavedTime > 5:
                            break
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
    if len(sys.argv) > 1:
        for folder in sys.argv[1:]:
            #print(folder)
            compress(folder)
    elif DEFAULT_TARGET:
        compress(DEFAULT_TARGET)
    print(" ")
    print("Finish.")
    print("Save " + str(round(spaceSavedThisTime,1)) + " MB.")
    #os.system("pause")
