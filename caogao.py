import os
import math
import time
import turtle
# from pygrun import *


# for i in range(10):

#     print(i)

# lambda

with open(opts.path_mu_sig + '/' + random.choice(files), 'rb') as f:
    loaded_dict = pickle.load(f)
    mu_t_f1[k] = loaded_dict['mu_f1']
    std_t_f1[k] = loaded_dict['std_f1']

import cv2
for i in os.listdir("C:/Users/dell/Desktop/robotcar_demo/robotcar_train_depth_gt_clean"):
    image = cv2.imread("C:/Users/dell/Desktop/robotcar_demo/robotcar_train_depth_gt_clean/"+i,-1)/256.0
    # image = transforms.ToTensor()(image)
    valid_ = (image > 0.1) & (image < 80)
    image = image[valid_]
    if image.size==0:
        print(i)