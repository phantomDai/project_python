import jieba.analyse
import jieba.posseg as pseg
import os
from  stanfordcorenlp import StanfordCoreNLP



def cut_words(dir):
    """
    分词
    :param dir: data包下的作者名字
    :return: NULL
    """


    data_path = os.path.abspath(os.path.join(os.path.join(os.getcwd(),".."),"data"))

    #根据不同的dir名字对文件进行分词
    parent_path = os.path.join(data_path,dir)
    write_parent_path = os.path.join(parent_path, "participle")

    if os.path.exists(write_parent_path):
        pass
    else:
        os.mkdir(write_parent_path)

    #遍历指定目录下的所有文件
    for file_name in os.listdir(parent_path):
        file_path = os.path.join(parent_path,file_name)
        if os.path.isdir(file_path):
            continue
        output = ''
        with open(file_path, 'r') as f:
            content = f.read()
            word_list = jieba.cut(content, cut_all=False)
            output = "/ ".join(word_list)
            f.close()

        #将分词后的内容写入到相同文件名的participle目录中
        write_file_path = os.path.join(write_parent_path, file_name)
        with open(write_file_path, 'w') as f:
            f.write(output)
            f.close()


def cut_word_and_label(dir):
    """
    分词和标注
    :param dir: data包下的作者名字
    :return: NULL
    """

    data_path = os.path.abspath(os.path.join(os.path.join(os.getcwd(), ".."), "data"))

    # 根据不同的dir名字对文件进行分词
    parent_path = os.path.join(data_path, dir)
    write_parent_path = os.path.join(parent_path, "participleAndLabel")

    if os.path.exists(write_parent_path):
        pass
    else:
        os.mkdir(write_parent_path)

    # 遍历指定目录下的所有文件
    for file_name in os.listdir(parent_path):
        file_path = os.path.join(parent_path, file_name)
        if os.path.isdir(file_path):
            continue
        output = ''
        with open(file_path, 'r') as f:
            content = f.read()
            word_list = pseg.cut(content)

            for w in word_list:
                output += w.word + "/" + w.flag + " "

        # 将分词后的内容写入到相同文件名的participleAndLabel目录中
        write_file_path = os.path.join(write_parent_path, file_name)
        with open(write_file_path, 'w') as f:
            f.write(output)
            f.close()

def create_dicts(dir):
    nlp = StanfordCoreNLP(r'G:\stanford_nlp', lang='zh')
    data_path = os.path.abspath(os.path.join(os.path.join(os.getcwd(), ".."), "data"))

    # 根据不同的dir名字对文件进行分词
    parent_path = os.path.join(data_path, dir)
    write_parent_path = os.path.join(parent_path, "dicts")

    if os.path.exists(write_parent_path):
        pass
    else:
        os.mkdir(write_parent_path)

    # 遍历指定目录下的所有文件
    for file_name in os.listdir(parent_path):
        file_path = os.path.join(parent_path, file_name)
        if os.path.isdir(file_path):
            continue
        output = ''
        with open(file_path, 'r') as f:
            content = f.read()
            list = nlp.ner(content)
            for word, flag in list:
                output += word + '\n'
        output = output.encode('utf-8')
        write_file_path = os.path.join(write_parent_path, file_name)
        with open(write_file_path, 'wb') as f:
            f.write(output)
            f.close()


def cut_word_with_dict(dir):
    data_path = os.path.abspath(os.path.join(os.path.join(os.getcwd(), ".."), "data"))

    # 根据不同的dir名字对文件进行分词
    parent_path = os.path.join(data_path, dir)
    write_parent_path = os.path.join(parent_path, "participleWithDict")

    # get dit
    dict_path = os.path.join(parent_path, "dicts")

    if os.path.exists(write_parent_path):
        pass
    else:
        os.mkdir(write_parent_path)

    # 遍历指定目录下的所有文件
    for file_name in os.listdir(parent_path):
        file_path = os.path.join(parent_path, file_name)

        if os.path.isdir(file_path):
            continue

        dict_file_path = os.path.join(dict_path, file_name)
        jieba.load_userdict(dict_file_path)

        output = ''
        with open(file_path, 'r') as f:
            content = f.read()
            word_list = jieba.cut(content, cut_all=False)
            output = "/ ".join(word_list)
            f.close()

        write_file_path = os.path.join(write_parent_path, file_name)
        with open(write_file_path, 'w') as f:
            f.write(output)
            f.close()


# 获取分词后的文档，存放在目录下的participle目录中
cut_words("luyao")
# 分词 + 词性标注
cut_word_and_label("luyao")
# 为每一个文档创建字典
create_dicts("luyao")
# 基于自定义文档进行分词
cut_word_with_dict("luyao")