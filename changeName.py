# -*- coding: cp936 -*-
# ������Ŀ¼�µ�è��ͼƬ�ͱ�ǩ�ļ���������images��annotations�ļ�����

import os, shutil

def batchRenameFile1(srcDirName, destDirName):  # srcDirName ΪԴ�ļ��еľ���·�����������������ļ������ļ��ж��ڸ��ļ����£�destDirName ΪĿ���ļ��еľ���·��
    subDirNameList = os.listdir(srcDirName)  # ��ȡ�������������ļ����ļ�������
    for subDirName in subDirNameList:
        fileList = os.listdir(srcDirName+'/'+subDirName)    # �˴����������·��
        i = 1
        for file in fileList:
            shutil.copy(srcDirName+'/'+subDirName+'/'+file, destDirName+'/1_'+subDirName+'_'+str(i)+'.jpg')  # �˴����������·��
            print(destDirName+'/1_'+subDirName+'_'+str(i)+'.jpg')
            i = i+1


def batchRenameFile2(srcDirName, destDirName):  # srcDirName ΪԴ�ļ��еľ���·�����������������ļ������ļ��ж��ڸ��ļ����£�destDirName ΪĿ���ļ��еľ���·��
    subDirNameList = os.listdir(srcDirName)  # ��ȡ�������������ļ����ļ�������
    for subDirName in subDirNameList:
        fileList = os.listdir(srcDirName+'\\'+subDirName)    # �˴����������·��
        i = 1
        for file in fileList:
            shutil.copy(srcDirName+'\\'+subDirName+'\\'+file, destDirName+'\\2_'+subDirName+'_'+str(i)+'.jpg')  # �˴����������·��
            print(destDirName+'\\2_'+subDirName+'_'+str(i)+'.jpg')
            i = i+1


def batchRenameFile3(srcDirName, destDirName):  # srcDirName ΪԴ�ļ��еľ���·�����������������ļ������ļ��ж��ڸ��ļ����£�destDirName ΪĿ���ļ��еľ���·��
    subDirNameList = os.listdir(srcDirName)  # ��ȡ�������������ļ����ļ�������
    for subDirName in subDirNameList:
        fileList = os.listdir(srcDirName+'/'+subDirName)    # �˴����������·��
        i = 1
        for file in fileList:
            shutil.copy(srcDirName+'/'+subDirName+'/'+file, destDirName+'/1_'+subDirName+'_'+str(i)+'.xml')  # �˴����������·��
            print(destDirName+'/1_'+subDirName+'_'+str(i)+'.xml')
            i = i+1


def batchRenameFile4(srcDirName, destDirName):  # srcDirName ΪԴ�ļ��еľ���·�����������������ļ������ļ��ж��ڸ��ļ����£�destDirName ΪĿ���ļ��еľ���·��
    subDirNameList = os.listdir(srcDirName)  # ��ȡ�������������ļ����ļ�������
    for subDirName in subDirNameList:
        fileList = os.listdir(srcDirName+'/'+subDirName)    # �˴����������·��
        i = 1
        for file in fileList:
            shutil.copy(srcDirName+'/'+subDirName+'/'+file, destDirName+'/2_'+subDirName+'_'+str(i)+'.xml')  # �˴����������·��
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