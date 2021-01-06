# -*- coding: utf-8 -*-

# Std Library
import sys

# Project Library
from .logger import LogSetting

log = LogSetting().log_set('cmd')


def command_check(options):
    command = [k for k, v in options.items() if v == True]
    mode_list = ['test', 'dev', 'real']

    log.debug("=========Command Manager=========")
    log.debug("Command: {}".format(command))
    log.debug("Input Options: {}".format(options))

    if len(command) > 1:
        print("More than one option is not allowed: {}".format(len(command)))
        sys.exit(1)
    elif len(command) == 0:
        print("Please enter an option")
        print("Use -h for help")
        sys.exit(1)
    elif options['mode'].lower() not in mode_list:
        print("Unsupported agent mode: {}".format(options['mode']))
        print("Support mode: {}".format(mode_list))
        sys.exit(1)

    return command[0]