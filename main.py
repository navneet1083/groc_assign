from argparsers.argparse import ArgParse
from utils.loggers.logconf import LoggerManager

logger = LoggerManager().get_logger(__name__)


def run_main():
    logger.info('Running App')
    args_p = ArgParse()
    args = args_p.parse_arg()

    logger.debug(f'Input file loc: {args.path}')


if __name__ == '__main__':
    run_main()
