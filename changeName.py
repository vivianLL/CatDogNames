# -*- coding: cp936 -*-
# 将二级目录下的猫狗图片和标签文件重命名到images和annotations文件夹下

import os, shutil

def batchRenameFile1(srcDirName, destDirName):  # srcDirName 为源文件夹的绝对路径，真正保存数据文件的子文件夹都在该文件夹下；destDirName 为目标文件夹的绝对路径
    subDirNameList = os.listdir(srcDirName)  # 获取真正保存数据文件的文件夹序列
    for subDirName in subDirNameList:
        fileList = os.listdir(srcDirName+'/'+subDirName)    # 此处须给出绝对路径
        i = 1
        for file in fileList:
            shutil.copy(srcDirName+'/'+subDirName+'/'+file, destDirName+'/1_'+subDirName+'_'+str(i)+'.jpg')  # 此处须给出绝对路径
            print(destDirName+'/1_'+subDirName+'_'+str(i)+'.jpg')
            i = i+1


def batchRenameFile2(srcDirName, destDirName):  # srcDirName 为源文件夹的绝对路径，真正保存数据文件的子文件夹都在该文件夹下；destDirName 为目标文件夹的绝对路径
    subDirNameList = os.listdir(srcDirName)  # 获取真正保存数据文件的文件夹序列
    for subDirName in subDirNameList:
        fileList = os.listdir(srcDirName+'\\'+subDirName)    # 此处须给出绝对路径
        i = 1
        for file in fileList:
            shutil.copy(srcDirName+'\\'+subDirName+'\\'+file, destDirName+'\\2_'+subDirName+'_'+str(i)+'.jpg')  # 此处须给出绝对路径
            print(destDirName+'\\2_'+subDirName+'_'+str(i)+'.jpg')
            i = i+1


def batchRenameFile3(srcDirName, destDirName):  # srcDirName 为源文件夹的绝对路径，真正保存数据文件的子文件夹都在该文件夹下；destDirName 为目标文件夹的绝对路径
    subDirNameList = os.listdir(srcDirName)  # 获取真正保存数据文件的文件夹序列
    for subDirName in subDirNameList:
        fileList = os.listdir(srcDirName+'/'+subDirName)    # 此处须给出绝对路径
        i = 1
        for file in fileList:
            shutil.copy(srcDirName+'/'+subDirName+'/'+file, destDirName+'/1_'+subDirName+'_'+str(i)+'.xml')  # 此处须给出绝对路径
            print(destDirName+'/1_'+subDirName+'_'+str(i)+'.xml')
            i = i+1


def batchRenameFile4(srcDirName, destDirName):  # srcDirName 为源文件夹的绝对路径，真正保存数据文件的子文件夹都在该文件夹下；destDirName 为目标文件夹的绝对路径
    subDirNameList = os.listdir(srcDirName)  # 获取真正保存数据文件的文件夹序列
    for subDirName in subDirNameList:
        fileList = os.listdir(srcDirName+'/'+subDirName)    # 此处须给出绝对路径
        i = 1
        for file in fileList:
            shutil.copy(srcDirName+'/'+subDirName+'/'+file, destDirName+'/2_'+subDirName+'_'+str(i)+'.xml')  # 此处须给出绝对路径
            print(destDirName+'/2_'+subDirName+'_'+str(i)+'.xml')
            i = i+1



srcDirName = "E:\Cats&Dogs\mycatVOCdevkit\VOC2007\JPEGImages"
destDirName = "E:\myVOCdevkit\VOC2007\images"

batchRenameFile1(srcDirName, destDirName)

srcDirName = "E:\Cats&Dogs\mydogVOCdevkit\VOC2007\JPEGImages"
batchRenameFile2(srcDirName, destDirName)

srcDirName = "E:\Cats&Dogs\mycatVOCdevkit\VOC2007\Annotations"
destDirName = "E:\myVOCdevkit\VOC2007\\annotations"

batchRenameFile3(srcDirName, destDirName)

srcDirName = "E:\Cats&Dogs\mydogVOCdevkit\VOC2007\Annotations"
batchRenameFile4(srcDirName, destDirName)