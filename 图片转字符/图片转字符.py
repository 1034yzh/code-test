from PIL import Image

img=input("请输入图片名称：")
ascii_char = list("@*,'.  ")
# $@B%8&WM#*;:,'.                  
#$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'.  
# 将256灰度映射到7字符上  
def get_char(r, b, g, alpha=256):  
    if alpha == 0:  
        return ' '  
    length = len(ascii_char)  
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)#灰度映射公式
  
    unit = (256.0 + 1)/length  
    return ascii_char[int(gray/unit)]

if __name__ == '__main__':
    im = Image.open(img)
    print(im.size)
    i=im.size[0]/im.size[1]
    if i>1:
        x=100
        y=int(100/i)
    else:
        y=100
        x=int(100*i)
    im = im.resize((100,100), Image.NEAREST)
    
    txt = ""  
  
    for i in range(100):  
        for j in range(100):  
            txt += get_char(*im.getpixel((j, i)))  
        txt += '\n'  
  
    print(txt)
	
	# 字符画输出到文件    
    with open("output.txt", 'w') as f:  
            f.write(txt)  
