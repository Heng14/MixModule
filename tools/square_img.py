import os
import os.path as osp
import numpy as np
from skimage.io import imsave, imread

def basename(f):
    return osp.splitext(f)[0]

def gif2png_drive(in_p='img', in_m='mask2'):

    out_p = in_p.split('/')[0] + '_square'
    out_m = in_m.split('/')[0] + '_square'
    
    os.makedirs(out_p, exist_ok=True)
    os.makedirs(out_m, exist_ok=True)

    imgs = os.listdir(in_p)
    for f in imgs:
        f_path = osp.join(in_p, f)
        m_path = osp.join(in_m, basename(f)+'_2ndHO.png')

        im = imread(f_path)
        im_m = imread(m_path)
        img = np.array(im)
        mask = np.array(im_m)

        img_cut = img[:, 19:979]
        mask_cut = mask[:, 19:979]

        out_p_path = osp.join(out_p, f)
        out_m_path = osp.join(out_m, basename(f)+'.png')

        imsave(out_p_path, img_cut)
        imsave(out_m_path, mask_cut)

if __name__ == '__main__':
    import fire
    fire.Fire(gif2png_drive)

