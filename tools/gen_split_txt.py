import os
import random


def split_skin(in_path, out_path='split_txt'):
    os.makedirs(out_path, exist_ok=True)
    train_txt = open(os.path.join(out_path, 'train_txt'), 'w')
    val_txt = open(os.path.join(out_path, 'val_txt'), 'w')
    test_txt = open(os.path.join(out_path, 'test_txt'), 'w')
    fs = os.listdir(in_path)
    random.shuffle(fs)
    for i, f in enumerate(fs):
        if i<1815:
            train_txt.write(f+'\n')
        elif i<(1815+259):
            val_txt.write(f+'\n')
        else:
            test_txt.write(f+'\n')
    train_txt.close()
    val_txt.close()
    test_txt.close()


def split_drive(in_path='train_img_patch', out_path='split_txt'):
    os.makedirs(out_path, exist_ok=True)
    train_txt = open(os.path.join(out_path, 'train_txt'), 'w')
    val_txt = open(os.path.join(out_path, 'val_txt'), 'w')
    fs = os.listdir(in_path)
    random.shuffle(fs)
    for i, f in enumerate(fs):
        if i<len(fs)//10:
            val_txt.write(f+'\n')
        else:
            train_txt.write(f+'\n')

    train_txt.close()
    val_txt.close()


if __name__=='__main__':
    import fire
    #fire.Fire(split_skin)
    fire.Fire(split_drive)
