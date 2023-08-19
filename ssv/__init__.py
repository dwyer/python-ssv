import re


class reader:

    def __init__(self, f):
        self._f = f
        self._line = None
        self._next()

    def __iter__(self):
        while self._line:
            yield self._readrow()

    def _next(self):
        self._line = self._f.readline()

    def _readrow(self):
        row = tuple(re.split(r'\s{2,}', self._line.rstrip('\n')))
        self._next()
        return row


class DictReader(reader):

    def __init__(self, f):
        super().__init__(f)
        self.fieldnames = self._readrow()

    def __iter__(self):
        while self._line:
            row = self._readrow()
            yield dict(zip(self.fieldnames, row))
