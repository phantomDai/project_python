import sys
import os

class deletefile(object):
    """
    this class is responsible to delete some types of files
    """

    def delete_file(self, path, filter='.class'):
        """
        the function of deleting the files
        :param path: the parent dir
        :param filter: the specified file
        :return: None
        """
        if os.path.isdir(path):
            for filename in os.listdir(path):
                dir_path = os.path.join(path, filename)
                for file in os.listdir(dir_path):
                    if file.endswith(filter):
                        os.remove(os.path.join(dir_path, file))
                    else:
                        pass
        else:
            print("路径表示不是一个目录")


delete = deletefile()
delete.delete_file(r"G:\PROJECT_IDEA\DMT\src\main\java\labprograms\ACMS\mutants")



