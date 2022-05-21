#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : linjie
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import paddlehub as hub
import sopt
import os


'''
人脸检测
'''
module = hub.Module(name="ultra_light_fast_generic_face_detector_1mb_640")
# 待预测图片路径
test_img_path = ["test.png"]
input_dict = {"image": test_img_path}
results = module.face_detection(data=input_dict,visualization=True) #预测并保存结果

'''
检测到人脸：results[0]['data']!=[]
未检测到人脸：result[0]['data']==[]
'''
if results[0]['data']!=[]:
    '''
    检测到人脸
    '''
    locs = []
    locdata = str(int(results[0]['data'][0]['left']))+","+str(int(results[0]['data'][0]['top']))+","+str(int(results[0]['data'][0]['right']))+","+str(int(results[0]['data'][0]['bottom']))+","+str(input_dict['image'][0])
    locs.append(locdata)

    img = sopt.imgRead(input_dict['image'][0]) #读取图片路径
    save_path = 'IMG/'
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    sopt.screenShot(img, locs, save_path)
    print("检测到人脸，完成截图")
else:
    print("检测不到，不截图")