from PIL import Image as im
import os

""" Image Stitcher
Simple image Stitcher.
"""
def stitcher_v(im1, im2, file_name="derivation", padding = 10, ext = ""):
    im1, im2 = im.open(str(im1) + ext), im.open(str(im2) + ext)
    size1, size2 = im1.size, im2.size
    size = [max(size1[i], size2[i]) for i in range(2)]
    size[1] = size1[1] + size2[1]
    new_img = im.new("RGBA", (size[0]+padding, size[1]+ padding), "white")
    new_img.paste(im1, (0+int(padding/2), 0+int(padding/2), size1[0]+int(padding/2), size1[1]+int(padding/2)))
    new_img.paste(im2, (0+int(padding/2), size1[1]+int(padding/2), size2[0]+int(padding/2), size1[1]+size2[1]+int(padding/2)))
    new_img.save(file_name, "png")

# stitcher_h("1.png", "2.png", file_name="both.png")
# stitcher("1", "2", file_name="derivation2")

""" Image Stitcher
Simple image Stitcher. [HORIZONTAL]
"""
def stitcher_h(im1, im2, file_name="derivation", padding = 10, ext = ""):
    im1, im2 = im.open(str(im1) + ext), im.open(str(im2) + ext)
    size1, size2 = im1.size, im2.size
    size = [max(size1[i], size2[i]) for i in range(2)]
    size[0] = size1[0] + size2[0]
    new_img = im.new("RGBA", (size[0]+padding, size[1]+ padding), "white")
    new_img.paste(im1, (0+int(padding/2), 0+int(padding/2), size1[0]+int(padding/2), size1[1]+int(padding/2)))
    new_img.paste(im2, (size1[0]+int(padding/2),0+ int(padding/2)))
    new_img.save(file_name, "png")



def resize(im1, size=(650,473)):
    img = im.open(im1)
    print(img.size)
    img.resize(size).save(im1)

def vert_imgs_stitcher():
    dirs = os.listdir()
    new_img = im.new("RGBA", (1, 1), "white")
    new_img.save("All" + ".png", "png")
    for item in dirs:
        if "png" not in item:
            continue
        stitcher_v("All.png", item, file_name="All.png")

def files_rename(name="week5_"):
    dirs = os.listdir()
    i = 0
    for item in dirs:
        if "png" not in item:
            continue
        os.rename(item, name+str(i)+".png")
        i+=1


#ni.paste(img, (0+10, 0+10), size1[0]+int(padding/2), size1[1]+int(padding/2))