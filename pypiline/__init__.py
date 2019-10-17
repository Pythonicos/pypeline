__all__ = ['Pypiline']

from functools import partial


_DEFAULT = object()


class Pypiline:
    def __init__(self):
        self._funcs = []

    def append_context(self, context_pipeline) -> 'Pypiline':
        self._funcs.append(context_pipeline)
        return self

    def append(self, method, *args, **kwargs) -> 'Pypiline':
        self._funcs.append(partial(method, *args, **kwargs))
        return self

    def do(self, last_value=None):
        result = last_value or _DEFAULT
        for method in self._funcs:
            if isinstance(method, Pypiline):
                if result is _DEFAULT:
                    method.do()
                else:
                    method.do(result)
                result = _DEFAULT
            else:
                if result is _DEFAULT:
                    result = method()
                else:
                    result = method(result)
        return None if result is _DEFAULT else result

