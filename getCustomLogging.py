#!/usr/bin/env python3

import logging, logging.handlers
from datetime import datetime

def get_logging(LogFileName):
    try:
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        handler = logging.handlers.RotatingFileHandler(LogFileName, maxBytes=10000000, backupCount=5)
        formatter = logging.Formatter('%(asctime)s, : %(levelname)s, : %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        #logger_now = datetime.now().strftime("%Y/%m/%D %H:%M:%S %p")
    
    except Exception as e:
        print(f"There was an exception in '{get_logging.__module__}' : ", e)
