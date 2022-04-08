# PicCompress 图片批量压缩

图片批量压缩Python脚本。

把文件夹或图片直接拖入脚本即可。

Python script for batch image compression 

Just drag folders or pictures intothe script.



## 依赖 Dependency

Python 3

Pillow （如果没有安装，该脚本会自动安装 If not installed, the script will automatically install it.）



## 用法 Usage

把文件夹或图片直接拖入脚本PicCompress.py即可。如果拖入的是文件夹，则会遍历子文件夹把所有图片都压缩了。

**注意，压缩后的文件会直接替换原来的文件，文件名不变，尺寸不变，只改变压缩质量。**

Just drag folders or pictures into the script *PicCompress.py*. If you drag a folder into it,  the subfolders and pictures will all be compressed.
**Noted that the compressed files will take the place of the original files. The file name and resolution remain unchanged, and only the compression quality will be changed.**



## 参数 Parameters

文件的开头有两个参数：

SIZE_CUT = 6 表示大于6MB的图片都会进行压缩

QUALITY = 95 表示压缩质量95，这个质量基本上就是最好的了，人像基本就是这个质量，如果要求不高可以降低到90，人眼基本看不出差距。

DEFAULT_TARGET 表示默认的压缩目标，即双击打开该脚本所要压缩的目标，可以是文件或文件夹地址。

There are two parameters at the beginning of the file:
SIZE_CUT = 6  means that pictures larger than 6MB will be compressed
QUALITY = 95 indicates that the compression quality is 95. This quality is almost the best. 
DEFAULT_TARGET indicates the default compression target if you don't drag any files or folders into the script, which can be address of a file or folder.



