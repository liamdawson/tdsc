from __future__ import unicode_literals, absolute_import, print_function
import platform
import appdirs


class ContextInfo:
    @property
    def platform(self):
        return platform.system()


class ContextStore:
    pass


class Context:
    __store = ContextStore()
    info = ContextInfo()

    @property
    def store(self):
        return self.__store

    def paths_for_state(self, state_name, version=None, roaming=False):
        return appdirs.AppDirs(state_name, 'tdsc', version=version, roaming=roaming)
