import logging
import logging.config

from utils.configreader.confparse import ConfigManager

cfg = ConfigManager().get_config('conf')


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances.keys():
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class LoggerManager(object):
    __metaclass__ = Singleton

    _loggers = {}

    def __init__(self, *args, **kwargs):
        pass

    @staticmethod
    def get_logger(name=None):
        if not name:
            # print('bye')
            logging.basicConfig()
            return logging.getLogger()
        elif name not in LoggerManager._loggers.keys():
            log_path = cfg.get('Path-Related', 'logger_file_path')
            logging.config.fileConfig(log_path, disable_existing_loggers=False)
            LoggerManager._loggers[name] = logging.getLogger(str(name))
        return LoggerManager._loggers[name]
