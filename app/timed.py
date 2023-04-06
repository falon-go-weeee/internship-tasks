import time
import logging
from functools import wraps

logging.basicConfig()
logger = logging.getLogger("my-logger")
logger.setLevel(logging.DEBUG)

def timed(func):
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time_ns()
        result = func(*args, **kwargs)
        end = time.time_ns()
        logger.debug("{} ran in {}ns".format(func.__name__, round(end - start, 2)))
        return result

    return wrapper