# -*- encoding=UTF-8 -*-
'''
    配置文件有关各种data的配置文件
'''

path_date = "./data/date.csv"
path_object = "./data/object.csv"

#训练数据
path_train_enrollment = "./data/train/enrollment_train.csv"
path_train_truth = "./data/train/truth_train.csv"
path_train_log = "./data/train/log_train.csv"

#测试数据
path_test_enrollment = "./data/test/enrollment_test.csv"
path_test_log = "./data/test/log_test.csv"

if __name__ == "__main__":
    import os;
    os.system("ls "+path_date)
    os.system("ls "+path_object)

    os.system("ls "+path_train_log)
    os.system("ls "+path_train_enrollment)
    os.system("ls "+path_train_truth)

    os.system("ls "+path_test_enrollment)
    os.system("ls "+path_test_log)