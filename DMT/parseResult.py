import os

def paste_result_to_origin(name, metric):
    corrent_path = os.getcwd()
    target_file_path = os.path.join(os.path.join(corrent_path, "results"), name)
    name = "temp" + name + ".txt"
    temp_file_path = os.path.join(corrent_path, name)
    file = open(target_file_path, 'r')
    list = file.readlines()
    temp_content = ""
    if metric == "F":
        temp_content = list[0]
    else:
        temp_content = list[1]
    content = temp_content.split(":")[1]
    content = content[1:len(content) - 2]
    temp_list = content.split(", ")
    con = ""
    for item in temp_list:
        con = con + item + '\n'

    temp_file = open(temp_file_path, 'w')
    temp_file.write(con)
    temp_file.close()


paste_result_to_origin("MT4ERS", "F")
# paste_result_to_origin("ERS_DRT", "F")
# paste_result_to_origin("MTARTsum4ERS", "F")
# paste_result_to_origin("DMTwithMAPT_RT4ERS", "F")
# paste_result_to_origin("DMTwithMAPT_PB4ERS", "F")
# paste_result_to_origin("DMTwithRAPT_RT4ERS", "F")
# paste_result_to_origin("DMTwithRAPT_PB4ERS", "F")


# paste_result_to_origin("MT4CUBS", "T")
# paste_result_to_origin("CUBS_DRT", "T")
# paste_result_to_origin("MTARTsum4CUBS", "T")
# paste_result_to_origin("DMTwithMAPT_RT4CUBS", "T")
# paste_result_to_origin("DMTwithMAPT_PB4CUBS", "T")
# paste_result_to_origin("DMTwithRAPT_RT4CUBS", "T")
# paste_result_to_origin("DMTwithRAPT_PB4CUBS", "T")