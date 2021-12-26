"""
JSON based configuration files management

Version 1.1 Added root folder as property

"""

import json
import json as js
import sys
# from config.Environment import Environment

class SBConfig:

    # root_folder = Environment.root_folder
    # environment = Environment.point_to

    def __init__(self):
        pass


    @staticmethod
    def read_config(path):
        """
        Load process parameters from configuration file.

        DEPRECATED: Only for backward compatibility

        @PARAMS
        path: Path for the file. Assumes configuration file name: config_tick.json

        RETURNS:

        A dictionary with the process parameters
        """

        print("Loading configuration file")
        if len(path) == 0:
            path = ""
        elif path[-1] != "/":
            path += "/"

        try:
            with open(path + "config_tick.json") as fp:
                _config_set = js.load(fp)
        except Exception as e:
            raise Exception(f"Was not possible to load configuration from path {path+'config'} - {str(e)}")

        print("Configuration file loaded ok")

        return _config_set

    @staticmethod
    def read_config_file(path, file_name):
        """
        Load process parameters from configuration file

        :param path: Path for the working folder
        :param file_name: configuration file name

        :returns
            _config_set: dictionary with process configuration
        """

        print("Loading configuration file")
        if len(path) == 0:
            path = ""
        elif path[-1] != "/":
            path += "/"

        try:
            with open(path + file_name) as fp:
                _config_set = js.load(fp)
        except json.JSONDecodeError as e:
            raise Exception(f"JSON syntax error in file {path + file_name} - {str(e)}")
        except Exception as e:
            raise Exception(f"Was not possible to load configuration from path {path + file_name} - {str(e)}")

        print("Configuration file loaded ok")

        return _config_set

    # def read_mod_env_config(self, sub_system, file_name):
    #     """
    #     Loads a configuration file for a sub-system in a specific environment.
    #
    #     The environment will be taken from the global class Environment.
    #
    #     :param sub_system: subsystem path in the format /<subsystem1/subsystem1_1/>
    #     :param file_name: name of the configuration file to load
    #     :return:
    #     """
    #
    #     # TODO: Search for specific environment class in the subsystem folder.
    #
    #     _path = self.root_folder + "config/" + self.environment + sub_system
    #     print("Loading configuration file")
    #     if len(_path) == 0:
    #         path = ""
    #     elif _path[-1] != "/":
    #         _path += "/"
    #
    #     try:
    #         with open(_path + file_name) as fp:
    #             _config_set = js.load(fp)
    #     except json.JSONDecodeError as e:
    #         raise Exception(f"JSON syntax error in file {_path + file_name} - {str(e)}")
    #     except Exception as e:
    #         raise Exception(f"Was not possible to load configuration from path {_path + file_name} - {str(e)}")
    #
    #     print("Configuration file loaded ok")
    #
    #     return _config_set





