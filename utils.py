from datetime import datetime
from utc import utc
import sys

def get_timestamp():
    timestamp = datetime.now(utc).strftime("[%d/%b/%Y:%H:%M:%S %z]")
    return timestamp

def log_stdout(msg):
    sys.stdout.write(get_timestamp() + " [info] " + msg + "\n")
    sys.stdout.flush()

def log_stderror(msg):
    sys.stderror.write(get_timestamp() + " [error] " + msg + "\n")
    sys.stderror.flush()
