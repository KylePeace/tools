# -*- coding: utf-8 -*-
import json
import os

def save_str_to_file(file_name, contents):
    fh = open(file_name, 'w')
    fh.write(contents)
    fh.close()

def over_load(obj):
    if not isinstance(obj, list):
        delete_spine(obj);
    else:
        for i in range(0, len(obj)):
            over_load(obj[i])

def delete_spine(obj):
    if obj['__type__'] == "sp.SkeletonData":
        print("find spine:",obj['_name'])
        obj.pop('skeletonJsonStr')

def each_file(filepath):
    fileNames = os.listdir(filepath)  # 获取当前路径下的文件名，返回List
    for file in fileNames:
        newDir = filepath + '/' + file # 将文件命加入到当前文件路径后面
        if os.path.isfile(newDir):  # 如果是文件
            if newDir.find(".json") is not -1:  #过滤出json文件
                datas.append(newDir)
        else:
            each_file(newDir)                #如果不是文件，递归这个文件夹的路径

path_root = r"F:\myWork\build\wechatgame\res" #文件夹目录
datas = []
each_file(path_root)
print(datas)

for i in range(0, len(datas)):
    path_name = datas[i]
    file = open(path_name)
    str = file.read();
    old_size = len(str)
    has = str.find("sp.SkeletonData")
    file.close()
    if has is not -1:
        out = json.loads(str)
        print("============")
        over_load(out);
        outstr = json.dumps(out, separators=(',', ':'))
        print(path_name)
        print("old size:",old_size,"new size:", len(outstr),"diff size:", old_size - len(outstr))
        save_str_to_file(path_name,outstr)