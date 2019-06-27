"""
读指定位置的excel文件
"""

import xlrd


def read_excel(path):
    workbook = xlrd.open_workbook(path, encoding_override='utf-8')

    for i in range(0, 5):
        sheet = workbook.sheet_by_index(i)

        rows = sheet.nrows

        columns = sheet.ncols

        print(sheet.cell(1, 3))


if __name__ == '__main__':
    read_excel('C:\\Users\\daihe\\Desktop\\SimpleLinear\\result\\SimpleLinear\\SimpleLinearindex@0numOfThreads@2.xls')
