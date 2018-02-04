from functools import partial, reduce

class EOL():
    pass

class Streamer:
    def __init__(self, _iter):
        self.structure = iter(_iter)
        self.eol = EOL()

    def _build(self, expression):
        self.structure = expression
        self.structure = iter(self.structure)
        return self

    def __iter__(self):
        return self

    def __next__(self):
        _obj = next(self.structure, self.eol)
        if _obj is not self.eol:
            return _obj
        else:
            raise StopIteration

    def _flatten(self, _generator,_function):
        yield from (y for x in _generator for y in _function(x))

    def map(self, _function, *args, **kwargs):
        _curried_function = partial(_function, *args, **kwargs)
        return self._build(map(_curried_function, self.structure))

    def flatmap(self, _function, *args, **kwargs):
        _curried_function = partial(_function, *args, **kwargs)
        return self._build(self._flatten(self.structure, _curried_function))

    def reduce(self, _function, *args, **kwargs):
        _curried_function = partial(_function, *args, **kwargs)
        return reduce(_curried_function)

    def filter(self, _function, *args, **kwargs):
        _curried_function = partial(_function, *args, **kwargs)
        return self._build(filter(_curried_function, self.structure))

    def tap(self, _function, *args, **kwargs):
        def _tap(function, iterable):
            for x in iterable:
                yield function(x)
        _curried_function = partial(_function, *args, **kwargs)
        return self._build(_tap(_curried_function, self.structure))

    def drain(self):
        for _ in self.structure:
            continue