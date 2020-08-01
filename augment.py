import sys
if '/opt/ros/kinetic/lib/python2.7/dist-packages' in sys.path:
    sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
import imgaug as ia
from imgaug import augmenters as iaa
import numpy as np
import imageio
import os

ia.seed(1)

DATA_DIR1 = '/home/raghwendra/Downloads/NewFlagDataRaw/Test'
SAVE_DIR1 = '/home/raghwendra/Downloads/NewFlagData/Test'

iter = 0

for each_cont in os.listdir(DATA_DIR1):
    DATA_DIR = os.path.join(DATA_DIR1,each_cont)
    iter=0
    for each_flag in os.listdir(DATA_DIR):
        actual_path = os.path.join(DATA_DIR,each_flag) 
        img = imageio.imread(actual_path) #read you image
        images = np.array(
            [img for _ in range(30)], dtype=np.uint8)  # 32 means creat 32 enhanced images using following methods.

        seq = iaa.Sequential(
            [
                iaa.Fliplr(0.5),  
                iaa.Crop(percent=(0, 0.1)),            
                iaa.Sometimes(0.5, iaa.GaussianBlur(sigma=(0, 0.5))),        
                iaa.ContrastNormalization((0.75, 1.5)),         
                iaa.AdditiveGaussianNoise(
                    loc=0, scale=(0.0, 0.05 * 255), per_channel=0.5),    
                iaa.Multiply((0.8, 1.2), per_channel=0.2),
                iaa.Affine(
                    scale={
                        "x": (0.8, 1.2),
                        "y": (0.8, 1.2)
                    },
                    translate_percent={
                        "x": (-0.2, 0.2),
                        "y": (-0.2, 0.2)
                    },
                    rotate=(-25, 25),
                    shear=(-8, 8))
            ],
            random_order=True)  # apply augmenters in random order

        images_aug = seq.augment_images(images)

        for i in range(30):
            imageio.imwrite(SAVE_DIR1+ '/' + each_cont + '/' + str(i+iter*30)+'new.jpg', images_aug[i])  #write all changed images
        iter += 1

