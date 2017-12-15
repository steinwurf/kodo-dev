#! /usr/bin/env python
# encoding: utf-8

APPNAME = 'kodo-dev'
VERSION = '0.0.0'

from waflib.extras.wurf.waf_build_context import WafBuildContext
from waflib.Build import BuildContext

from waflib.extras.wurf.waf_configuration_context import WafConfigurationContext
from waflib.Configure import ConfigurationContext

from waflib.extras.wurf.waf_resolve_context import WafResolveContext

from waflib.TaskGen import feature, after_method



class FixResolveContext(WafResolveContext):

    def is_toplevel(self):
        return True

class FixConfigurationContext(WafConfigurationContext):
   
    def execute(self):
        
    

        super(FixConfigurationContext, self).execute()
        self.recurse_dependencies()

    def pre_recurse(self, node):
        print(node)
        super(ConfigurationContext, self).pre_recurse(node)

    def is_toplevel(self):
        return True

class FixBuildContext(WafBuildContext):
   
    def execute(self):
        
        self.restore()
        if not self.all_envs:
            self.load_envs()
        self.recurse_dependencies()
        super(FixBuildContext, self).execute_build()


    def pre_recurse(self, node):
        print(node)
        super(BuildContext, self).pre_recurse(node)

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
