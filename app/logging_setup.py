import logging
from logging.handlers import RotatingFileHandler

LOGS_OUTPUT = './app/app_logs/data.log'
LOGS_FORMAT = '%(asctime)s\t%(levelname)s\t%(message)s'
LOGS_DATE_FORMAT = '%H:%M:%S'

logging.basicConfig(
    format=LOGS_FORMAT,
    level=logging.INFO,
    datefmt=LOGS_DATE_FORMAT,
)
logger = logging.getLogger(__name__)


class LineRotatingFileHandler(RotatingFileHandler):
    def __init__(self, maxlines, filename=LOGS_OUTPUT):
        super().__init__(filename=filename, backupCount=5)
        self.maxlines = maxlines
        self.filename = filename

    def shouldRollover(self, record):
        if self.stream is None:
            self.stream = self._open()
        with open(self.filename, 'r') as file:
            count_lines = len(file.readlines())
        if count_lines >= self.maxlines:
            return True
        return False


line_handler = LineRotatingFileHandler(maxlines=50)
formatter_line = logging.Formatter(LOGS_FORMAT, datefmt=LOGS_DATE_FORMAT)

line_handler.setFormatter(formatter_line)
logger.addHandler(line_handler)
