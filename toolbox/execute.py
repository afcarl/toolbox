from __future__ import print_function
import subprocess

c_end     = '\033[0m'
c_cyan    = '\033[0;36m'

def execute(cmd, verbose=True, quiet=False):
    if not quiet:
        print(cmd)
    try:
        proc = subprocess.Popen(cmd,  stdin=subprocess.PIPE,
                                     stdout=subprocess.PIPE,
                                      shell=True)

        stdout, stderr = proc.communicate()
        if (not quiet) and verbose:
            print(c_cyan+stdout+c_end)
    except OSError as e:
        print(cmd)
        raise e
