import logging

logging.basicConfig(
    filename='HISTORYlistener.log',
    level=logging.DEBUG,
    format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)

####################################################################################################

import logging

class MyFormatter(logging.Formatter):
    def format(self, record):
        record.message2 = ""
        if(record.args):
            record.func_name = record.args.get("func_name", "Fallback Value")
        return super().format(record)

logger = logging.getLogger()
fh = logging.FileHandler(filename='log.txt', mode='a')
fh.setFormatter(MyFormatter('%(asctime)s --- %(func_name)s --- %(message)s', datefmt='%Y-%m-%d %H:%M:%S'))
logging.basicConfig(level=logging.INFO, handlers=[fh])

def write_log(func_name, message):
    logger.info(message, {"func_name": func_name})

