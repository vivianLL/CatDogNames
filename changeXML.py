# -*- coding: utf-8 -*-
# 根据字典中的值修改xml文件中节点的内容

import os
from xml.etree.ElementTree import parse, Element

# 根据猫狗名字的对应关系生成数字：种类的字典，狗的序号在猫后面，所以在狗的序号后面加42
def creatDic():
    txtDict = {}
    DirFile = 'E:\Cats&Dogs\CatList.txt'
    dicFile = open(DirFile,'r')
    while True:
        line = dicFile.readline()
        if '\xef\xbb\xbf' in line:
            line = line.replace('\xef\xbb\xbf', '')
        if line == '':
            break
        key = line.split('\t')[0]
        # print(key)
        value = line.split('\t')[-1]
        # print(value)
        txtDict[key] = value  # 加入字典
    dicFile.close()

    DirFile = 'E:\Cats&Dogs\DogList.txt'
    dicFile = open(DirFile, 'r')
    while True:
        line = dicFile.readline()
        if '\xef\xbb\xbf' in line:
            line = line.replace('\xef\xbb\xbf', '')
        if line == '':
            break
        key = line.split('\t')[0]
        value = line.split('\t')[-1].split('\n')[0]
        txtDict[str(int(key)+int(42))] = value  # 加入字典
    dicFile.close()
    return txtDict

def batchRenameFile1(DirName,txtDict):  # DirName 为文件夹的绝对路径

    FileList = os.listdir(DirName)

    for FileName in FileList:
        FilePath = DirName+'\\'+FileName
        print(FilePath)
        doc = parse(FilePath)
        root = doc.getroot()
        sub1 = root.find("filename")
        name = FileName.split(".")[0] + ".jpg"
        sub1.text = name
        sub2 = root.find("path")
        sub2.text = "E:\myVOCdevkit\VOC2007\\images\\"+name
        species = FileName.split("_")[0]
        label = FileName.split("_")[1]
        if species == "1":                 # cat
            sub3 = root.find("folder")
            sub3.text = txtDict[label]
            for sub4 in root.findall("object"):   ##找到root节点下的所有object节点，因为有不止一个名字叫object的节点
                subsub=sub4.find('name')
                subsub.text = txtDict[label]
        if species == "2":                 # dog
            sub3 = root.find("folder")
            sub3.text = txtDict[str(int(label)+int(42))]
            for sub4 in root.findall("object"):
                subsub=sub4.find('name')
                subsub.text = txtDict[str(int(label)+int(42))]

        doc.write(FilePath)


txtDict = creatDic()
# print(txtDict)

DirName = "E:\myVOCdevkit\VOC2007\\annotations"
# DirName = 'C:\Users\leilu\Desktop\\test1\\1'
batchRenameFile1(DirName,txtDict)