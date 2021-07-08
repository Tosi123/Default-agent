# -*- coding: utf-8 -*-

# Std Library
import os
import sys
import time
import signal

# Project Library
from .env import AGENT_HOME, PID_FILE
from .logger import LogSetting
from .exception import MethodNotImplementedError
from .platform import Platform


log = LogSetting().log_set(__name__)


class Daemon:
    """
    stop, start 등 데몬 컨트롤 클래스 
    """

    def __init__(self, home_path=AGENT_HOME, pid_file=PID_FILE):
        self.home_path = home_path
        self.pid_file = pid_file

    def _default_setting(self):
        os.chdir(self.home_path)
        os.umask(0o022)
        os.setsid()

    def pid_check(self):
        """
        PID 파일 pid 값 확인 함수
        """
        try:
            file = open(self.pid_file, 'r')
            pid = int(file.read().strip())
            file.close()
            return pid
        except FileNotFoundError:
            return False
        except Exception as e:
            log.exception("PID check fail")
            sys.exit(1)

    def pidfile_write(self):
        try:
            pid = os.getpid()
            file = open(self.pid_file, 'wt')
            file.write(str(pid))
            file.close()
            os.chmod(self.pid_file, 0o644)
        except Exception as e:
            log.exception("PID file create fail")
            sys.exit(1)

    def daemon_fork(self):
        """
        자식 프로세스 생성 함수
        """
        try:
            fork = os.fork()
            if fork > 0:
                # 부모 프로세스 종료
                sys.exit(0)
            self._default_setting()
            log.debug(f"Fork create success: {fork}")
        except Exception as e:
            log.exception("Daemon fork fail")
            sys.exit(1)

    def start(self):
        log.info("=========Start Daemon=========")
        pid = self.pid_check()
        status = Platform.ps_status(pid)

        if status:
            log.warn(f"Don't start daemon Already starting: {pid}")
            return False
        elif status == None:
            log.error(f"Daemon status check fail: {pid}")
            return False

        # Daemon 생성 후 Main Logic 실행
        self.daemon_fork()
        log.info("Daemon Default Setting Start..")
        self.pidfile_write()
        log.info("Daemon Logic Start..")
        self.run()

    def stop(self):
        log.info("=========Stop Daemon=========")
        pid = self.pid_check()
        status = Platform.ps_status(pid)

        if status == False:
            log.warn("Daemon already stopped")
            return True
        elif status == None:
            log.error(f"Daemon status check fail: {pid}")
            return False

        try:
            os.kill(os.getpgid(pid), signal.SIGTERM)
            log.info("Parent process shutdown start...")
        except ProcessLookupError:
            try:
                log.warn(f"Unable to kill parent process: {os.getpgid(pid)}")
                os.kill(pid, signal.SIGTERM)
                log.info("Daemon shutdown start...")
            except ProcessLookupError:
                log.warn("Daemon not found")
            except Exception as e:
                log.exception(f"Daemon shutdown error: {e}")
                return False
        except Exception as e:
            log.exception(f"Parent process kill error: {e}")
            return False

        # Stop sginal 보낸뒤 프로세스 죽은지 확인 후 파일 삭제
        while True:
            if Platform.ps_status(pid) == False:
                log.info(f"Daemon shutdown successful: {pid}")
                break
            log.info("Stopping...")
            time.sleep(1)

        if os.path.exists(self.pid_file):
            os.remove(self.pid_file)
        return True

    def restart(self):
        if self.stop():
            self.start()

    def status(self):
        pid = self.pid_check()
        if Platform.ps_status(pid):
            print("=========DAEMON STATUS=========")
            print(f"PID: {pid}")
            print(f"Status: Running")
            print(f"System CPU Core: {Platform.sys_cup_count()}ea")
            print(f"System CPU Used: {Platform.sys_use_cpu()}%")
            print(f"System Memory Free: {Platform.sys_free_mem()}MB")
            print(f"Process CPU Used: {Platform.use_mem(pid)}%")
            print(f"Process Memory Used: {Platform.use_mem(pid)}MB")
            print("==============================")
        else:
            print("=========DAEMON STATUS=========")
            print("Status: Stopped")
            print(f"System CPU Core: {Platform.sys_cup_count()}ea")
            print(f"System CPU Used: {Platform.sys_use_cpu()}%")
            print(f"System Memory Free: {Platform.sys_free_mem()}MB")
            print("==============================")

    def run(self):
        raise MethodNotImplementedError(self.__class__.__name__)
