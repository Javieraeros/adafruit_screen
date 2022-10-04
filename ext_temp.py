from time import *
from subprocess import check_output

def get_temp():
    process = check_output(['ssh', 'javi@zero2pi', 'sh', 'scripts/lm75.sh'])
    return process.decode('utf-8')
