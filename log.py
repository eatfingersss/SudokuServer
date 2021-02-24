import time
import inspect
import io
import os

class LogConfig:

    def __init__(self):
        self.level = "debug"
        self.log_file = "game.log"
        self.stdout = True
        self.file_h = None

    def open(self):
        if self.file_h == None:
            self.file_h = io.open(self.log_file, "a")

    def scan(self):
        self.file_h == None
        error("uncomplete part")



_log_config = LogConfig()

_LEVEL = ["TRACE", "DEBUG", "INFO", "WARN", "ERROR"]

_CURRENT_LEVEL = os.getenv("VERBOSE") or "DEBUG"

def trace(msg, *data):
    log("TRACE", msg, *data)

def debug(msg, *data):
    log("DEBUG", msg, *data)

def info(msg, *data):
    log("INFO", msg, *data)

def warn(msg, *data):
    log("WARN", msg, *data)

def error(msg, *data):
    log("ERROR", msg, *data)

def log(level, msg, *data):
    if check(level) == False:
        return
    if data == None:
        _MSG = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " ["+ level +"] " + msg
    else:
        _MSG = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " ["+ level +"] {}@{}[{}]\t" + msg.format(*data)
    _stack = inspect.stack()[2]
    _MSG=_MSG.format(_stack.filename, _stack.function, _stack.lineno)
    write(_MSG)

def check(level):
    return _LEVEL.index(level) >= _LEVEL.index(_CURRENT_LEVEL)

def write(data):
    if _log_config.stdout:
        print(data)
    if not _log_config.file_h :
        _log_config.file_h = io.open(_log_config.log_file, "a")
    _log_config.file_h.writelines(data + "\n")
