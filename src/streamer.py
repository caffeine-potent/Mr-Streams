class pStream:
    
###PRIVATE FUNCTIONS
    def _builder(self, expression):
        self.STR = expression
        return self

    def _flatten(self,generator,function):
        for thing in generator:
            for value in function(thing):
                yield value

###OVERRIDES
    def next(self):
        return next(self.STR)

    def __init__(self, iterable_thing):
        self.STR = iterable_thing

    def __iter__(self):
        return iter(self.STR)

### TRANSFORMS
    def map(self,function):
        return self._builder(map(function, self.STR))

    def flatmap(self, function):
        return self._builder(self._flatten(self.STR, function))

### CONSUMERS
    def print_stream(self):
        print(list(self.STR))

    def consume(self, function):
        function(self.STR)

    def drain(self):
        for x in self.STR:
            pass
