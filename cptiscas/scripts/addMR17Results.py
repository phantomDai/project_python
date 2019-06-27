"""
this scripts is responsible to add extends results to result file
"""
import xlrd
import xlwt
import os


def add_extra_content(object_name, list):
    """
    add content according to the specified object
    :param object_name: object name
    :param list: names
    :return: null
    """
    sheet_list = ["sheet1", "sheet2", "sheet3", "sheet4", "sheet5"]
    target_path = os.path.join(os.path.join(os.path.abspath('..'), 'results'), object_name)
    supplement_path = os.path.join(os.path.join(os.path.join(os.path.abspath('..'), 'results'),
                                                'supplement'), object_name)
    save_path = os.path.join(os.path.join(os.path.join(os.path.abspath('..'),
                                                       'results'), 'save'), object_name)
    if os.path.exists(save_path):
        pass
    else:
        os.mkdir(save_path)

    for name in list:

        target_file_path = os.path.join(target_path, name)
        supplement_file_path = os.path.join(supplement_path, name)
        # 获得工作簿的对象
        target_work_book = xlrd.open_workbook(target_file_path)
        supplement_work_book = xlrd.open_workbook(supplement_file_path)
        # 遍历每一个sheet
        for sheet in sheet_list:
            target_temp_sheet = target_work_book.sheet_by_name(sheet)
            supplement_temp_sheet = supplement_work_book.sheet_by_name(sheet)
            # 获得行数
            rows_target = target_temp_sheet.nrows
            rows_supplement = target_temp_sheet.nrows
            # 获得列数
            cols = target_temp_sheet.ncols
            for row in range(1, rows_supplement):
                for col in range(0, cols):
                    target_temp_sheet.write(rows_target + row - 1, col, supplement_temp_sheet.cell_value())

            temp_book = xlwt.Workbook(encoding='utf-8')






