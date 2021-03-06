#!/usr/bin/env python
from localconfig import *
from datetime import datetime
import sys, subprocess, os, math

def check_output(command):
    print ' '.join(command)
    return subprocess.Popen(command, stdout=subprocess.PIPE).communicate()[0]


seqfile=sys.argv[1]
sys.stderr.write(str(datetime.now()) + ': running Psipred\nThis may take quite a few minutes!\n')
check_output([psipred, seqfile])
