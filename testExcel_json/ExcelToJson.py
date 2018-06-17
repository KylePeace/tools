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

import xlrd
import os


# excel 路径
excelPath = r"excel/"
#json路径 = r"json"
jsonPath = r'json/'

# 文件名
excelFile = []


# 数据正文开始行数从0开始的
readcol = 3


def openWorkbook(workbook, sheet):
    # 获得行数和列数
    rows = sheet.nrows - 1
    cols = sheet.ncols - 1
    # 创建一个数组用来存储excel中的数据
    p = []

    # 表头
    #print("rows:", rows)
    for i in range(readcol, rows):
        d = {}
        for j in range(0, cols):
            q = "%s" % sheet.cell(1, j).value
            # print(q)
            if(q == ""):
                break
            if(sheet.cell(i, j).value == ""):
                print("        ")
                print("%s表第%d行，第%d列为空" % (sheet.name, i + 1, j + 1))
                print("请修改%s表  后重新导出，否则会有错误！" % sheet.name)
                print("        ")

                return
            d[q] = sheet.cell(i, j).value
            #print(sheet.cell(i, j).value)

        ap = []
        count = 0
        for k, v in d.items():
            # 类型检查
            valueType = sheet.cell(2, count).value
            count += 1
            if isinstance(v, float):  # excel中的数字值默认是float,需要进行判断处理，通过'"%s":%d'，'"%s":"%s"'格式化数组\
                ap.append('"%s":%d' % (k, v))
            else:
                if(valueType == "int"):
                    print("%s 表，类型错误%d行%d列：" % (sheet.name, i + 1, count))
                    print("        ")
                    return

                ap.append('"%s":"%s"' % (k, v))

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
    for root, dirs, files in os.walk(file_dir):
        # print(root)  # 当前目录路径
        # print(dirs)  # 当前路径下所有子目录
        print("打印文件名：", files)  # 当前路径下所有非目录子文件
        if(not files):
            print("获取文件名错误")
            return
        return files


# 读取单个excel 文件
def readExcel(file):
    # 读取excel表的数据
    workbook = xlrd.open_workbook(r"excel/" + file)
    # 选取需要读取数据的那一页
    sheets = workbook.sheet_names()
    for sh in sheets:
        s = workbook.sheet_by_name(sh)

        openWorkbook(workbook, s)

# 创建目录


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
