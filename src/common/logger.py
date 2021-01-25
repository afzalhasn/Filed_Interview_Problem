import logging
import os
from logging.handlers import TimedRotatingFileHandler

class Logger:

    DEBUG = logging.DEBUG
    INFO = logging.INFO

    @staticmethod
    def init(base_dir_path, log_file_name, logging_level=logging.INFO):
        
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
        if not os.path.exists(f"{base_dir_path}/logs"):
            os.makedirs(f"{base_dir_path}/logs", exist_ok = True)
        logging.basicConfig(filename=f"{base_dir_path}/logs/{log_file_name}.log",
                            level=logging_level,
                            format='%(asctime)s %(levelname)-8s %(message)s', datefmt='%Y-%m-%d %H:%M:%S'
                            )
    
        handler = TimedRotatingFileHandler(f"{base_dir_path}/logs/{log_file_name}.log",
                                        when="midnight",
                                        interval=1)
        logFormatter = logging.Formatter('%(asctime)s %(levelname)-8s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        handler.setFormatter( logFormatter )
        handler.suffix = "%Y-%m-%d"
        logging.root.addHandler(handler)

    @staticmethod
    def log_info(msg):
        logging.info(msg)

    @staticmethod
    def log_debug(msg):
        logging.debug(msg)

    @staticmethod
    def log_error(msg):
        logging.error(msg)
