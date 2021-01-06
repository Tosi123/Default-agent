# -*- coding: utf-8 -*-

# Std Library
import platform

# 3rd Library
import psutil


class Platform:
    """
    시스템 운영체제 및 하드웨어 정보 클래스
    """
    @staticmethod
    def get_os():
        return {
            'linux': 'linux',
            'darwin': 'mac',
            'windows': 'windows',
        }.get(platform.system().lower(), 'unknown')

    @staticmethod
    def sys_free_mem():
        return round(psutil.virtual_memory().free / (1024*1024))  # Byte -> MB

    @staticmethod
    def sys_use_cpu():
        return psutil.cpu_percent()

    @staticmethod
    def sys_cup_count(logical=True):
        # True == 논리적 코어
        # False == 물리적 코어
        return psutil.cpu_count(logical=logical)

    @staticmethod
    def use_cpu(pid):
        try:
            return psutil.Process(pid).cpu_percent()
        except psutil.NoSuchProcess:
            return None

    @staticmethod
    def use_mem(pid):
        try:
            # Byte -> MB
            return round(psutil.Process(pid).memory_info()[0] / (1024*1024))
        except psutil.NoSuchProcess:
            return None

    @staticmethod
    def ps_status(pid):
        try:
            return psutil.pid_exists(pid)
        except psutil.NoSuchProcess:
            return False
        except Exception as e:
            return None
