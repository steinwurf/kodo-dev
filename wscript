#! /usr/bin/env python
# encoding: utf-8

APPNAME = 'kodo-dev'
VERSION = '0.0.0'

from waflib.extras.wurf.waf_build_context import WafBuildContext
from waflib.extras.wurf.waf_resolve_context import WafResolveContext


class FixResolveContext(WafResolveContext):
    """ The WafResolveContext is used during the resolve phase. We set
    is_toplevel() to return always True otherwise internal dependencies are
    skipped. Since are building multiple projects and their tests etc. we also
    need their internal dependencies e.g. gtest, stub etc.
    """

    def is_toplevel(self):
        return True

class FixBuildContext(WafBuildContext):
    """ The WafBuildContext is executed during a build. We set is_toplevel()
    True where we also want to build examples or unit tests.
    """
    def is_toplevel(self):

        if self.path == self.srcnode:
            return True
        if 'kodo-core' in str(self.path):
            return True
        if 'kodo-rlnc' in str(self.path):
            return True
        if 'kodo-reed-solomon' in str(self.path):
            return True
        if 'kodo-fulcrum' in str(self.path):
            return True
        else:
            return False

def build(bld):
    pass

