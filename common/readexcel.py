# coding:utf-8
import xlrd
#读excel数据类
class ExcelUtil():
    def __init__(self,excelpath,sheetname="Sheet1"):#两个属性第一个属性：文件名，第二个属性sheetname
        self.data = xlrd.open_workbook(excelpath)  #打开文件
        self.table = self.data.sheet_by_name(sheetname)
        #获取第一行作为key值
        self.keys = self.table.row_values(0)
        #获取总行数
        self.rowNows = self.table.nrows
        #获取总列数
        self.colNum = self.table.ncols
    def dict_data(self):
        if self.rowNows <= 1:
            print ("总行数小于等于1")
        else:
            r = []
            j = 1
            for i in list(range(self.rowNows-1)):
                s = {}
                #从第二行取对应的value值
                s["rowNum"] = i+2
                values = self.table.row_values(j)
                for x in list(range(self.colNum)):
                    s[self.keys[x]] = values[x]
                r.append(s)
                j+=1
            return r
if __name__=="__main__":
    filepath = "debug_api.xlsx"
    sheetName = "Sheet1"
    data = ExcelUtil(filepath,sheetName)
    print (data.dict_data())