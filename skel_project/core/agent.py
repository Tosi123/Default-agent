# -*- coding: utf-8 -*-

# Std Library
import time
import signal

# Project Library
from .daemon import Daemon
from .logger import LogSetting

log = LogSetting().log_set(__name__)


class Agent(Daemon):

    def __init__(self):
        super(Agent, self).__init__()
        self.run_loop = True

    def _sigterm_handle(self, signum, frame):
        log.debug(f"Shutdown the loop... Signal entered: {signum}")
        self.run_loop = False

    def run(self):
        # Sgiterm 시그널 왔을 경우 종료 처리 stop() 함수
        signal.signal(signal.SIGTERM, self._sigterm_handle)

        while self.run_loop:
            log.info('Test Agent')
            time.sleep(5)

        log.info("Agent stop")
