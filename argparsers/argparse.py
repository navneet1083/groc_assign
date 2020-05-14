import argparse

from utils.loggers.logconf import LoggerManager

logger = LoggerManager().get_logger(__name__)


class ArgParse:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Grocery Product Detection!')
        self.parser.add_argument('--path', default='', type=str, metavar='PATH',
                                 help='path to images ')

    def parse_arg(self):
        logger.info('Parsing arguments !! ')
        args = self.parser.parse_args()
        return args
