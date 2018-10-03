#-*-coding:utf-8 -*-

from PIL import Image,ImageFilter,ImageDraw,ImageFont
'''
im = Image.open('E:/微信宣传稿/图片/Image/1.jpg')
w,h = im.size
print('Original image size:%sx%s'% (w,h))
#缩放到%50
im.thumbnail((w/2,h/2))
print('Resize image size:%sx%s'%(w/2,h/2))
#ImageFIlter.BLUR加滤镜
im2 = im.filter(ImageFilter.BLUR)
im.save('E:/微信宣传稿/图片/Image/2.jpg')
im2.save('E:/微信宣传稿/图片/Image/3.jpg')
im2.show()
'''
#制作字母验证图片
import random

#生成随机字母
def ranChar():
    return chr(random.randint(65,90))

#随机颜色
def randColor():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))

def randColor2():
    return (random.randint(32,125),random.randint(32,125),random.randint(32,125))

width  = 240
height = 60
image = Image.new('RGB',(width,height),(2555,255,255))
#创建Font对象
font = ImageFont.truetype('C:/Windows/WinSxS/amd64_microsoft-windows-font-truetype-arial_31bf3856ad364e35_10.0.17134.1_none_5803fc87168579d6/arial.ttf',36)

#创建Drow对象
draw = ImageDraw.Draw(image)
#填充每个像素
for x in range(width):
    for y in range(height):
        draw.point((x,y),fill = randColor())

#输出文字
for t in range(4):
    draw.text((60 * t,20),ranChar(),font = font,fill = randColor())

image = image.filter(ImageFilter.BLUR)
image.save('E:/微信宣传稿/图片/Image/code.jpg')
image.show()