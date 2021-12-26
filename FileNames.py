import os

class FileNames:
    def __init__(self):
        pass

    @staticmethod
    def collect_file_names(input_folder,  pattern):
        """
        Collects the input_currency data set file names
        :param input_folder, folder from which to collect the files
        :param pattern: Search pattern

        :return  _input_files: Input file list
        """
        _dir_list = next(os.walk(input_folder))[2]
        _input_files = [s for s in _dir_list if pattern in s]
        return _input_files

    @staticmethod
    def find_file( path: str, pattern: str,):
        _dir_list = next(os.walk(path))[2]
        _input_files = [s for s in _dir_list if pattern in s]
        if len(_input_files)!=0:
            return _input_files[0]
        else:
            return None

    @staticmethod
    def parse_internal_file_name(file_name):
        """
        Extracts from a currency file name the currency, bar size and price type

        :param file_name:
        :return:
        """

        assert file_name is not None, "File name not specified"
        assert file_name !=  "",  "File name is empty"

        _fn_tmp = file_name.split(".")
        if len(_fn_tmp) != 2:
            raise Exception(f"File name does not have an extension {file_name}")

        _fn_cmp_lst = _fn_tmp[0].split("_")

        if len(_fn_cmp_lst) < 3:
            raise Exception(f"Invalid file name {file_name}")

        _name_info = dict()

        if _fn_cmp_lst[1] == "":
            raise Exception(f"Invalid currency {_fn_cmp_lst[1]}")
        else:
            _name_info["instrument"] =  _fn_cmp_lst[1]

        if _fn_cmp_lst[2] == "":
            raise Exception(f"Invalid bar size {_fn_cmp_lst[2]}")
        else:
            _name_info["bar_size"] = _fn_cmp_lst[2]

        if _fn_cmp_lst[3] == "":
            raise Exception(f"Invalid price type {_fn_cmp_lst[3]}")
        else:
            _name_info["price_type"] = _fn_cmp_lst[3]

        if _fn_cmp_lst[4] == "":
            raise Exception(f"Invalid strategy name {_fn_cmp_lst[4]}")
        else:
            _name_info["strategy_name"] = _fn_cmp_lst[4]

        if _fn_cmp_lst[5] == "":
            raise Exception(f"Invalid Scenario {_fn_cmp_lst[5]}")
        else:
            _name_info["scenario_id"] = _fn_cmp_lst[5]

        return _name_info

    @staticmethod
    def replace_special_char(f_name):
        f_name = f_name.replace("<", "_LT_")
        f_name = f_name.replace(">", "_GT_")
        f_name = f_name.replace("=", "_EQ_")

        return f_name

    @staticmethod
    def create_folder(folder_name):
        
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        return folder_name
