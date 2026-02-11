from US_Visa .logger import logging
from US_Visa.exception import USVisaException
logging.info("This is a test log message.")
import sys



try:
    r=3/0
    print(r)
except Exception as e:
    raise USVisaException(e, sys)