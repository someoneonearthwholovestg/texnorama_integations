from config import Config
from loguru import logger
import sys

def get_logger():
    level =  int(Config.DEBUG_MODE)

    if level == 5:
    	level = "TRACE"
    elif level == 10:
    	level = "DEBUG"
    elif level == 20:
    	level = "INFO"
    elif level == 25:
    	level = "SUCCESS"
    elif level == 30:
    	level = "WARNING"
    elif level == 40:
    	level = "ERROR"
    elif level == 50:
    	level = "CRITICAL"
    else:
    	level = "TRACE"

    logger.add("logs/log_{time}.log", level=level, format="<green>{time}</green> <level>{message}</level>",
               serialize=True, enqueue=True, rotation="10 MB", retention="14 days", compression="zip")

    logger.level(level)

    return logger