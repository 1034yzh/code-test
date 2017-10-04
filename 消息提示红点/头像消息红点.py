# 引入Pillow
from PIL import Image, ImageDraw, ImageFont, ImageColor
def add_num(img):
    # 创建一个Draw对象
    draw = ImageDraw.Draw(img)
    # 创建一个 Font
    myfont = ImageFont.truetype('C:/windows/fonts/Arial.ttf', size=40)
    # 创建一个fill
    fillcolor = ImageColor.colormap.get('red')
    (width, height) = img.size
    draw.text((width-20, 0), '1', font=myfont, fill=fillcolor)
    img.save('result.png')
    return 0
if __name__ == '__main__':
    img=input("请输入图片名：")
    image = Image.open(img)
    add_num(image)
# imagefont主要是设置字体类型以及大小
# imagecolor主要是获取red颜色
# draw.text参数分别为文本位置，文本内容，文本字体类型及大小，文本字体颜色 
