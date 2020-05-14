import configparser
from configparser import ExtendedInterpolation


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances.keys():
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class ConfigManager(object):
    __metaclass__ = Singleton

    _configs = {}

    def __init__(self, *args, **kwargs):
        pass

    @staticmethod
    def get_config(name=None):
        if not name:
            print(f'Inside ConfParser static method')
            config = configparser.ConfigParser(interpolation=ExtendedInterpolation())
            return config
        elif name not in ConfigManager._configs.keys():
            config = configparser.ConfigParser(interpolation=ExtendedInterpolation())
            config.read_file(open(r'configs/config.cfg'))
            ConfigManager._configs[name] = config
        return ConfigManager._configs[name]
