import logging
import os
from datetime import datetime



logger = logging.getLogger("logger")
logger.setLevel(logging.INFO)
logger.propagate = False 

if not logger.handlers:
    formatter = logging.Formatter(
        '[%(asctime)s] %(levelname)s : %(name)s: %(message)s'
    )

   
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

   
    




