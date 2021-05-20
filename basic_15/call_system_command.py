import subprocess
from threading import Timer
import platform


def is_win():
    return platform.system().lower() == 'windows'


def is_linux():
    return platform.system().lower() == 'linux'


def execute(command, timeout=30):
    # p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p = subprocess.Popen("dir C:", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #timer = Timer(timeout, p.terminate())
    try:
        #timer.start()
        stdout, stderr = p.communicate(timeout=10)
        ret_code = p.returncode
        return ret_code, stdout, stderr
    except Exception as e:
        raise e
    finally:
        #timer.cancel()
        pass


if __name__ == '__main__':
    # subprocess.Popen("notepad.exe test.txt", shell = True)

    #p = subprocess.Popen("dir C:", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #stdout, stderr = p.communicate()
    #print(p.returncode)
    #print(stdout)
    #print(stderr)

    #exit(0)

    ret = None
    if is_win():
        ret = execute("notepad.exe")
    elif is_linux():
        ret = execute("ls /")
    else:
        print("Not supported platform.")
    print(ret[0])
    print(ret[1])
    print(ret[2])
