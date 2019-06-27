import os


class AddPackageInfo(object):
    """"
    this class is responsible to add the information of mutants' package
    """

    def add_information(self, path, program, class_name):
        """"
        add information
        """
        if os.path.isdir(path):
            for mutant in os.listdir(path):
                mutant_path = os.path.join(path, mutant)
                f = open(os.path.join(mutant_path, class_name), 'r+')
                lines = f.readlines()
                f = open(os.path.join(mutant_path, class_name), 'w')
                package_info = "// This is a mutant program."
                new_package_info = "package labprograms." + program + ".mutants." + mutant + ";"
                for content in lines:
                    f.write(content.replace(package_info, new_package_info))
                f.close()
        else:
            print("path is not a dir")



    def add_MRS_to_MOS(self, path):
        """"
        import labprograms.MOS.sourceCode.MSR;
        """
        if os.path.isdir(path):
            for mutant in os.listdir(path):
                mutant_dir = os.path.join(path, mutant)
                f = open(os.path.join(mutant_dir, "MealOrderingSystem.java"), 'r+')
                lines = f.readlines()
                f = open(os.path.join(mutant_dir, "MealOrderingSystem.java"), 'w')
                old_info = "// Author : ysma"
                new_info = "import labprograms.MOS.sourceCode.MSR;"
                for content in lines:
                    f.write(content.replace(old_info, new_info))
                f.close()

        else:
            print("the path is not a dir")


addpackageinfo = AddPackageInfo()
# addpackageinfo.add_information(r"G:\PROJECT_IDEA\DMT\src\main\java\labprograms\ACMS\mutants", "ACMS", "AirlinesBaggageBillingService.java")
addpackageinfo.add_MRS_to_MOS(r"G:\PROJECT_IDEA\DMT\src\main\java\labprograms\MOS\mutants")




