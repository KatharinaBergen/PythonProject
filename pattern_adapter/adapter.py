from abc import abstractmethod, ABC


class LegacyLogger:
    def write_to_logfile(self, msg: str, level: str) -> None:
        print(f"[{level.upper()}] {msg}")

#ADAPTER PATTER: legacy/third party/ even BE code is wrapped by an adapter to meet new or different needs
class Logger(ABC):
    @abstractmethod
    def log(self, msg: str) -> None:
        pass

class LegacyLoggerAdapter(Logger):
    def __init__(self, legacy_logger: LegacyLogger, default_level: str = "debug"):
        self.legacy_logger = legacy_logger
        self.default_level = default_level

    def log(self, msg: str) -> None:
        self.legacy_logger.write_to_logfile(msg, level=self.default_level)
