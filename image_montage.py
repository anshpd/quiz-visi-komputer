#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 14:45:51 2018

@author: mis-admin
"""

import cv2
import os
from imutils import build_montages
import numpy as np
from tqdm import tqdm

images_cat = []
images_mask = []
images_montage = []

IMG_WIDTH = 550
IMG_HEIGHT = 330

path_cat = os.getcwd()+'/cat'
path_mask = os.getcwd()+'/mask'
path_hasil = os.getcwd() + '/hasil'

img_cat = cv2.imread(path_cat+'/cat.jpg', 1)
img_cat = cv2.resize(img_cat, (IMG_WIDTH,IMG_HEIGHT))

for all_masks in tqdm(os.listdir(path_mask)):
	path_loc = os.path.join(path_mask, all_masks)
	img_mask=cv2.imread(path_loc, cv2.IMREAD_COLOR)
	img_mask=cv2.resize(img_mask, (IMG_WIDTH,IMG_HEIGHT))
	images_mask.append(img_mask)

for i in range (9):
	add_images=cv2.add(img_cat, images_mask[i%7])
	add_images=cv2.imwrite(os.path.join(path_hasil, 'cat-'+str(i)+'.jpg'), add_images)

path = os.getcwd()
for image in tqdm(os.listdir(path_hasil)):
	loc=os.path.join(path_hasil, image)
	img_montage = cv2.imread(loc, cv2.IMREAD_COLOR)
	images_montage.append(img_montage)

#Fungsi untuk Collage Image
montages = build_montages(images_montage, (400, 200), (3,3))

for montage in montages:
	cv2.imshow("Pop Art Collage", montage)
	cv2.imwrite(os.path.join(path_hasil, 'montages.jpg'), montage)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
#	add_images=cv2.add(img_cat, img_mask)
#	add_images=cv2.imwrite(os.path.join(path_hasil, 'cat-{}.jpg'), add_images)
#img_mask_yellow = cv2.imread(path_mask+'/yellow.jpg',1)
#img_mask_blue = cv2.imread(path_mask+'/blue.jpg',1)
#img_mask_green = cv2.imread(path_mask+'/green.png',1)
#img_mask_red = cv2.imread(path_mask+'/red.jpg',1)
#img_mask_org = cv2.imread(path_mask+'/orange.png',1)

#img_cat=cv2.resize(img_cat, (IMG_WIDTH,IMG_HEIGHT))
#img_mask_yellow=cv2.resize(img_mask_yellow, (IMG_WIDTH,IMG_HEIGHT))
#img_mask_green=cv2.resize(img_mask_green, (IMG_WIDTH,IMG_HEIGHT))
#img_mask_blue=cv2.resize(img_mask_blue, (IMG_WIDTH,IMG_HEIGHT))
#img_mask_red=cv2.resize(img_mask_red, (IMG_WIDTH,IMG_HEIGHT))
#img_mask_org=cv2.resize(img_mask_org, (IMG_WIDTH,IMG_HEIGHT))
#for entire_images in all_images:
#	add_images = cv2.add(img_cat, img_mask)
#	for i in range (9):
#		add_images = cv2.imwrite(os.path.join(path_hasil, 'cat-'+str(i)+'.jpg'), add_images)
	
#add_yellow = cv2.add(img_cat, img_mask_yellow)
#add_blue = cv2.add(img_cat, img_mask_blue)
#add_green = cv2.add(img_cat, img_mask_green)
#add_red = cv2.add(img_cat, img_mask_red)
#add_org = cv2.add(img_cat, img_mask_org)

#cv2.imwrite(os.path.join(path_hasil ,'cat-0.jpg'), add_yellow)
#cv2.imwrite(os.path.join(path_hasil ,'cat-1.jpg'), add_blue)
#cv2.imwrite(os.path.join(path_hasil ,'cat-2.jpg'), add_green)
#cv2.imwrite(os.path.join(path_hasil ,'cat-3.jpg'), add_red)
#cv2.imwrite(os.path.join(path_hasil ,'cat-4.jpg'), add_org)









