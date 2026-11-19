class Tensor:
    def __init__(self, data, shape=None):
        self._data, self._shape = self._flatten_nested(data)
        if shape:
            total = reduce(lambda a,b: a*b, shape, 1)
            if total != len(self._data):
                raise ValueError(...)
            self._shape = tuple(shape)
        self._strides = self._compute_strides(self._shape)