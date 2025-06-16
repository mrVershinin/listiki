import logging


RESET = "\033[0m"

LEVEL_COLOR_MAP = {
    "DEBUG": "\033[37m",  # Белый
    "INFO": "\033[34m",  # Синий
    "WARNING": "\033[33m",  # Жёлтый
    "ERROR": "\033[31m",  # Красный
    "CRITICAL": "\033[1;31m",  # Жирный красный
}


class ColoredFormatter(logging.Formatter):
    def format(self, record):
        color = LEVEL_COLOR_MAP.get(record.levelname, RESET)
        log_message = super().format(record)
        return f"{color}{log_message}{RESET}"


def setup_logging(level=logging.INFO):
    LOG_FORMAT = (
        "\n[%(asctime)s] %(levelname)-8s | "
        "%(name)s : %(funcName)s : %(lineno)d\n"  #
        "%(message)s\n"
    )
    DATE_FORMAT = "%d/%m %H:%M:%S"

    formatter = ColoredFormatter(LOG_FORMAT, datefmt=DATE_FORMAT)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(level)

    root_logger = logging.getLogger()
    root_logger.setLevel(level)
    root_logger.addHandler(console_handler)

    return root_logger
