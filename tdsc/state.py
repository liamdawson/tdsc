from __future__ import unicode_literals, absolute_import, print_function
from abc import ABC, abstractmethod


class State(ABC):
    def should_execute(self, ctx):
        raise NotImplemented

    @abstractmethod
    def execute(self, ctx):
        raise NotImplemented

    def post_execute(self, ctx, result):
        return result

    def run(self, ctx):
        try:
            if self.should_execute(ctx):
                result = self.execute(ctx)
                return self.post_execute(ctx, result)
        except Exception as err:
            return err
