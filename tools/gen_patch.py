import os
import os.path as osp
import numpy as np
from skimage.io import imsave, imread

def basename(f):
    return osp.splitext(f)[0]


def gen_train_patch(f, f_path, m_path, out_img_p, out_mask_p):

    print (f'processing {f} ...')

    os.makedirs(out_img_p, exist_ok=True)
    os.makedirs(out_mask_p, exist_ok=True)
    img = imread(f_path)
    mask = imread(m_path)
    h, w, _ = img.shape
    h0, w0 = mask.shape

    assert (h, w) == (h0, w0), 'img and mask shape not equal !!!'
    for i in range(0, h-48, 15):
        for j in range(0, w-48, 15):
            mask_patch = mask[i:i+48,j:j+48]
            if mask_patch.max()!=0:
                img_patch = img[i:i+48,j:j+48]
                img_p = osp.join(out_img_p, f.split('.')[0]+f'_{i}_{j}.jpg')
                mask_p = osp.join(out_mask_p, f.split('.')[0]+f'_{i}_{j}_segmentation.png')
                imsave(img_p, img_patch)
                imsave(mask_p, mask_patch)


def gen_test_patch(f, f_path, m_path, out_img_p, out_mask_p):

    print (f'processing {f} ...')

    os.makedirs(out_img_p, exist_ok=True)
    os.makedirs(out_mask_p, exist_ok=True)
    img = imread(f_path)
    mask = imread(m_path)
    h, w, _ = img.shape
    h0, w0 = mask.shape

    assert (h, w) == (h0, w0), 'img and mask shape not equal !!!'
    for i in range(0, h, 48):
        for j in range(0, w, 48):

            mask_patch = mask[i:i+48,j:j+48]
            if mask_patch.max()!=0:
                img_patch = img[i:i+48,j:j+48]
                img_p = osp.join(out_img_p, f.split('.')[0]+f'_{i}_{j}.jpg')
                mask_p = osp.join(out_mask_p, f.split('.')[0]+f'_{i}_{j}_segmentation.png')
                imsave(img_p, img_patch)
                imsave(mask_p, mask_patch)

def main(img_p='images_png', mask_p='1st_manual_png'):

    out_img_p = 'train_img_patch'
    out_mask_p = 'train_mask2_patch'
    imgs = os.listdir(img_p)
    for f in imgs:
        f_path = osp.join(img_p, f)
        m_path = osp.join(mask_p, f.split('_')[0]+'_manual1.png')
        #m_path = osp.join(mask_p, basename(f)+'.png')
        gen_test_patch(f, f_path, m_path, out_img_p, out_mask_p)
        #gen_train_patch(f, f_path, m_path, out_img_p, out_mask_p)

if __name__ == '__main__':
    import fire
    fire.Fire(main)

