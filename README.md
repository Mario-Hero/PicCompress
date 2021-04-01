# ppicComp

批量图像压缩python脚本

把文件夹或图片直接拖入即可。

Python script for batch image compression 

Just drag the folder or pictures into it.



## 需要 Needs

Python 3

Pillow (用pip install pillow来安装即可)



## 用法 Usage

把文件夹或图片直接拖入即可。如果拖入的是文件夹，则会贯穿子文件把所有图片都压缩了。



**注意，压缩后的文件会直接替换原来的文件。**



文件的开头有两个变量：

SIZE_CUT = 5 表示大于5MB的图片都会进行压缩

QUALITY = 90 表示压缩质量90，这个质量基本人眼是看不出来啥差距的，而且很多原先10M的图能压缩一半。80以下的质量大概就不太行了。





