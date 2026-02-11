import logging
import os

from from_root import from_root
from datetime import datetime
log_dir = "logs"
LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

logs_path = os.path.join(log_dir, LOG_FILE)
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    filename=logs_path,
    format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG,
)