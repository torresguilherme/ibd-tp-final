from PIL import Image
from PIL.ImageColor import getcolor, getrgb
from PIL.ImageOps import grayscale
from PIL import ImageEnhance
import random
import os
import math
#From: https://stackoverflow.com/questions/29332424/changing-colour-of-an-image/29379704#29379704
def image_tint(src, tint='#fffab5'):
    if Image.isStringType(src):  # file path?
        src = Image.open(src)
    if src.mode not in ['RGB', 'RGBA']:
        raise TypeError('Unsupported source image mode: {}'.format(src.mode))
    src.load()

    tr, tg, tb = getrgb(tint)
    tl = getcolor(tint, "L")  # tint color's overall luminosity
    if not tl: tl = 1  # avoid division by zero
    tl = float(tl)  # compute luminosity preserving tint factors
    sr, sg, sb = map(lambda tv: tv/tl, (tr, tg, tb))  # per component
                                                      # adjustments
    # create look-up tables to map luminosity to adjusted tint
    # (using floating-point math only to compute table)
    luts = (tuple(map(lambda lr: int(lr*sr + 0.5), range(256))) +
            tuple(map(lambda lg: int(lg*sg + 0.5), range(256))) +
            tuple(map(lambda lb: int(lb*sb + 0.5), range(256))))
    l = grayscale(src)  # 8-bit luminosity version of whole image
    if Image.getmodebands(src.mode) < 4:
        merge_args = (src.mode, (l, l, l))  # for RGB verion of grayscale
    else:  # include copy of src image's alpha layer
        a = Image.new("L", src.size)
        a.putdata(src.getdata(3))
        merge_args = (src.mode, (l, l, l, a))  # for RGBA verion of grayscale
        luts += tuple(range(256))  # for 1:1 mapping of copied alpha values
    return Image.merge(*merge_args).point(luts)
##

skintones = [
        "#fcf6bf",
        "#fff1c1",
        "#e5c175",
        "#664921",
        "#28130e"
        ]

haircolor = [
        "#303030",
        "#592828",
        "#c40101",
        "#ff9a02",
        "#ffe882",
        "#fff8cc"
        ]
def get_random_file_in_dir(directory):
    choices = []
    for i in directory:
        filelist = os.listdir(i)
        for j in filelist:
            if(os.path.isfile(os.path.join(i,j))):
                choices.append(os.path.join(i,j))
        
    file = random.choice(choices)
    return file

def get_random_file_for_genre(basedir,genre):
    return (get_random_file_in_dir([basedir,os.path.join(basedir,genre)]))
def generate_user(genre):
    img = Image.open(get_random_file_for_genre("Art/Face",genre))
    nose = Image.open(get_random_file_for_genre("Art/Nose",genre))
    mouth = Image.open(get_random_file_for_genre("Art/Mouth",genre))
    eyes = Image.open(get_random_file_for_genre("Art/Eyes",genre))
    hair = Image.open(get_random_file_for_genre("Art/Hair",genre))
    has_accessory = random.random()
    has_beard = random.random()
    hairtone = random.randint(0,len(haircolor) - 1)
    tintHair = image_tint(hair,haircolor[hairtone])
    #result = image_tint(img,skintones[random.randint(0,len(skintones) - 1)])
    skintone = random.randint(0,len(skintones) - 1)
    result = image_tint(img,skintones[skintone])
    
    bright = ImageEnhance.Brightness(result)
    brightnessFactor = random.uniform(0.6, 1)
    result = bright.enhance(brightnessFactor)
    color = ImageEnhance.Color(result)
    result = color.enhance(0.4 + (brightnessFactor))
    
    
    hairbright = ImageEnhance.Brightness(tintHair)
    tintHair = hairbright.enhance(brightnessFactor - 0.1)
    contrast = ImageEnhance.Contrast(tintHair)
    tintHair = contrast.enhance(0.2 + (brightnessFactor))
    #pixels = img.load() # create the pixel map
    
    #for i in range(img.size[0]):    # for every col:
    #    for j in range(img.size[1]):    # For every row
    #        pixels[i,j] = (i, j, 100) # set the colour accordingly
    if(genre == "F"):
        offset = (0,-1)
    else:
        offset = (0,0)
    result.paste(eyes,offset,eyes)
    result.paste(mouth,offset,mouth)
    result.paste(nose,offset,nose)
    result.paste(tintHair,(0,0),tintHair)
    if(has_accessory > 0.5):
        accessory = Image.open(get_random_file_for_genre("Art/Accessories",genre))
        result.paste(accessory,(0,0),accessory)
    if(has_beard > 0.6):
        beard = Image.open(get_random_file_for_genre("Art/Beard",genre))
        beard = image_tint(beard,haircolor[hairtone])
    
        hairbright = ImageEnhance.Brightness(beard)
        beard = hairbright.enhance(brightnessFactor)
        contrast = ImageEnhance.Contrast(beard)
        beard = contrast.enhance(0.2 + (brightnessFactor))
        result.paste(beard,(0,0),beard)
    return result

amt = 80
column_amount  = 10
image_width = 32
image_height= 48
row_amount = math.ceil(amt/column_amount)
print("ROWS:")
print(row_amount)
img = Image.new('RGB', (image_width * column_amount,image_height * row_amount), (255, 255, 255))
genres = ["M","F"]
for i in range(amt):
    
    result = generate_user(random.choice(genres))
    result.save("UserImg/img"  + str(i) + ".png")
    img.paste(result,((i%(column_amount)) * image_width,math.floor(i/column_amount) * image_height),result)
img.save("tmp.png")
#img.show()