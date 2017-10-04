from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

def white_to_transparent(img):
    img=img.convert('RGBA') #返回一个转换后的图像的副本
    datas=img.getdata()
    newData=[]
    for item in datas:
        if item[0]==255 and item[1]==255:
            newData.append((255,255,255,0))
        else:
            newData.append(item)
    img.putdata(newData)    #赋给图片新的像素数据
    img.save("121.png")
    return img

if __name__=="__main__":

    p1_name="target_img.png"#目标图片名称
    p2_name="redpoint_img.png"#红点图片名称
    #打开两张png图片，注意为当前路径
    p1_image=Image.open(p1_name)
    p2_image=Image.open(p2_name)
    p2_transparent=white_to_transparent(p2_image)
    p1_image.paste(p2_transparent,(0,0),p2_transparent)#第二个p2_transparent是掩码图像

    usr_font=ImageFont.truetype("C:/windows/fonts/Arial.ttf",32)
    draw=ImageDraw.Draw(p1_image) #在p1_image上绘制文字，图像
    draw.text((152,8),u'12',font=usr_font)
    p1_image.save("final_img.png","PNG")
