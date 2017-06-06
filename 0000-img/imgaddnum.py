from PIL import Image,ImageFont,ImageDraw
import random

def imgaddnum(im):  
    w,h=im.size
    font=ImageFont.truetype('Arial.ttf',100)
    draw=ImageDraw.Draw(im)
    draw.text((w-80,0),'4',font=font,fill=(255,0,0))
    draw.ellipse((0,0,100,100),fill=(255,0,0))
    draw.arc((100,100,200,200),0,180,fill=(255,0,0))
    im.save('test.jpg','jpeg')

if __name__ == '__main__':
    im = Image.open('huaji.jpg')
    imgaddnum(im)