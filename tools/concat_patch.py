import os
import os.path as osp
import numpy as np
from skimage.io import imsave, imread
import re

def basename(f):
    return osp.splitext(f)[0]


def concat_patch(f, f_path, m_path, out_img_p, out_mask_p):

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

def main(img_p='mixunet'):

    out_p = img_p.rstrip('/') + '_whole'
    os.makedirs(out_p, exist_ok=True)
    img_dict = {}
    ims = os.listdir(img_p)

    for i in range(11, 15):
        sr0 = sr1 = np.zeros((960,960))
        gt0 = gt1 = np.zeros((960,960))
        img0 = img1 = np.zeros((960,960))
        img_dict['{:0>2d}'.format(i) + 'L'] = {'SR': sr0, 'GT':gt0, 'images': img0}
        img_dict['{:0>2d}'.format(i) + 'R'] = {'SR': sr1, 'GT':gt1, 'images': img1}

    for i in ims:
        im = imread(osp.join(img_p, i))
        i_list = re.split('[_.]', i)
        img_dict[i_list[1]][i_list[-2]][int(i_list[2]):int(i_list[2])+48, int(i_list[3]):int(i_list[3])+48] = im

    for k in img_dict.keys():
        for i in img_dict[k].keys():
            if i == 'images':
                continue
            imsave(f'{out_p}/{k}_{i}.jpg',img_dict[k][i])
    

if __name__ == '__main__':
    import fire
    fire.Fire(main)

