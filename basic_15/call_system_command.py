import subprocess
from threading import Timer
import platform


def is_win():
    return platform.system().lower() == 'windows'


def is_linux():
    return platform.system().lower() == 'linux'


def execute(command, timeout=30):
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print("Run command: %r" % command)
    try:
        stdout, stderr = p.communicate(timeout=timeout)
        ret_code = p.returncode
        print("---------------")
        print("Return code: %r" % ret_code)
        print("Stdout: %r" % stdout)
        print("Stderr: %r" % stderr)
        print("---------------")
        return ret_code, stdout, stderr
    except Exception as e:
        raise e


def import_backups(command, timeout=300, retry_times=5):
    for i in range(retry_times):
        print("Importing backups at #%r times..." % i)
        try:
            ret_code, stdout, stderr = execute(command, timeout)
            if ret_code == 0:
                print("Succeed to import backups.")
                return True
        except Exception as e:
            print("Failed to import backups, exception: %r" % e)
            print(e)
    print("Failed to import backups.")
    return False


if __name__ == '__main__':
    ret = None
    if is_win():
        ret = import_backups("python.exe D:\\work\\python_workspace\\python_study\\basic_15\\test_timeout.py", timeout=2)
    elif is_linux():
        ret = execute("ls /")
    else:
        print("Not supported platform.")
