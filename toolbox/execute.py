from __future__ import print_function
import subprocess

c_end     = '\033[0m'
c_cyan    = '\033[0;36m'

def execute(cmd, verbose=True):
    print(cmd)
    try:
        proc = subprocess.Popen(cmd,  stdin=subprocess.PIPE,
                                     stdout=subprocess.PIPE,
                                      shell=True)

        stdout, stderr = proc.communicate()
        if verbose:
            print(c_cyan+stdout+c_end)
    except OSError as e:
        print(cmd)
        raise e
