import coloredlogs
import logging
from logging.handlers import RotatingFileHandler


class IoTLogger:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

        # Max log file size is 5MB.
        self.fh = RotatingFileHandler('./Logs/IoTLogs.log', mode='a', maxBytes=5 * 1024 * 1024, backupCount=0, encoding=None,
                                      delay=False)
        # self.fh = logging.FileHandler('IoTLogs.log')
        self.fh.setLevel(logging.DEBUG)

        formatter = coloredlogs.BasicFormatter('%(asctime)s : %(levelname)s : %(message)s')
        self.fh.setFormatter(formatter)
        self.logger.addHandler(self.fh)

        coloredlogs.install(level='DEBUG', logger=self.logger)

    def log_warning(self, message):
        self.logger.warning(message)

    def log_info(self, message):
        self.logger.info(message)

    def log_critical(self, message):
        self.logger.critical(message)

    def log_error(self, message):
        self.logger.error(message, exc_info=True)

    def log_debug(self, message):
        self.logger.debug(message)


'''
if __name__ == "__main__":
    log = IoTLogger()
    log.log_warning("Func=" + __name__ + " : " + "Log=Celeste")
    log.log_debug("Func=" + __name__ + " : " + "Log=Celeste")
    log.log_error("Func=" + __name__ + " : " + "Log=Celeste")
    log.log_info("Func=" + __name__ + " : " + "Log=Celeste")
    log.log_critical("Func=" + __name__ + " : " + "Log=Celeste")
'''
