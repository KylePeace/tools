'''
    作用：转换Excel 成  json
    使用版本：python 3.6
    目录结构：
        --excel
        --json
        ExcelToJso.py

    命名方式：excel文件的每个sheet要命名，这个名字就是导出json的文件名字

    excel 有模版

    ----------------------------
    author: kely
    Date:2018/6/17
    ----------------------------
'''
# -*- coding: utf-8 -*-  
import xlrd
import os
import sys
import json
import re
# # excel 路径
excelPath = os.getcwd()+r"/excel/"
#json路径 = r"json"
jsonPath = os.getcwd()+r'/json/'
#ts路径 = r"json"
tsEnumPath = os.getcwd()+r'/ts/'

# excelPath = r"D:/learn/other/tools/testExcel_json/excel/"
# #json路径 = r"json"
# jsonPath = r'D:/learn/other/tools/testExcel_json/json/'
# 文件名
excelFile = []
# print(sys.argv[0])
# print(os.getcwd())


# 数据正文开始行数从0开始的
readcol = 3

mixStr = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
global  tsTypeStr
tsTypeStr = "\n\n"

def createTsType(workbook, sheet,fileName):
    rows = sheet.nrows
    cols = sheet.ncols
    print("%s rows,cols:%d,%d" % (sheet.name, rows, cols))
    

    # 创建一个数组用来存储excel中的数据
    p = []
    print("--------------------------")
    finalstr = "/***%s"%fileName+"***/"+"\n"
    finalstr += "export interface %s \n{\n"%(sheet.name+"_row")

    for i in range(0, cols):
        #描述
        des = sheet.cell(0, i).value
        # print(sheet.cell(0, i).value)
        #字段名
        name = sheet.cell(1, i).value
        # print(sheet.cell(1, i).value)
        #类型
        type = sheet.cell(2, i).value
        # print(sheet.cell(2, i).value)
        if(name == "" or type == ""):
            continue
        finalstr+= "\n"
        finalstr+= "\t"+"/***%s"%des+"***/"+"\n"
        finalstr+="\t"
        if(type == "int" or type == "float"):
            finalstr+= name+" :number"
        elif(type == "string" or type =="str" ):
            finalstr+= name+" :string"
        elif(type == "list"):
            finalstr+= name+" :any[]"
        elif(type == "num_list" or type == "float_list" or type == "int_list" ):#数字数组
            finalstr+= name+" :number[]"
        elif(type == "str_list" or type == "string_list"):#字符串数组
            finalstr+= name+" :string[]"
        elif(type == "item"):
            finalstr+=name +" :{itemId:number, itemNum:number}"
        elif(type == "item_list"):
            finalstr+=name +" :{itemId:number, itemNum:number}[]"
    

        finalstr+=";"
        finalstr+="\n"
      
    finalstr+="\n}\n\n\n"
    print("finalstr:\n%s"%finalstr)
    print("--------------------------")
    return finalstr




def openWorkbook(workbook, sheet):
    # 获得行数和列数
    rows = sheet.nrows
    cols = sheet.ncols
    print("%s rows,cols:%d,%d" % (sheet.name, rows, cols))
    

    # 创建一个数组用来存储excel中的数据
    p = []

    # 表头
    # print("rows:", rows)
    for i in range(readcol, rows):
        d = {}
        for j in range(0, cols):
            q = "%s" % sheet.cell(1, j).value
            if(q == ""):
                break
            if(sheet.cell(i, j).value == ""):
                print("        ")
                print("%s表第%d行，第%d列为空" % (sheet.name, i + 1, j + 1))
                # print("请修改%s表  后重新导出，否则会有错误！" % sheet.name)
                print("        ")
                # sheet.cell(i, j).value = mixStr
                d[q] = mixStr
                # return
            else:
                d[q] = sheet.cell(i, j).value
        ap = []
        count = 0
        for k, v in d.items():
            # 类型检查
            valueType = sheet.cell(2, count).value
            count += 1
            if(valueType == '' or valueType == None):
                print("%s缺少类型"%sheet.name)
                return
            if(v==mixStr):
                continue
            #兼容把所有的中文逗号替换成英文
            #判断是不是字符串
            if(isinstance(v,str)):
                v = v.replace("，",",")
            

            if(valueType == "float"):  
                ap.append('"%s":%d' % (k, v))
            elif(valueType == "int"):
                    print("%s 表，类型错误%d行%d列：" % (sheet.name, i + 1, count))
                    print("        ")
                    ap.append('"%s":%d' % (k, v))
                    #return
            elif(valueType == "list"):  # 新增的数组类型判断
                # v2 = str(v).split("|")
                v2 = re.split(r'\|',str(v))
                v3 = []
                for vv in v2:
                    if(vv.isdigit()):
                        v3.append(int(vv))
                    else:
                        v3.append(str(vv))
                ap.append('"%s":%s' % (k, json.dumps(v3,ensure_ascii=False)))  # 将数组类型的值转换为字符串并添加到列表中
            elif(valueType == "string" or valueType == "str"): 
                ap.append('"%s":"%s"' % (k, v))
            # elif(valueType == "num_list" or valueType == "int_list"):
            #     v2 = re.split(r'\|',str(v))
            #     v3 = []
                
            #     for vv in v2:
            #         if(not vv.isdigit()):
            #             print("%sint_list中有字符串"%sheet.name)
            #             return
            #         v3.append(int(vv))
            #     ap.append('"%s":%s' % (k, json.dumps(v3,ensure_ascii=False)))
            elif(valueType == "str_list"):
                # v2 = re.split(r'\|',str(v))
                # v3 = []
                # for vv in v2:
                #     v3.append(str(vv))
                # ap.append('"%s":%s' % (k, json.dumps(v3,ensure_ascii=False)))


                v2 = re.split(r'\|',str(v))
                v3 = []
                for vv in v2:
                    vv4 = re.split(r',',str(vv))
                    v5 = []
                    for vvv in vv4:
                        v5.append(str(vvv))
                    v3.append(v5)
                ap.append('"%s":%s' % (k, json.dumps(v3,ensure_ascii=False)))

            elif(valueType == "item"):
                v2 = re.split(r',',str(v))
                v3={
                    "itemId":int(v2[0]),
                    "itemNum":int(v2[1])
                }
                ap.append('"%s":%s' % (k, json.dumps(v3,ensure_ascii=False)))
            elif(valueType =="item_list"):
                v2 = re.split(r'\|',str(v))
                v3 = []
                for vv in v2:
                    vv4 = re.split(r',',str(vv))
                    v3.append({
                    "itemId":int(vv4[0]),
                    "itemNum":int(vv4[1])
                })
                ap.append('"%s":%s' % (k, json.dumps(v3,ensure_ascii=False)))
            # elif(valueType =="int_list_list"):
            #     v2 = re.split(r'\|',str(v))
            #     v3 = []
            #     for vv in v2:
            #         vv4 = re.split(r',',str(vv))
            #         v5 = []
            #         for vvv in vv4:
            #             v5.append(int(vvv))
            #         v3.append(v5)
            #     ap.append('"%s":%s' % (k, json.dumps(v3,ensure_ascii=False)))
            # elif(valueType == "str_list_list"):
            #     v2 = re.split(r'\|',str(v))
            #     v3 = []
            #     for vv in v2:
            #         vv4 = re.split(r',',str(vv))
            #         v5 = []
            #         for vvv in vv4:
            #             v5.append(str(vvv))
            #         v3.append(v5)
            #     ap.append('"%s":%s' % (k, json.dumps(v3,ensure_ascii=False)))
            elif(valueType == "int_list" or valueType == "num_list" or valueType == "float_list"):
                v2 = re.split(r'\|',str(v))
                v3 = []
                for vv in v2:
                    vv4 = re.split(r',',str(vv))
                    v5 = []
                    print("vvv4:",vv4)
                    for vvv in vv4:
                        print("isinstance(vvv,int)",vvv,isinstance(vvv,int))
                        print("isinstance(vvv,int)",vvv,isinstance(vvv,float))

                        if '.' in vvv:
                            v5.append(float(vvv)) 
                        else :
                            v5.append(int(vvv))
                    v3.append(v5)
                ap.append('"%s":%s' % (k, json.dumps(v3,ensure_ascii=False)))

        s = '{%s}' % (','.join(ap))  # 继续格式化
        p.append(s)

    t = '[%s]' % (','.join(p))  # 格式化b
    # print(t)

    # 写入文件
    with open(jsonPath + sheet.name + ".json", "w", encoding='utf8') as f:
        f.write(t)
        f.close()


# 获取制定目录下的所有excel文件
def getExcelFiles(file_dir):
    print(file_dir)
    for root, dirs, files in os.walk(file_dir):
        root_dir = os.path.dirname(os.path.abspath('.')) 
        print(root_dir+root)  # 当前目录路径
        print(dirs)  # 当前路径下所有子目录
        print("打印文件名：", files)  # 当前路径下所有非目录子文件
        if(not files):
            print("获取文件名错误")
            return []
        return files


# 读取单个excel 文件
def readExcel(file):
    # 读取excel表的数据
    workbook = xlrd.open_workbook(excelPath + file)
    # 选取需要读取数据的那一页
  
    global tsTypeStr 
    sheets = workbook.sheet_names()

    for sh in sheets:
        s = workbook.sheet_by_name(sh)

        openWorkbook(workbook, s)
        tsTypeStr+=createTsType(workbook, s,file)
       
    print("tsTypeStr:%s"%tsTypeStr)
    with open(tsEnumPath + "ConfigDefine" + ".ts", "w", encoding='utf8') as f:
        f.write(tsTypeStr)
        f.close()



def judgeDir():
    isExist1 = os.path.exists(excelPath)
    if not isExist1:
        os.makedirs(excelPath)
        print(excelPath + ' 创建成功')
    else:
        print(excelPath + ' 目录已存在')

    isExist2 = os.path.exists(jsonPath)
    if not isExist2:
        os.makedirs(jsonPath)
        print(jsonPath + ' 创建成功')
    else:
        print(jsonPath + ' 目录已存在')

    isExist2 = os.path.exists(tsEnumPath)
    if not isExist2:
        os.makedirs(tsEnumPath)
        print(tsEnumPath + ' 创建成功')
    else:
        print(tsEnumPath + ' 目录已存在')


def main():
    # openWorkbook()
    excelFiles = getExcelFiles(excelPath)

    for file in excelFiles:
        filetype = os.path.splitext(file)
        # 其中os.path.splitext()函数将路径拆分为文件名+扩展名
        if filetype[1] == '.xlsx' or filetype[1] == ".xls":
            if(filetype[0][0] == "~"):
                break
            # print(file)
            readExcel(file)


if __name__ == '__main__':
    judgeDir()
    main()
    print("转换完成")
    os.system("pause")
