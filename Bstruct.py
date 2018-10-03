#-*-coding:utf-8-*-

import base64,struct,os
#struct模块的pack()函数可以把任意的数据类型变成bytes
#unpack()函数可以把bytes变成相应的数据类型
def get_basefile(url):
    with open(url,'rb') as f:
        bmp_data = f.read(30)
        return bmp_data
        print(bmp_data)

def bmp_info(data):

    info = struct.unpack('<ccIIIIIIHH',data)
    s = info[0] + info[1]
    if s == b'BM' or s == b'BA':
        return{
            'width': info[6],
            'hight': info[7],
            'color': info[9]
        }
    else:
        print("data is not XXXX.bmp file")
        exit()
if __name__ == '__main__':
   data =  get_basefile('C:/Users/Administrator.WIN-0D6TMPD9FUH/Downloads/test.bmp')
   bi = bmp_info(data)
   print(bi)