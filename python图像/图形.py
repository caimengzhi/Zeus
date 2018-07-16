#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""
@author: caimengzhi
@license: (C) Copyright 2013-2017.
@contact: 610658552@qq.com
@software: pycharm 2017.02
@project: cmz
@file: 图形.py
@time: 2018/7/16 17:34
@desc:  test on python3.x
"""
# from PIL import Image, ImageFont, ImageDraw
# text = "EwWIieAT"
# im = Image.new("RGB",(130,35), (255, 255, 255))
# dr = ImageDraw.Draw(im)
# font = ImageFont.truetype("msyh.ttf", 24)
# #simsunb.ttf 这个从windows fonts copy一个过来
# dr.text((10, 5), text, font=font, fill="#000000")
# im.show()
# im.save("t.png")

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random


# 随机字母:
def rndChar():
    return chr(random.randint(65, 90))


# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


# 240 x 60:
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象:
font = ImageFont.truetype('msyh.ttf', 36)
# 创建Draw对象:
draw = ImageDraw.Draw(image)
# 填充每个像素:
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
# 输出文字:
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
# 模糊:
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')
image.show()


# python3 图形.py
# 然后输出随机字符串
