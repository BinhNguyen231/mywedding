import os
import cv2

p_raw = "..\\..\\anh_da_chinh_sua\\anh_le"
for image in os.listdir(p_raw):
    img = cv2.imread(os.path.join(p_raw, image))
    h,w,_ = img.shape
    min_shape = 1080
    ratio = h/w
    new_h, new_w = 0,0
    if h<w:
        new_h = 1080
        new_w = int(new_h/ratio)
    else:
        new_w = 1080
        new_h = int(new_w * ratio)
    new_img = cv2.resize(img, (new_w, new_h))
    cv2.imwrite(os.path.join("..\\..\\anh_da_chinh_sua\\anh_le_resize", image), new_img)

