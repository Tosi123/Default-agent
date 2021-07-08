# -*- coding: utf-8 -*-

# Std Library
import os
from configparser import ConfigParser
from optparse import OptionParser, Values

# Project Library
from .env import AGENT_NAME, AGENT_CONFIG, AGENT_CONFIG_DEV, AGENT_VERSION
from .logger import LogSetting
from .exception import PathNotFound

log = LogSetting().log_set(__name__)


class AgentSettiong:

    def get_options(self):
        parser = OptionParser()
        parser.add_option("-A", "--start", dest="start",
                          default=False, action="store_true", help="Agent를 기동 합니다.")
        parser.add_option("-S", "--stop", dest="stop",
                          default=False, action="store_true", help="Agent를 종료 합니다.")
        parser.add_option("-R", "--restart", dest="restart",
                          default=False, action="store_true", help="Agent를 재기동 합니다.")
        parser.add_option("-I", "--status", dest="status",
                          default=False, action="store_true", help="Agent 상태를 출력 합니다.")
        parser.add_option("-V", "--version", dest="version",
                          default=False, action="store_true", help="Agent 버전을 출력 합니다.")
        parser.add_option("-M", "--mode", dest="mode", default="real",
                          action="store", help="Agent 실행 모드를 선택 합니다 (real, test #default: real)")

        try:
            options, args = parser.parse_args()
            option_dict = vars(options)
        except Exception as e:
            log.error(f"Agent Options Load Error: {e}")
            option_dict = {'agent_start': False,
                           'agent_stop': False,
                           'agent_stauts': True,
                           'version_show': False,
                           'agent_mode': 'real'}
        return option_dict

    def read_config(self, mode):
        config = ConfigParser()
        result = {}

        # Agent mode에 맞게 Config 읽어오기
        if mode == 'real':
            if os.path.exists(AGENT_CONFIG):
                config.read(AGENT_CONFIG)
            else:
                raise PathNotFound(AGENT_CONFIG)
        elif mode == 'test' or mode == 'dev':
            if os.path.exists(AGENT_CONFIG_DEV):
                config.read(AGENT_CONFIG_DEV)
            else:
                raise PathNotFound(AGENT_CONFIG_DEV)

        # Config에서 가져올 항목
        result['string'] = config.get('DATABASE', 'STRING')
        result['number'] = config.getint('DATABASE', 'NUMBER')
        result['boolean'] = config.getboolean('DATABASE', 'BOOLEAN')
        return result

    @property
    def get_version(self):
        return AGENT_VERSION

    @property
    def get_name(self):
        return AGENT_NAME
