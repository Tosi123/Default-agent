# -*- coding: utf-8 -*-

# Std Library
import sys

# Project Library
from core.agent import Agent
from core.config import AgentSettiong
from core.logger import LogSetting
from core.command import command_check
from core.platform import Platform

log = LogSetting().log_set(__name__)


def main():
    # 운영체제 검사 Linux만 허용
    if Platform.get_os() != 'linux':
        log.error(f"This operating system is not supported: {Platform.get_os()}")
        log.error("Linux only...")
        sys.exit(1)

    setting = AgentSettiong()
    # 명령어 옵션 가져오고 Format 검증
    options = setting.get_options()
    command = command_check(options)
    agent_config = setting.read_config(options['mode'].lower())
    agent = Agent()

    if command == 'start':
        agent.start()
    elif command == 'stop':
        agent.stop()
    elif command == 'restart':
        agent.restart()
    elif command == 'status':
        agent.status()
        sys.exit(0)
    elif command == 'version':
        print(f"Name: {setting.get_name}")
        print(f"Version: {setting.get_version}")
        sys.exit(0)


if __name__ == "__main__":
    main()
