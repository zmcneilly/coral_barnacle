import logging
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)
if os.getenv("STAGE", "") == "dev":
    logger.setLevel(logging.DEBUG)
