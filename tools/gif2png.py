import os
import os.path as osp
import numpy as np
from PIL import Image
from skimage.io import imsave, imread

def basename(f):
    return osp.splitext(f)[0]

def gif2png_drive(in_p):
    out_p = in_p.split('/')[0] + '_png'
    os.makedirs(out_p, exist_ok=True)
    imgs = os.listdir(in_p)
    for f in imgs:
        f_path = osp.join(in_p, f)

        im = Image.open(f_path)
        img = np.array(im)
        if len(img.shape) == 3:
            out_path = osp.join(out_p, basename(f)+'.jpg')
            img0 = np.zeros((576,576,3), dtype='u1')

        elif len(img.shape) == 2:
            out_path = osp.join(out_p, basename(f)+'.png')
            img0 = np.zeros((576,576), dtype='u1')
        img0[:,5:570] = img[4:580,:]
        imsave(out_path, img0)


def gif2png_luna(in_p):    
    out_p = in_p.split('/')[0] + '_png'
    os.makedirs(out_p, exist_ok=True)
    imgs = os.listdir(in_p)
    for f in imgs:
        f_path = osp.join(in_p, f)
        im = Image.open(f_path)
        img = np.array(im)
        #out_path = osp.join(out_p, basename(f)+'.jpg')
        out_path = osp.join(out_p, basename(f)+'_segmentation.png')
        imsave(out_path, img)


if __name__ == '__main__':
    import fire
    fire.Fire(gif2png_luna)

