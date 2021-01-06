# -*- coding: utf-8 -*-

# Std Library
import os
import json
import logging
import logging.config

# Project Library
from .env import LOG_CONFIG
from .exception import PathNotFound


class LogSetting:
    @classmethod
    def log_set(cls, name="main"):
        if os.path.exists(LOG_CONFIG):
            with open(LOG_CONFIG, 'rt') as file:
                config = json.load(file)
                logging.config.dictConfig(config)
                # Logging Config에 등록된 값 없을 경우 default 설정
                if name not in config['loggers'].keys():
                    name = "main"
                logger = logging.getLogger(name)
                file.close()
                return logger
        else:
            raise PathNotFound(LOG_CONFIG)
