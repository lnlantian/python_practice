##   进度条显示

#!/usr/bin/env python
# coding:utf-8

import time
import sys


def progress_test():
    bar_length = 50
    for percent in xrange(0, 100):
        hashes = '#' * int(percent / 100.0 * bar_length)
        spaces = ' ' * (bar_length - len(hashes))
        sys.stdout.write("\rPercent: |%s| %d%%   %s" % (hashes + spaces, percent, time.strftime("%a %b %d %H:%M:%S %Y",time.localtime())))
        sys.stdout.flush()
        time.sleep(1)


progress_test()
