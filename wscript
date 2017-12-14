#! /usr/bin/env python
# encoding: utf-8

APPNAME = 'kodo-dev'
VERSION = '0.0.0'


from waflib.Configure import conf

@conf
def is_toplevel(self):
    """
    Returns true if the current script is the top-level wscript
    """
    print(self.path)

    if 'kodo-core' in str(self.path):
        return True
    if 'kodo-rlnc' in str(self.path):
        return True
    else:
        return False




def build(bld):

    pass
