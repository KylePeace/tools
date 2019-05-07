
#coding=utf-8
'''
	python3
	对比文件夹内容，拷贝新文件在旧文件夹中不存在的文件
	对比的是文件得名字
	author:kley

'''
import os

import os.path

import shutil

rootdir="./nowRes" 
outdir = "./outRes"
lastdir ="./lastRes"


def mkdir(path):
	path = path.strip()
	isExists = os.path.exists(path)
	if not isExists:
		os.makedirs(path)
		#print("创建目录："+path)
		return True
	else:
		#print("目录已存在:"+path)
		return False


#创建所有文件夹
def mkAlldir():
	for parent,dirnames,filenames in os.walk(rootdir): 
	    for dirname in dirnames:  
	        newpath = (parent+"\\"+dirname).replace(rootdir,outdir)
	        #print(newpath)
	        mkdir(newpath)

def copyFile():
	for parent,dirnames,filenames in os.walk(rootdir): 
		for filename in filenames:
	  		comparePath = os.path.join(parent,filename).replace(rootdir,lastdir)
	  		isExists = os.path.exists(comparePath)
	  		if not isExists:
	  			copypath = shutil.copy(os.path.join(parent,filename), os.path.join(parent,filename).replace(rootdir,outdir))


def removeEmptydir(out):
	for (root, dirs, files) in os.walk(out):
		for item in dirs:
			dir = os.path.join(root, item)
			try:
				os.rmdir(dir)  
			except Exception as e:
				print('Exception',e)
				removeEmptydir(dir)

def main():
	mkAlldir()
	copyFile()
	removeEmptydir(outdir)
	  

if __name__ == '__main__':
	main()
